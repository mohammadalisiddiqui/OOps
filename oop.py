# class Myclass:
#     x=5
#     y = "ali"
#     z = 44.5
#     car = "Hi_Roof"

# p1 = Myclass()
# print(p1.x)
# print(p1.y)
# print(p1.z)
# print(p1.car)    

# class cons:
#    def __init__(self, name, age): #self is for refrencing
#         self.name =name
#         self.age = age
# p1 = cons("Ali",25)
# print(p1.name)
# print(p1.age)

# class cons:
#     def __init__(self, name, age): #self is for refrencing
#         self.name =name
#         self.age = age
#     def myfun(self):       #this self refrence function self to constructor self
#         print("My name is "+self.name)
#         print("And Im {} years old ".format(self.age))
# p1 = cons("Ali",25)
# p1.myfun()

# class new_class:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
#     def myfun(self):
#         print("name is"+self.name)
#         print("And Im {} years old ".format(self.age))
# p1 = new_class("ahad",30)
# p1.name = "ali"
# # del p1.name   delete object attribute name
# # del p1  delete whole object
# p1.myfun()

                    #  parent and child class

# class person:
#     def __init__ (self, fname,lname):
#         self.fisrt = fname
#         self.last = lname
#     def printname(self):
#         print(self.fisrt,self.last)  #also hide this
#         print(self)
# class firefighter(person):
#     def __init__ (self, fname,lname):
#         self.fisrt1 = lname
#         self.last1 = fname
#     def printname1(self):
#         print(self.fisrt1,self.last1)
# p1 = firefighter("Ali","Siddiqui")
# p1.printname1()



class person:
    def __init__ (self, fname,lname):
        self.fisrt = fname
        self.last = lname
    def printname(self):
        print(self.fisrt,self.last)  #also hide this
        print(self)
class firefighter(person):
    def __init__ (self, fname,lname):
       person.__init__(self,fname,lname)
    def printname1(self):
        print(self.fisrt1,self.last1)
p1 = firefighter("Ali","Siddiqui")
p1.printname1()

