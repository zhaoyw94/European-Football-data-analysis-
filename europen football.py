#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')

# we will use this dataset.
# source: https://www.kaggle.com/hugomathien/soccer

def get_data():
    cnx = sqlite3.connect('/Users/yiwenzhao/Desktop/Edx 1 Python for DS/Week-5-Exercises-2/database.sqlite')
    df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)
    return df

df = get_data()


# In[11]:



# Let's see what is in our dataset
df.describe()


# In[19]:




def line_plot(df, x, y):

    df.sort_values(by = x, inplace = True)
    plt.plot(df[x][:50].values, df[y][:50].values)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title("Line Plot of %s and %s" % (y, x))
    
    plt.show()
 


# In[20]:




line_plot(df, 'potential', 'overall_rating')


# In[44]:




def plot_histogram(df, X):
   
    hist_data = df.dropna()[X].values
    plt.hist(hist_data, 10, 
            normed=False, facecolor = 'green')
    
    plt.xlabel(X)
    plt.ylabel('# numbers of players')
    plt.title('histogram of %s' % X)
    
    plt.grid(True)
   


# In[45]:


plot_histogram(df, 'penalties')


# In[53]:


# modify this cell

def plot_scatter(df, x, y):
    ### BEGIN SOLUTION
    ### BEGIN SOLUTION
    fig, axis = plt.subplots()
    # Grid lines, Xticks, Xlabel, Ylabel

    axis.yaxis.grid(True)
    axis.set_title('Scatter Plot between %s and %s' % (x, y) ,fontsize=10)
    axis.set_xlabel(x,fontsize=10)
    axis.set_ylabel(y,fontsize=10)

    hori = df[x]
    vert = df[y]

    axis.scatter(hori, vert)
    plt.show()
    ### END SOLUTION
    
    
    
    
    ### END SOLUTION


# In[54]:



plot_scatter(df, 'gk_diving', 'gk_handling')

