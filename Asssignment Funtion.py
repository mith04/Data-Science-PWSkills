#!/usr/bin/env python
# coding: utf-8

# # Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25

# In[1]:


'''We create Function using "def" keyword '''
l=[]
def test():

    for i  in range(25):
        if i%2!=0 :
            l.append(i)
    return l


# In[2]:


test()


# # Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use

# In[3]:


''' *args is used to enter Multiple/ulimited  values 
AND 
**kwargs is used to pass value in KEY:VALUE pair . we can pass dictionary value in it 

Let's see some example 
'''

def test1(*args):
    return args


# In[4]:


# Now call test1()
test1(10,20,55.69,78.15,'Mithilesh','Yadav',True,False)


# In[5]:


# Let's see **kwargs 
def test2(**kwargs):
    return kwargs


# In[6]:


type(test2()) ## this Shows type Of test Method is Dictionary . so we can pass value In Key and value pair 


# In[7]:


test2()


# In[8]:


test2(name='Mithilesh',address='noida',course='Data Science ')


# # Q3.  What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Ans:
#  An iterator is an object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets.Iterator which allows us to move from one value to another.
# We can move Next to Next to Fetch the value 

# __iter__ () is used to Initialise Iterator 
# and
# __next__() isu+ used to d

# In[9]:


class iterator_Test:
    def __init__(self,n):
        self.n=n
        self.index =0
        
    def __iter__(self):
        
        return self 
    def __next__(self):
        if self.index<5:
            result=self.n[self.index]
            self.index +=1
            return result
        else:
            raise StopIteration
L=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
A  = iterator_Test(L)
for i in A:
    print(i)


# # Q4.  What is a generator function in python? Why yield keyword is used? Give an example of a generator function

# Python provides a generator to create your own iterator function. A generator is a special type of function which does not return a single value, instead, it returns an iterator object with a sequence of values. 
# 
# it is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a Python generator function. 
# 
# ** TO MAKE GENERATOR FUNCTION WE HAVE TO USE YIELD KEYWORD OTHERWISE IT WILL BE CONSIDER AS NORMAL FUNCTION 

# In[10]:


def generator_func():
    my_list=[10,20,30,40,50,60]
    for i in my_list:
        yield i
gen=generator_func()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# # Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers

# In[11]:


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator():
    num = 2
    while num < 1000:
        if is_prime(num):
            yield num
        num += 1

# Use the generator to print the first 20 prime numbers
prime_gen = prime_generator()
for _ in range(20):
    prime = next(prime_gen)
    print(prime)


# # Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.
# 

# In[12]:


# Initialize the first two Fibonacci numbers
fibonacci_sequence = [0, 1]

# Use a while loop to generate the next 8 Fibonacci numbers
while len(fibonacci_sequence) < 10:
    next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_fib)

# Print the first 10 Fibonacci numbers
print(fibonacci_sequence)


# # Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']

# In[13]:


s='pwskills'
l=[]
for i in range(len(s)):
    l.append(s[i])
print(l)


# # Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.
# 

# In[19]:


number= int(input("Enter number"))
temp=number
reverse=0

while(number>0):
    dig =number%10
    reverse = reverse*10+dig
    number =number//10

if temp==reverse:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")


# # Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
# 

# In[21]:


odd_list=[]
for i in range(1,101):
    if i%2!=0:
        odd_list.append(i)
print(odd_list)


# In[ ]:




