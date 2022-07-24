#!/usr/bin/env python
# coding: utf-8

# # Assignment -3 python programming.

# Q-1 Check if a Number is Positive, Negative or Zero

# In[5]:


n=float(input("Enter the number : "))
if(n>0):
    print("The number is positive ")
elif(n<0):
    print("The number is negative")
else:
    print("The number is 0")


# Q-2 Check if a Number is Odd or Even.
# 

# In[15]:


n=int(input("Enter the number : "))
if(n%2==1):
    print("The number entered is odd")
else:
    print("The given number is even ")
    


# Q-3 Check Leap Year

# In[39]:


n=int(input("Enter the year "))
if(n%400==0):
    print("The given year is century year and its a leap year ")
elif(n%100==0):
    print("The given year is not a leap year.")
    
elif(n%4==0):
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")


# Q-4 Check Prime Number

# In[23]:


c=0
n=int(input("Enter the number "))
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
if(c>=3):
    print("The given number is not a prime number ")
else:
    print("The given number is prime  ")


# Q-5 Finding prime numbers from 1 to 1000

# In[66]:


for i in range(1,10001):
    if i>1:
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print(i)


# In[ ]:




