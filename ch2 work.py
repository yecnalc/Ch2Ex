#!/usr/bin/env python
# coding: utf-8

# # Chapter 2 Exercises

# ## Algorithim Workbench - Number 12
# 
# Predicting the output of a print function

# In[1]:


print('George','John','Paul','Ringo',sep='@')


# This is my prediction for the print function above:
# "George@John@Paul@Ringo"

# # Programming Exercises - Number 1
# Displaying personal (fake) information using the "print" function

# In[4]:


print('Name: John Doe')


# In[5]:


print('Address: 1234 Spartan Ave','East Lansing','MI','48823')


# In[6]:


print('Phone Number: 678-999-8212')


# In[7]:


print('College Major: Theater')


# # "Planting Grapevines"
# Write a program that can calculate how many grapevines to plant in a row

# V = Number of grapevines that will fit in a row
# R = Length of the row in feet
# E = Amount of space in feet
# S = Space between vines in feet

# In[30]:


R = float(input('Enter the length of the row in feet:'))
E = float(input('Enter the amount of space used by and end-post assembly:'))
S = float(input('Enter amount of space between vines:'))


# In[31]:


V=(R-(2*E))/S


# In[32]:


print('Number of grape vines that will fit in a row = ',V)


# In[ ]:




