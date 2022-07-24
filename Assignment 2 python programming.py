#!/usr/bin/env python
# coding: utf-8

# ### Assignment -2 Python programming

# Q-1 Conversion to kilometer to miles
# 

# In[4]:


n=float(input("Enter the number that you wnated to change into miles : "))
"1 km =  0.621371 miles"
s=n* 0.621371 
print("The distance in miles is ", s ," miles")


# Q-2- convert Celsius to Fahrenheit

# In[5]:


c=float(input("Enter the temperature in celsius " ))
f=(1.8*c)+32
print("The temperature in fahrenheit is given as : ", f)


# Q-3- Display Calender

# In[15]:


import calendar


# In[16]:


yy=int(input("Enter the year "))
mm=int(input("Enter the month "))
print(calendar.month(yy,mm))


# Q-4- Sloving quadratic equation

# In[11]:


a=float(input("Enter the value of the coefficient of x^2 "))
b=float(input("ENter the value of the coefficent of x "))
c=float(input("Enter the value of the constant "))
d=(b**2-(4*a*c))**(1/2)
x_1=(-b+d)/(2*a)
x_2=(-b-d)/(2*a)
print("The solutions of the given qquadratic equations is given as : " ,x_1 , x_2)


# Q-5-swap two variables without temp variable

# In[13]:


a=int(input("Enter the first variable "))
b=int(input("Enter the second variable "))
a=a+b
b=a-b
a=a-b
print("The values are now swapped "," a =", a , "b =" , b )


# In[ ]:




