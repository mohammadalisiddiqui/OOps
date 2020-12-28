# class player:
#     def __init__ (self, name, age, mode):
#         self.name = name
#         self.age = age
#         self.mode = mode
#     def myfun(self):
#         print("player is running")
#         print("Player name is "+self.name)
#         print("Player age is {} Years old".format(self.age))
#         print("Player playing in {} Mode".format(self.mode))
# p1 = player("ali",30,"easy")
# p1.myfun()

# class vehicle:
#     def __init__(self,name,model,No_Wheels):
#         self.name = name
#         self.model = model
#         self.No_Wheels = No_Wheels
#     def myfun(self):
#         print("Vehicle name is {} model is {} and have {} Wheels".format(self.name,self.model,self.No_Wheels)) 

# class car(vehicle):
#     def __init__(self,name,model,No_Wheels):
#         super().__init__(name,model,No_Wheels)
#     def carfun(self):
#         super().myfun()

# class motorBike(vehicle):
#     def __init__(self,name,model,No_Wheels):
#         super().__init__(name,model,No_Wheels)  
#     def motorfun(self):
#         super().myfun()    

# car1 = car("Toyota","2010","4")
# car1.carfun()

# bike = motorBike("Uniquie","2020","2")
# bike.motorfun()


                    # Encapsulation

# class computer:
#     def __init__(self):
#         self.__maxprice = 900  #double underscore show protection or private hogaya

#     def sell(self):
#         print("selling Price: {}".format(self.__maxprice)) 
#     def setMaxPrice(self,price):
#         self.__maxprice = price    

# c = computer()
# c.sell()
# c. __maxprice = 1000
# c.sell()
# c.setMaxPrice(1000)
# c.sell()

#  using encapsulation


class vehicle:
    def __init__(self,name,model,No_Wheels):
        self.name = name
        self.model = model
        self.__No_Wheels = 4
    def myfun(self):
        print("Vehicle name is {} model is {} and have {} Wheels".format(self.name,self.model,self.__No_Wheels)) 

class car(vehicle):
    def __init__(self,name,model,No_Wheels):
        super().__init__(name,model,No_Wheels)
    def carfun(self):
        super().myfun()

class motorBike(vehicle):
    def __init__(self,name,model,No_Wheels):
        super().__init__(name,model,No_Wheels)  
    def motorfun(self):
        super().myfun()    

car1 = car("Toyota","2010","8")
car1.carfun()

bike = motorBike("Uniquie","2020","2")
bike.motorfun()