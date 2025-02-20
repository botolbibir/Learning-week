                                        #ASD 
                                    #SINGLE LIST 
# class Node:
#     """Represents a node in a linked list."""
#     def __init__(self, data, next=None):
#         """
#         Initializes a Node with the given data and optional next node.

#         Args:
#             data: The data to be stored in the node.
#             next (Node, optional): The next node in the linked list. Defaults to None.
#         """
#         self.data = data
#         self.next = next

# class LinkedList:
#     """Represents a linked list."""
#     def __init__(self, root=None):
#         """
#         Initializes a LinkedList with an optional root node.

#         Args:
#             root (Node, optional): The root node of the linked list. Defaults to None.
#         """
#         self.root = root
#         self.size = 0

#     def add_node(self, data):
#         """
#         Adds a new node with the given data to the end of the linked list.

#         Args:
#             data: The data to be stored in the new node.
#         """
#         new_node = Node(data)

#         if self.root is None:
#             self.root = new_node
#         else:
#             current_node = self.root
#             while current_node.next:
#                 current_node = current_node.next
#             current_node.next = new_node

#         self.size += 1  # Corrected the increment operator

#     def __len__(self):
#         """
#         Returns the number of nodes in the linked list.
#         """
#         return self.size

#     def __repr__(self):
#         """
#         Returns a string representation of the linked list.
#         """
#         nodes = []
#         current_node = self.root
#         while current_node:
#             nodes.append(str(current_node.data))
#             current_node = current_node.next
#         return ' -> '.join(nodes)

# # Example usage:
# linked_list = LinkedList()
# linked_list.add_node(1)
# linked_list.add_node(2)
# linked_list.add_node(3)
# print(linked_list)  # Output: 1 -> 2 -> 3
# print(len(linked_list))  # Output: 3



                            #stack
class Stack:
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Adds an item to the top of the stack.

        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes the top item from the stack.

        Returns:
            The removed item.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack")

    def peek(self):
        """
        Returns the top item from the stack without removing it.

        Returns:
            The top item.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Cannot peek into an empty stack")

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of items in the stack.

        Returns:
            The number of items in the stack.
        """
        return len(self.items)
