#!/usr/bin/env python
# coding: utf-8

# # Q1. Create a python program to sort the given list of tuples based on integer value using a lambda function. [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# In[4]:


List=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_data=sorted(List,key=lambda x:x[1])

for item in sorted_data:
    print(item)


# # Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In[11]:


L=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(x):
    return x**2
list(map(square,L))


# In[12]:


# OR Another Way
list(map(lambda x:x**2,L))


# # Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions.Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] .Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

# In[13]:


Integers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
string_tuples=tuple(map(lambda x:str(x),Integers))
print(string_tuples)


# # Q4.  Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25

# In[17]:


from functools import reduce
numbers=list(range(1,26))
list_Products=reduce(lambda x,y:x*y,numbers)
print('The Product of the List is ', list_Products)


# # Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function.[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

# In[21]:


my_list=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
list(filter(lambda x:x%2==0 and x%3==0 , my_list))


# # Q6. Write a python program to find palindromes in the given list of strings using lambda and filter function.['python', 'php', 'aba', 'radar', 'level']

# In[26]:


S=['python', 'php', 'aba', 'radar', 'level']
is_palindromes=lambda s:s==s[::-1]
find_palindromes=list(filter(is_palindromes,S))
print('Palindromes are ',find_palindromes)


# In[ ]:




