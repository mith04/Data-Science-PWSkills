#!/usr/bin/env python
# coding: utf-8

# # Q1. Explain why we have to use the Exception class while creating a Custom Exception.
# 
# Note: Here Exception class refers to the base class for all the exceptions

# The Exception class is the base class for all built-in exceptions. When creating a custom exception, it is recommended to inherit from the Exception class or one of its subclasses. 
# 
# Here's why using the Exception class is important when creating a custom exception in Python:
# 
# 1.Exception Hierarchy: Inheriting from the Exception class ensures that your custom exception becomes part of the standard exception hierarchy in Python. This hierarchy is crucial for organizing and handling different types of exceptions in a consistent and structured manner.
# 
# 2.Clarity and Readability: Inheriting from the Exception class makes your custom exception more understandable to other developers. When they encounter your custom exception in the code, they can immediately recognize it as an exceptional condition that needs to be handled differently from regular program flow.
# 
# 3.Compatibility: Many built-in features and libraries in programming languages are designed to work with exceptions derived from the Exception class. 
# 
# 4.Exception Handling: Custom exceptions often represent specific error conditions or exceptional situations within your application. By deriving from the Exception class, you can provide specialized handling for these situations, such as logging detailed error messages, rolling back transactions, or notifying users appropriately.
# 

# # 2. Write a python program to print Python Exception Hierarchy.
# 

# In[18]:


def exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Start printing the hierarchy from the base Exception class
exception_hierarchy(Exception)


# # Q3. What errors are defined in the ArithmeticError class? Explain any two with an example.
# 

# 
# The ArithmeticError class in Python is a base class for various arithmetic-related errors
# 
# Here are the 2 errors with example :
# 
# ZeroDivisionError:
# 
# This error occurs when attempting to divide a number by zero, which is mathematically undefined.
# 
# 
# 

# In[19]:


try:
    result = 10 / 0  # Attempting division by zero
except ZeroDivisionError as e:
    print(f"Error: {type(e).__name__} - {e}")


# 2.OverflowError:
# 
# This error occurs when the result of an arithmetic operation exceeds the maximum limit that can be represented by the data type.

# In[24]:


import math

try:
    result = math.exp(1000)  # Calculating exponential of a large number
except OverflowError as e:
    print(f"Error: {type(e).__name__} - {e}")


# # Q4. Why LookupError class is used? Explain with an example KeyError and IndexError.
# 
# 
# Ans : 
# The LookupError class in Python is used to handle errors related to lookup operations, such as indexing or key-based access, when the target value is not found. 
# 
# 
# 1. KeyError :KeyError is raised when trying to access a dictionary key that does not exist.
# 
# Lets see it's example :
# 

# In[32]:


my_dict = {'name': 'Alice', 'age': 30}

try:
    value = my_dict['email']  # Accessing a non-existent key
except KeyError as e:
    print(f"Error: {type(e).__name__} - {e}")


# Index Error :IndexError occurs when trying to access an index in a sequence (like a list or tuple) that is out of range.
# 

# In[34]:


my_list = [10, 20, 30]

try:
    value = my_list[3]  # Accessing an index out of range
except IndexError as e:
    print(f"Error: {type(e).__name__} - {e}")


# # Q5. Explain ImportError. What is ModuleNotFoundError?
# 
# 
# ImportError is an exception class in Python that is raised when an import statement fails to import a module or when an imported module fails to provide an attribute that is being accessed. It is a subclass of the Exception class and is commonly used in scenarios where there are issues with importing modules or using attributes from imported modules.
# 
# 
# ModuleNotFoundError:
# 
# ModuleNotFoundError is a more specific subclass of ImportError raised when the specified module cannot be found during import.
# 

# # Q6. List down some best practices for exception handling in python. 
# 1. Use Specific Exceptions
# 2. Implement Error Logging
# 3. Define Custom Exception Classes
# 
# 4. Handle Exceptions Gracefully
# 5. Use Finally for Cleanup Tasks
# 

# In[ ]:




