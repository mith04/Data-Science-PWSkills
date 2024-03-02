#!/usr/bin/env python
# coding: utf-8

# # 1. Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed and average_of_vehicle.

# In[1]:


class vehicle:
    def __init__(self,name_of_vehicle,max_speed,average_of_speed):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed=max_speed
        self.average_of_speed=average_of_speed
        


# # Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.Create a method named seating_capacity which takes capacity as an argument and returns the name of the vehicle and its seating capacity.

# In[2]:


class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_speed):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_speed = average_of_speed
        
class Car(Vehicle):
    def __init__(self, name_of_vehicle, max_speed, average_of_speed):
        super().__init__(name_of_vehicle, max_speed, average_of_speed)
    
    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} passengers."

car = Car("Tata", 200, 50)
print(car.seating_capacity(4))


# # Q3.What is multiple inheritance? Write a python code to demonstrate multiple inheritance.

# # Ans: Multiple Inheritance  :- 
# 
# When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.
# 
# # Below is the code 

# In[3]:


class Class1:
    def m1(self) :
        print("Class 1")
class Class2(Class1):
    def m1(self):
        print("Class 2")

class Class3(Class1):
    def m1(self):
        print("Class 3")
        
class Class4(Class2,Class3):
      def m1(self):
        print("Class 4")
        
obj=Class4()
obj.m1()
obj2=Class2()
obj2.m1()


# # Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this class

# Getters: These are the methods used in Object-Oriented Programming (OOPS) which helps to access the private attributes from a class.
# 
# Setters: These are the methods used in OOPS feature which helps to set the value to private attributes in a class.

# In[4]:


# Code 
class Person :
    def __init__(self,name, age):
        self.name=name
        self.age=age
        
    # getter to get name
    def get_name(self):
        return self.name
    
    #setter
    def set_name(self,name):
        self.name=name
        
    #getter for age
    def get_age(self):
        return self.age
    
    #setter for age
    def set_age(self,age):
        self.age=age

#create an instance of the person Class
person =Person("John",30)

#printing the name
print(person.get_name())

#setting name
person.set_name("Rock")

#gettting name again 
print(person.get_name())

print(person.get_age())
person.set_age(40)

#getting age again 
print(person.get_age())



# # Q5.What is method overriding in python? Write a python code to demonstrate method overriding.
# 

#  Method overriding is a feature in object-oriented programming that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This means that when a method is called on an object of the subclass, the subclass's method will be executed instead of the superclass's method.
#  
#  # code :

# In[6]:


class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog Bark")
class Cat(Animal):
    def speak(self):
        print("Cat Meow")
        
#creating object
dog= Dog()
cat=Cat()
dog.speak()
cat.speak()


# In[ ]:




