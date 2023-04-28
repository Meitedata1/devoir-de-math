#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import math
import numpy
import time


# # Exercice 1

# In[2]:


def draw_my_fonction(f, start, end, number_of_points):
    x_values = numpy.linspace(start, end, number_of_points)
    y_values = f(x_values)
    
    numpy.gradient(y_values, x_values) 
    
    plt.figure(figsize=(15, 6))
    plt.plot(x_values, y_values)
    plt.show()


# # definition des poaramètres de mon scripts

# In[3]:


start = 0
end = 10
number_of_points = 10000

f = lambda x_values : numpy.exp(-x_values/10) * numpy.sin(x_values)


# In[4]:


draw_my_fonction(f, start, end, number_of_points)


# # Exercice 2

# In[5]:


def draw_my_fonction2(f, start, end, number_of_points):
       x_values = numpy.linspace(start, end, number_of_points)
       y_values = f(x_values)
       
       df_dx = numpy.gradient(y_values, x_values)
       
       plt.figure(figsize=(15, 6))
       plt.plot(x_values, y_values)
       plt.plot(x_values, df_dx)
       plt.show()


# # defintion des paramètres

# In[6]:


start2 = 0
end2 = 10
number_of_points2 = 10000
f2 = lambda x_values : numpy.exp(-x_values/10) * numpy.sin(x_values)


# In[7]:


draw_my_fonction2(f2, start2, end2, number_of_points2)


# # exercice 3

# In[8]:


x_values = numpy.linspace(3, 7, number_of_points)
numpy.mean(f(x_values))
y_values = f(x_values)
numpy.mean(f(y_values))


# In[9]:


x_values = numpy.linspace(3, 7, number_of_points)
numpy.std (f(x_values))
y_values = f(x_values)
numpy.std(f(x_values))
numpy.std(f(y_values))


# # exercice 4

# In[ ]:





# # exercice 5

# In[243]:


def monte_carlo(f, start, end, number_of_points):
    total = 0
    for i in range (number_of_points):
        x = random.uniform(start, end)
        total += f(x)
    return (end - start) * total/number_of_points


# In[244]:


start = 0
end = 10
number_of_points = 10000

f = lambda x_values : math.exp(-x_values/10) * math.sin(y_values)


# In[245]:


monte_carlo(f, start, end, number_of_points)


# # correction exo 3

# In[ ]:




