#!/usr/bin/env python
# coding: utf-8

# # Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.
# 

# Class is a user defined blueprint or Prototype from which objects are created . Classes provides means of bundling data and Functionality Together.
# creating a new class, creates new types of objects and the Objects access all the data and Functions which are defined in The class. 
# 
# Objects: Object is an instance of a class. which are use to access the data from the Class . 
# 
# Let's see examples:
# 

# In[10]:


#defining class
class Bike:
 
    #  variables defined 
    name=" "
    gear =0
    
    # creating Object of class
    
bike=Bike()
    
    # accessing the variables using object
bike.gear=5
bike.name='Royal Enfield'
    
print(f"Name:{bike.name},Gears:{bike.gear}")
    
    
    


# # Q2. Name the four pillars of OOPs.
# 

# The Four pillar of oops are :
# 1. Polymorphism
# 2. Inheritance
# 3. Encapsulation
# 4. Abstraction

# # Q3. Explain why the __init__() function is used. Give a suitable example.
# 

# __init__  it is a default constructor . constructor are used to  Inticalise the object's state.  It is used to intialise (assign Value) to the data members of the class when an object is created.
# constructions contains collections of statement (instructions ) which are execute when the class's object is created . 
# it run at the time of object creation  
# 
# Let's see example:
# 
# 

# In[11]:


class greeting:
    def __init__(self,name):
        self.name=name
    
    def method_greeting(self):
        print('Hello , My name is Mith. welcome to My Villa', self.name)

# creating object
G=greeting('Stranger')
G.method_greeting()


# # Q4. Why self is used in OOPs?
# 

# Self represents the instance of  the class.  By using 'self' we  can acess the attribute and methods of the class In python . It binds the Attributes with the Given Arguments . 

# # Q5. What is inheritance? Give an example for each type of inheritance.
# 

# Inheritance is defined as the mechanism of inheriting the properties of the base class to the child class
# types of inheritance :
# 1. Single inhertiance
# 2. Multiple inhertiance
# 3. MultiLevel inhertiance
# 4. Hierarchical inhertiance
# 5. Hybrid inhertiance
# 
# Let's see Examples of each 

# # 1. Single inhertiance
# 

# In[13]:


class parent():
    def func1(self):
        print(" I am The Parent class")

class Child(parent):
    def func2(self):
        print(" I am child")
        
# creating object of Child Class to access parent class

c=Child()
c.func1()
c.func2()


# # 2. Multiple inhertiance
# 

# In[15]:


class mother:
    def func1(self):
        print('mother')
class father:
    def func2(self):
        print('father')
        
class Child(mother, father):
    def func3(self):
        print('Child')
        
# Object creating for Child but it will acess mother and father properties

c=Child()
c.func1()
c.func2()
c.func3()


# # 3. MultiLevel inhertiance
# 

# In[16]:


class Grandparent:
    def func1(self):
        print('GrandParent')
        
class parent(Grandparent):
    def func2(self):
        print('Child1')
        
class child(parent):
    def func3(self):
        print('Child')
        
c=child()
c.func1()
c.func2()


# # 4. Hierarchical inhertiance
# 

# In[20]:


# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class1


class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

# Derivied class2


class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# # 5. Hybrid inhertiance
# 

# In[21]:


class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):
	def func3(self):
		print("This function is in student 2.")


class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")


object = Student3()
object.func1()
object.func2()


# In[ ]:




