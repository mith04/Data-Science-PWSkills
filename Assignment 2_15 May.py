#!/usr/bin/env python
# coding: utf-8

# # Q1. How do you comment code in Python? What are the different types of comments?
# 

# Ans : Comments in python are the lines that are ignored by the Interpreter during the execution of Progam
# This make code more readable and Helps the Coder to understands the code very Carefully or easily .
# using comments , you can define any Notes Or explain what a particluar line is going to Perform. 
# 
# **** There are  types of comments we use In python *** 
# 1. single line comments 
# 2. Multiple line comments
# 3. Docstring Comments
# 
# 1. single line comments  : Single line comments begins with  '#' Or '##' symbol. we can mention our comments Lines after single '#'
# 
# 2. Multiple line comments : Python Doesn't Support multiple lines but we can do it multiples ways . 
# like : if you multiple lines to comment than you can use '#' for each line at start 
# Or you can also String literals '' for each lines without assigning it to any variables. 
# if we will NOT assign any Variable to String Literals that it will be ignored  by the python interpreters
# 
# 3. Docstring Comments : we can use single or Double Quotes 3 times to make It Comment.
# Example: Single Quotes : '''  '''
#          Double Quotes : """  """
#          
#          Within this Quotes  we can mention multiple lines
#          

# # Q2. What are variables in Python? How do you declare and assign values to variables?
# 

# in python  , Variables is a named Storage location that holds value. we don't need to declare them before Using them Or their data types . 
# A variable is created the Moment we first assign the value. 
# python variable is the name given to the memory location
# 
# For Example  :
# mith = 100
# 
# Here mith is a Variable name and we have assigned 100 as  value  to it. 
# Like wise you can create any variable and store any type of data Like string , int , float , boolean etc . 
# 

# # Q3. How do you convert one data type to another in Python?
# 

# Yes , In python we can convert one data type to another And this concept is known as TypeCasting . 
# Let's take example : 
# 
# s =10           # this is int But If we want to convert in float
# s=float(10)
# 
# another ex: 
# A='565'  , here we have assigned 565 as String but we want to convert in to INT
# 
# A=int('565)
#  
# Another ex:
# Whenever we take input from the User it returns String type . here we can use Typecasting
# 
# B = input('Enter the number:') --> This will always return String , But if it will return  Str we can't perform Arthimetical operations . 
# 
# So, here we will do typecasting
# 
# B=int(input('Enter the number :')
# 

# # Q4. How do you write and execute a Python script from the command line?
# 

# Here are the steps to Write and Execute The phython Script from Command line
# 1. open Command line 
# 2. Select Dictory (like cd Documents)
# 3. create python file with extension .py
# like : test.py 
# 
# 4. than here write the code and save it using CTRL+S Or from File option 
# 
# than again goto command line
# TO RUN IT 
# 
# Write : python test.py
# 
# this will execute the code that you have written in test.py 
# 
# OR 
# there is a another way : 
# 1. goto Command line 
# 2. Type python , start typing code here
# like : >>> a=10
# >>> b=20
# >>> if b>a:
# ...     print('B is greater than A')
# ... else:
# ...     print (' A is greater than B')
# 
# B is greater than A
# >>>

# # Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].
# 

# In[1]:


my_list=[1,2,3,4,5]
my_list[1:3]


# # Q6. What is a complex number in mathematics, and how is it represented in Python?
# 

#  complex number in mathematics is written in  the Form of A+Bi 
#  Where as A and B are the real number and I is the imaginary number called 'Iota'. 
#  
#  Example : 5 +6i ==> 5 is The real number and 6i is the imaginary number
#  
#  # in python 
#  
#  we use a+bj ==> we use j as imaginary instead of i . only j will be accepted as imaginary no other character wil be accepted . 
#  
#  Example = 4+5j 
#  

# # Q7. What is the correct way to declare a variable named age and assign the value 25 to it?
# 

# age =25 # we have assigned 25 in the variable age 

# # Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to ?
# 

# In[4]:


price =9.99
type(price )


# So the data type of the variable is Float .

# # Q9. Create a variable named name and assign your full name to it as a string. How would you print the value of this variable

# In[1]:


name='Mithilesh Yadav'
print(name)


# # Q10. Given the string "Hello, World!", extract the substring "World".
# 

# In[6]:


S='Hello, World!'
S[7:12:1]


# # Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not

# In[12]:


is_student =True 
if is_student == True :
    print('yes i am Student')
else:
    print('No , i am not Student')


# In[ ]:




