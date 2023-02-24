#!/usr/bin/env python
# coding: utf-8

# In[5]:


def even(a):
    if(a%2==0):
        print('even')
    else:
        print('odd')
        
even(1)
   


# In[11]:


def sum():
    a = int(input('enter the 1st number: '))
    b = int(input('enter 2nd number: '))
    
    c = a+b
    
    print(c)
    
sum()


# In[12]:


def num(*n) :
    for i in n:
        print(i)
        
num(1,2,3,4,34,53,5,45,67,46)


# In[13]:


def func3(x):
    return 5*x
print(func3(3))
print(func3(5))
print(func3(9))


# In[14]:


import pandas as pd
dict={
"country":["brazil","russia","india","china","south africa"],
"capital":["brasilia","moscow","new delhi","bejing","pretoria"],
"area":[8.56,17.10,3.268,7.24,1.221],
"population":[128.3,587,7643,2456,3564]    
}
brics=pd.DataFrame(dict)
print(brics)


# In[16]:


brics=pd.read_csv('cereal.csv')
brics


# In[17]:


brics.head(5)


# In[18]:


brics.tail(2)


# In[19]:


brics.shape


# In[20]:


brics['name']


# In[22]:


brics[{'name','type'}]


# In[23]:


brics.iloc[[1,2,3],[0,1]]


# In[24]:


brics.iloc[[2,3,4],[1,2,4]]


# In[26]:


brics[brics['name'] == 'Trix']


# In[6]:


brics=pd.read_csv('cereal.csv')
brics

import seaborn as sns

sns.boxplot(x=cr,'type',y=cr,'calories')


# In[ ]:




