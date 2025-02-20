                                                        #CLASS
# class Amarine:
#     def __init__(self, name, age, type):
#         self.name = name
#         self.age = age
#         self.type = type
#     def serang (self,hero):
#         self.hero = print(self.name + "Serang " + hero)
#     def counter (self,korban):
#         self.korban = print(self.name + " Counter " + korban)

# penyerang=Amarine("Zilong ","20","Assasin")
# diserang=Amarine("Alucard","21", "Dark sistenk" )

# penyerang.serang(diserang.name)
# diserang.counter(penyerang.name)

# class access:
#     def __init__(self, name, age, type):
#         self.__name = name
#         self.__age = age
#         self.__type = type
#     @property
#     def type(self):
#         return self.__type
#     @type.getter
#     def type(self):
#         return self.__type
#     @type.setter
#     def type(self, type):
#         self.__type = type

#     @property
#     def name(self):
#         return self.__name
#     @name.getter
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, name):
#         self.__name = name

# zilong = access ("Zilong", "20", "Assasin")
# print(zilong.type)
# zilong.type = "Fighter"
# print(zilong.type)

# Trans = access ("andre", "23", "mage")
# print(Trans.name)
# Trans.name = "andriana"
# print(Trans.name)

                                            #CLASS INHERITENCE

# class inheritence:
#     def __init__(self, name, age, type):
#         self.name = name
#         self.age = age
#         self.type = type

# class subinheritence(inheritence):
#     pass

# andre = inheritence("Andre", "20", "Mage")
# print (andre.name)
# Andriana = inheritence ("Andriana", "23", "Mage")
# print ("menjadi " + Andriana.name + " Anak Kucay")

                                        #MULTI INHERITENCE

# class setX:
#     print ("ini adalah class setX")
# class typeX:
#     print ("ini adalah class typeX")

# class MultiInheritence(setX, typeX):
#     def __init__ (self,name, type, color):
#         self.name = name
#         self.type = type
#         self.color = color
    
#     def show(self):
#         print("Namanya adalah " + self.name + " rasnya " + self.type + " warnanya " + self.color)

# multi=MultiInheritence("Andre", "batak", "black")
# multi.show()

#                                                 SUPER

# class setX:
#     def __init__(self, name, age, color,type):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.type = type

# class typeX:
#     def __init__(self, name, age, color,type):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.type = type

# class MultiInheritence(setX, typeX):
#     def __init__(self, name, age, color,type):
#         super().__init__(name, age, color,type)

#     def __init__ (self,name, age, color,type):
#         super().__init__(name,age, color ,type)

#     def show(self):
#         print("Namanya adalah " + self.name + " rasnya " + self.age + " warnanya " + self.color + " Kerjanya " + self.type)

# multi=MultiInheritence("Andre", "batak","hitam", "pengrodok")
# multi.show()

                                        #ABSTRACT

# from abc import ABC, abstractmethod #UNTUK MEMANGGIL ABSTRAK
# class setX:
#     def __init__(self, name, age, color,type):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.type = type
        
#     @abstractmethod #UNTUK MENGOPER KE FUGSI DI BAWAH
#     def show(self):
#         pass

# class typeX:
#     def __init__(self, name, age, color,type):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.type = type

#     @abstractmethod 
#     def rodok(self):
#         pass

# class MultiInheritence(setX, typeX):
#     def __init__(self, name, age, color,type):
#         super().__init__(name, age, color,type)

#     def __init__ (self,name, age, color,type):
#         super().__init__(name,age, color ,type)

#     def show(self): #MENGINISIASI FUNGSI DARI ABSTRACT DI ATAS
#         print("Namanya adalah " + self.name + " rasnya " + self.age + " warnanya " + self.color + " Kerjanya " + self.type)

#     def rodok(self): #MENGINISIASI FUNGSI DARI ABSTRACT DI ATAS
#         print("Andre adalah pengrodok")

# multi=MultiInheritence("Andre", "batak","hitam", "pengrodok")
# multi.show()
# multi.rodok()

                                    #MAGIC METHOD

# class setX:
#     def __init__(self, name, age, color,type):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.type = type
    
#     def __str__(self): #MAGIC METHOD
#         return "Namanya adalah " + self.name + " rasnya " + self.age + " warnanya"
    
# class typeX:
#     def __init__(self, name, age, color,type):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.type = type

#     def __repr__(self): #MAGIC METHOD
#         return "Hai"
    

# class MultiInheritence(setX, typeX):
#     def __init__(self, name, age, color,type):
#         super().__init__(name, age, color,type)

#     def __init__ (self,name, age, color,type):
#         super().__init__(name,age, color ,type)

#     def show(self):
#         print("Namanya adalah " + self.name + " rasnya " + self.age + " warnanya " + self.color + " Kerjanya " + self.type)

# multi=MultiInheritence("Andre", "batak","hitam", "pengrodok")
# multi.show()
# print(multi)

                                        #DECORATOR

class setX:
    def __init__(self, name, age, color,type):
        self.name = name
        self.age = age
        self.color = color
        self.type = type
    

class typeX:
    def __init__(self, name, age, color,type):
        self.name = name
        self.age = age
        self.color = color
        self.type = type

class MultiInheritence(setX, typeX):
    def __init__(self, name, age, color,type):
        super().__init__(name, age, color,type)

    def __init__ (self,name, age, color,type):
        super().__init__(name,age, color ,type)

    def show(self):
        print("Namanya adalah " + self.name + " rasnya " + self.age + " warnanya " + self.color + " Kerjanya " + self.type)

multi=MultiInheritence("Andre", "batak","hitam", "pengrodok")
multi.show()