#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv('mtcars.csv')

df


# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import math
import plotly.express as px
import pandas as pd
import seaborn as sns
import random as rand


# In[2]:


x=np.arange(0,math.pi*2,0.05)
x


# In[3]:


y=np.sin(x)


# In[4]:


plt.plot(x,y)
plt.title("SIne wave")
plt.xlabel("angle")
plt.ylabel("Sine")
plt.show()


# In[5]:


x=[1,2,3,4,5]
y=[1,2,3,4,5]
fig=px.line(x=x,y=y,title="A simple line graph")
fig.show()


# In[6]:


cars=['AUDI','BMW','FORD','JAGUAR','TESLA','MERCEDES']
data=[23,17,35,29,12,41]
fig=plt.figure(figsize=(10,7))
plt.pie(data,labels=cars)
plt.title("Cars")
plt.show()


# In[7]:


pd.Series([65,61,25,22,27]).plot(kind="bar")


# In[8]:


plotdata=pd.DataFrame({'pies':[10,10,42,17,37]},index=["Dad","MOM","bro","Sis","Me"])
plotdata.plot(kind="barh")


# In[9]:


plotdata=pd.DataFrame({'pies':[10,10,42,17,37]},index=["Dad","MOM","bro","Sis","Me"])
plotdata.plot(kind="bar")


# In[10]:


plotdata.plot(kind="bar",stacked=True)


# In[11]:


df=sns.load_dataset('tips')
sns.barplot(x='time',y='total_bill',data=df)
plt.show()


# In[12]:


a= rand.sample(range(10,210),50)
b=rand.sample(range(30,500),50)
plt.scatter(a,b)


# In[13]:


a=np.linspace(0,10,100)
b=np.exp(-a)
plt.plot(a,b)
plt.show()


# In[14]:


x=rand.sample(range(2,67),10)
plt.boxplot(x,vert=True)
plt.show()


# In[ ]:




