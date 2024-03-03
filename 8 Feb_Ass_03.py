#!/usr/bin/env python
# coding: utf-8

# # Q1. What is Abstraction in OOps? Explain with an example.

# # Ans:
# Data abstraction is one of the most essential concepts  which is used to hide irrelevant details from the user and show the details that are relevant to the users.
# 
# # Code:
# 

# In[12]:


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius**2
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):
        return self.length *self.width
    
#creating object 
circle=Circle(5)
rectangle=Rectangle(25,22)

#printing 
print(circle.area()) 
print(rectangle.area()) 


# #In this example, the Shape class is an abstract class that defines an abstract method area. The Circle and Rectangle classes are subclasses of Shape that provide concrete implementations for the area method. When the area method is called on instances of the Circle and Rectangle classes, the subclass's method is executed, which calculates the area of the circle and rectangle, respectively.

# # Q2. Differentiate between Abstraction and Encapsulation. Explain with an example.
# 

# Abstraction is a process of hiding the implementation details of a system from the user, and only the functional details will be available to the user end. On the other hand, Encapsulation is a method of wrapping up the data and code acting on the data into a single unit.
# 
# # code :Abstraction

# In[14]:


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating instances of the subclasses
dog = Dog()
cat = Cat()

# Calling the speak method on the instances
dog.speak() # Output: Dog barks
cat.speak() # Output: Cat meows


# In[16]:


# encapsulation
class Car:
    def __init__(self, make, model):
        self._make = make  # Protected attribute
        self.__model = model  # Private attribute

    def get_make(self):
        return self._make

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

# Creating an instance of the Car class
car = Car("Toyota", "Corolla")

# Accessing the protected attribute
print(car.get_make())  # Output: Toyota

# Accessing the private attribute (will raise an AttributeError)
# print(car.__model)  # AttributeError: 'Car' object has no attribute '__model'

# Accessing the private attribute using a getter method
print(car.get_model())  # Output: Corolla

# Setting the private attribute using a setter method
car.set_model("Camry")
print(car.get_model())  # Output: Camry


# # Q3. What is abc module in python? Why is it used?
# 
# The abc module in Python stands for Abstract Base Classes. It provides the infrastructure for defining abstract base classes (ABCs). An abstract base class is a class that cannot be instantiated on its own and is meant to be subclassed. It may contain one or more abstract methods, which are methods that are declared but not implemented in the abstract class. Subclasses of an abstract class must provide concrete implementations for all the abstract methods.
# 
# The abc module is used to enforce the concept of abstract classes and abstract methods in Python. It helps ensure that subclasses of abstract classes provide concrete implementations for all the abstract methods, which can be useful for creating well-structured and maintainable code. It also provides tools for working with abstract base classes, such as the abstractmethod decorator and the ABC class.

# # Q4. How can we achieve data abstraction?
# 
# In Python, we can achieve data abstraction by using abstract classes and abstract classes can be created using abc (abstract base class) module and abstractmethod of abc module.

# # Q5. Can we create an instance of an abstract class? Explain your answer.
# 
# # no we can't create an instance of a abstract class .here is the example :
# 
# from abc import ABC, abstractmethod
# 
# class Animal(ABC):
# 
#     @abstractmethod
#     def speak(self):
#         pass
# 
# #This will raise a TypeError because Animal is an abstract class
# 
# animal = Animal()
# 
# 
# In this example, the Animal class is an abstract class that defines an abstract method speak using the @abstractmethod decorator. When you try to create an instance of the Animal class, Python raises a TypeError because the class is not fully defined.
# 
# Instead, you should create subclasses of the Animal class that provide concrete implementations for the speak method. Instances of these subclasses can then be created and used.
# 
# # Code below using Subclass
# 

# In[18]:


class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating instances of the subclasses
dog = Dog()
cat = Cat()

# Calling the speak method on the instances
dog.speak() # Output: Dog barks
cat.speak() # Output: Cat meows


# In[ ]:




