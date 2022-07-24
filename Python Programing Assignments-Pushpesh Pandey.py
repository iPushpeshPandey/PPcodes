#!/usr/bin/env python
# coding: utf-8

# ### Assignment -1 Programming
# 

# Q-1-Printing 'Hello Python'

# In[1]:


print("Hello Python")

Q-2-Arithmetic operation addition and division
# In[16]:


a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
sum=a+b
print("The required sum of the numbers is : ", sum)

div=a/b
print("The required division of the numbers is : " ,div)


# Q-3 Area of a triangle

# In[54]:


a=float(input("Enter the first side of the triangle "))
b=float(input("Enter the second side of the triangle "))
c=float(input("Enter the third side of the triangle "))
s=(a+b+c)/2
print(s)
area=((s*(s-a)*(s-c)*(s-b)))**(1/2)
print("The required area of the triangle is given as : " , area)


# Q-4- Swapping of two variables

# In[62]:


n=str(input("Enter the first variable "))
m=str(input("Enter the second variable "))
s=" "
s=n
n=m
m=s
print("The swapped numbers are as follows : ", " n = ",n , " m = ", m)


# Q-5-Generate any random number

# In[59]:


n=int(input("Enter any number that you wanted to get printed "))
print(n)


# In[ ]:




