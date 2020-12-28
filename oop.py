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



# class person:
#     def __init__ (self, fname,lname):
#         self.fisrt = fname
#         self.last = lname
#     def printname(self):
#         print(self.fisrt,self.last)  #use parent property to print name by using child class
# class firefighter(person):
#     def __init__ (self, fname,lname):
#        person.__init__(self, fname, lname)
#     # def printname1(self):
#     #     print(self.fisrt1,self.last1)
# p1 = firefighter("Ali","Siddiqui")
# p1.printname()

            #  practice

# class person:
#     def __init__ (self, fname,lname):
#         self.fisrt = fname
#         self.last = lname
#     def printname(self):
#         print(self.fisrt,self.last)  #also hide this
# class firefighter(person):
#     def __init__ (self, fname,lname, midname):
#        super().__init__(self, fname, lname)
#        self.mid = midname
#     # def printname1(self):
#     #     print(self.fisrt1,self.last1)
# p1 = firefighter("Ali","Siddiqui","khan")
# p2
# p1.printname()
# print(p1.mid)



                                # 24 Dec 2020

# exceptional handling
# keywords are try,except,finally
# you can control some program when error occur by exceptional handling
# profesionaly use

# try:
#     print(x)
# except:
#     print("Except has printed")

# print(x)  #name error occur

# try:
#     print(x)
# except NameError: #if name error occur this except run
#     print("The Variable x is not defined")
# except: #if any other error occur this except run
#     print("Something went Wrong")

# x=3
# try:
#     print(x*4)
# except:
#     print("something wrong")
# else:
#     print("nothing went wrong")



# try:
#     print(x*4)
# except:
#     print("something wrong")
# finally: #error occur or not finally must be run in any case
#     print("I dont know about  error")

# a=int(input("enter any number"))
# i=1
# while(i<=10):
#     res = a*i
#     txt = "{0} * {1} = {2}"
#     print(txt.format(a,i,res))
#     # print("{} * {} = {}".format(a,i,res))
#     i+=1

# x= int(input("enter your Roll #"))
# if x<0:
#     raise Exception("Enter your Correct Roll No:")

# x= input("enter your Roll # : ")

# if type(x) is int:
#     raise TypeError("Type in String format")


# x= int(input("enter your Roll # : "))

# if type(x) is int:
#     raise TypeError("Type in String format")

# x= int(input("enter your Roll # : "))

# if  not type(x) is int:
#     raise TypeError("Type in String format")



# x = open("a.txt")
# print(x.read())

# keys "r"=read,"a"=append,"w"=write,"t"=text,"b"=binary

# x = open("a.txt","r")
# print(x.read(8))

# x = open("a.txt","r")
# print(x.readline())
# print(x.readline())
# print(x.readline())

# x = open("a.txt","a")
# x.write("this text is wrritten  in Visual studio code")
# x.close()
# x = open("a.txt","r")
# print(x.read())


# z = open("newfile.txt","w")
# z.write("this is new file")
# z.close


# z = open(r"C:\Users\IT\Desktop\ali Object\newfile.txt","r")
# print(z.read())
# z.close

            # practice

# a=int(input("enter any number"))          #backward counting
# i=1
# while(a>=i):
#     print(a)
#     a-=1



# a=int(input("enter any number"))    #backward counting using forloop
# i =1
# for x in range(i,a+1):
#     print(a)
#     a-=1