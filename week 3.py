#!/usr/bin/env python
# coding: utf-8

# In[32]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


data = pd.read_csv("mtcars.csv")
data1 = pd.read_csv("cereals.csv")


# In[34]:


data


# In[35]:


data1


# # Q1 Draw the graphs in week 2 for mtcars and cereals

# In[36]:


sns.histplot(data['hp'])
plt.show()


# In[37]:


plt.boxplot(data['mpg'])
plt.show()


# In[38]:


sns.boxplot(x=data['am'],y=data['mpg'],data=data)
plt.xticks([0,1],["manual","automatic"])
plt.show()


# In[39]:


sns.boxplot(x=data1['type'],y=data1['calories'],data = data1)
plt.show()


# # Q2 Create 20 random numbers and create respective graphs

# In[40]:


import random as r
l1 = []
for a in range(20):
    l1.append(r.randint(1,100))


# # a) line plot

# In[41]:


plt.plot(l1)
plt.show()


# In[42]:


sns.histplot(l1)
plt.show()


# # bar plot

# In[43]:


l2 = []
for x in range(20):
    l2.append(x)
sns.barplot(x= l2,y=l1)
plt.show()


# # side by side graph

# In[44]:


a = pd.DataFrame({"1":l1,"2":l2})
a.plot(kind='bar')
plt.show()


# # stacked graph

# In[45]:


b = pd.DataFrame({"1":l1,"2":l2})
b.plot(kind='bar',stacked=True)
plt.show()


# # sin graph

# In[46]:


import math
x = np.arange(0,math.pi*2,0.05)
y = np.sin(x)
plt.plot(x,y)
plt.show()


# # 3D scatter plot using seaborn and matplotlib

# In[47]:


fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(projection='3d')
sns.set_style("whitegrid")
ax.scatter(l1,l2)
ax.set_xlabel("X AXIS")
ax.set_ylabel("Y AXIS")
ax.set_zlabel("Z AXIS")
plt.show()


# # surface plot

# In[48]:


l1 = []
l2 = []
l1.append(np.arange(-1,1,0.02))
l2.append(np.arange(-1,1,0.02))
l1,l2 = np.meshgrid(l1,l2)
l3 = l1**2+l2**2
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='3d')
ax.set_xlabel("X AXIS")
ax.set_ylabel("Y AXIS")
ax.set_zlabel("Z AXIS")
ax.plot_surface(l1,l2,l3)
plt.show()


# # violinplot

# In[49]:


l1 = []
l2 = []
for x in range(20):
    l1.append(r.randint(50,100))
    l2.append(r.randint(1,50))
a = {"col1":l1,"col2":l2}
b = pd.DataFrame(a)
sns.violinplot(x='col1',data=b)
plt.show()


# In[50]:


plt.violinplot(l1)
plt.show()


# # pie plot

# In[51]:


plt.pie(l1)
plt.show()


# # Q3 draw the 5 number summary for the numerical columns in the iris dataset with boxplots

# In[52]:


df = pd.read_csv("IRIS.csv")
df


# In[53]:


plt.boxplot(df.iloc[:,:4])
plt.xticks([1,2,3,4],["sepal-length","sepal-width","petal-length","petal-width"])
plt.show()


# # Q4 create a dataset for 5 subjects for 5 programs each for a minimum of 10 students and draw suitable graphs

# In[54]:


programs=['CSE','ECE','EEE','ICT']
df={'program':[],'Student ID':[],'Subject 1':[],'Subject 2':[],'Subject 3':[],'Subject 4':[],'Subject 5':[]}


# In[55]:


import random
for program in programs:
    for i in range(1,11):
        df['program'].append(program)
        df['Student ID'].append(i)
        df['Subject 1'].append(random.randint(50,100))
        df['Subject 2'].append(random.randint(50,100))
        df['Subject 3'].append(random.randint(50,100))
        df['Subject 4'].append(random.randint(50,100))
        df['Subject 5'].append(random.randint(50,100))  


# In[56]:


fd=pd.DataFrame(df)


# In[57]:


fd


# In[58]:


means=fd.groupby(['program']).mean()


# In[59]:


means.plot(kind='bar')


# In[ ]:





# # Q5 Create a matrix using numpy and perform transpose multiplication and inverse of the matrix

# In[61]:


r = int(input("Enter number of rows"))
c = int(input("Enter number of columns"))
l1 = []
i = 0
while(i<r*c):
    l1.append(int(input()))
    i=i+1
arr = np.array([l1])
arr1 = np.matrix(arr.reshape(r,c))
arr1


# In[62]:


np.transpose(arr1)


# In[63]:


np.linalg.inv(arr1)


# In[64]:


arr2 = [[1,2],[3,4]]
res = np.dot(arr1,arr2)
res


# In[ ]:




