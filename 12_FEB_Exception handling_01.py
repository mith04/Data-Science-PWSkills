#!/usr/bin/env python
# coding: utf-8

# # What isan Exception in python? Write the difference between Exceptions and syntax errors?

# Ans :An exception is an event that disrupts the normal flow of a program during execution. When a statement or expression in a Python program encounters an error, it raises an exception, which can be caught and handled by the program to prevent it from crashing. Exceptions allow for graceful error handling, making Python code more robust and reliable.
# 
#  differences between exceptions and syntax errors in Python:
#  
#  
#  1.Exceptions occur during the execution of a program when an error is encountered.
# They are runtime errors and can be handled using try-except blocks to gracefully recover from the error and continue program execution.
# 
# ** Syntax error :
# 
# Syntax errors, also known as parsing errors, occur during the parsing of a Python script.
# They are caused by incorrect syntax in the code, such as missing parentheses, invalid keywords, or improper indentation.
# Syntax errors prevent the program from running at all and must be fixed before the program can be executed.
# 

# # 2.what happens when an exception is not handled? explain with example ?
# 
# 
# Ans :if the exception is not caught and handled anywhere along this path, the program will terminate abruptly, and an error message will be displayed to the user indicating the unhandled exception and its type.

# In[9]:


def divide_number(a,b):
    return a/b
result=  divide_number(10,0)
print('result',result )

## if will run this code will get exception

'''---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
Cell In[1], line 3
      1 def divide_number(a,b):
      2     return a/b
----> 3 result=  divide_number(10,0)
      4 print('result',result )

Cell In[1], line 2, in divide_number(a, b)
      1 def divide_number(a,b):
----> 2     return a/b

ZeroDivisionError: division by zero'''


# In[10]:


#we have to use Try and except block to handle exception 

try:
    # Code that may raise an exception
    result = 10 / 0  # Division by zero raises ZeroDivisionError
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero is not allowed!")


# # 3.which python statements are used to catch and handle exceptions? explain with example
# 
# Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.
# 
# 

# In[12]:


try:
    number = int(input("Enter a number: "))
    result = 10 / number  # Potential ZeroDivisionError or ValueError
    print("Result:", result)
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# # 4.explain with example 
# 
# a. try and else
# 
# b. finally
# 
# c.raise
# 
# TRY AND ELSE :
# 
# The else block in a try-except statement is executed only if no exception occurs in the try block. It's typically used to place code that should run when no exceptions are raised. Here's an example:

# In[15]:


try:
    # Code that may raise an exception
    result = 10 / 5  # Division by zero raises ZeroDivisionError
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero is not allowed!")
else:
    print("No Error thats why it's executed ")


# # Finally 
# 
# The finally block in Python is used to execute cleanup code, such as closing files or releasing resources, regardless of whether an exception was raised or not

# In[17]:


#Example :

try:
    # Code that may raise an exception
    result = 10 / 0  # Division by zero raises ZeroDivisionError
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero is not allowed!")
finally:
    print("Finally Block will be handled anyhow ")


# # Raise 
# 
# The raise statement in Python is used to raise an exception manually.
# 
# 

# In[20]:


def validate_age(age):
    if age < 0:
        raise ValueError("Age must be a non-negative integer.")
    return age

try:
    user_age = int(input("Enter your age: "))
    validated_age = validate_age(user_age)
    print(f"Your age is {validated_age}.")
except ValueError as e:
    print(f"Error: {e}")


# # what are the custome  exceptions in python? why do we need custom exception? explain with example

# 
# Custom exceptions in Python are user-defined exception classes that inherit from the base Exception class or its subclasses. They are created to handle specific error conditions or situations that are not covered by the built-in exceptions provided by Python.
# 
# 
# And 
# 
# we need this because it Make our  code much more readable and robust, and reduce the amount of code you write later to try and figure out what exactly went wrong.
# 

# In[1]:


class InvalidInputError(Exception):
    """Custom exception for handling invalid input."""
    def __init__(self, input_value):
        super().__init__(f"Invalid input value: {input_value}")
        self.input_value = input_value

def process_input(input_value):
    if not isinstance(input_value, int):
        raise InvalidInputError(input_value)
    # Process the input

try:
    user_input = 'abc'
    process_input(user_input)
except InvalidInputError as e:
    print(f"Error: {e}")
    print("Please provide a valid integer input.")


# # create a Custom exception class .use this class to handle an exception
# 

# In[10]:


class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def divide(a, b):
    if b == 0:
        raise CustomException("Division by zero is not allowed.")
    return a / b

try:
    result = divide(10, 0)
except CustomException as e:
    print("Error:", e.message)
else:
    print("Result of division:", result)


# In[ ]:




