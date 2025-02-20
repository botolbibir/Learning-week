class node: 
    def __init__(self, data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class dlinkedlist:
    def __init__(self,root=None):
        self.root=root
        self.last=root
        self.size=0

    def addNode(self,data):

        newNode=node(data)

        if self.root is None:
            self.root=newNode
            self.last=newNode
        else:
            self.last.next=newNode
            newNode.prev=self.last
            self.last=newNode

        self.size=+1
    
    def rmvNode(self,data):
        currentNode= self.root

        while currentNode is not None:
            if currentNode.data == data:
                if currentNode.prev is not None:
                    currentNode.prev.next == currentNode.next
                    if self.root:
                        self.root.prev = None
                    else:
                        self.last = None
                elif currentNode == self.last:
                    self.last = currentNode.prev
                    self.last.next=None
                else:
                    currentNode.prev.next = currentNode.next
                    currentNode.next.prev = currentNode.prev

                self.size -= 1
            currentNode = currentNode.next
                    

    def printNode(self):
        current = self.root
        while current is not None:
            print(current.data, end="<->")
            current = current.next
        print("None")

linkdlist=dlinkedlist()
linkdlist.addNode(1)
linkdlist.addNode(2)
linkdlist.addNode(3)
linkdlist.rmvNode(1)
linkdlist.printNode()