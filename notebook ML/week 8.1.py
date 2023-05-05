#!/usr/bin/env python
# coding: utf-8

# 

# ### Write the python code to build the ensemble learning models on atleast 4 datasets (with and without using pipeline). Build the models with atleast 4 train_test_split combinations and different set of hyper-parameter values.  Peform the data pre-processing and performance evaluation for the models.

# In[76]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier,AdaBoostClassifier,VotingClassifier
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.svm import SVC
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn import metrics
df=pd.read_csv('mushrooms.csv')


# In[77]:


for label in df.columns:
    df[label]=LabelEncoder().fit(df[label]).transform(df[label])
df.info()


# In[78]:


df.describe()


# In[79]:


df.isna().sum()


# In[80]:


X=df.drop(['class'],axis=1)
Y=df['class']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)


# In[81]:


model=DecisionTreeClassifier(criterion='entropy',max_depth=1)
model=model.fit(X_train,Y_train)
y_pred=model.predict(X_test)
print("Accuracy of model without ensembling:",metrics.accuracy_score(Y_test,y_pred)*100,"%")


# In[82]:


AdaBoost=AdaBoostClassifier(base_estimator=model,n_estimators=70,learning_rate=0.5)
boost_model=AdaBoost.fit(X_train,Y_train)
y_pred=boost_model.predict(X_test)
predictions=metrics.accuracy_score(Y_test,y_pred)
print("Accuracy of ensembled model:",predictions*100,"%")


# In[ ]:


test_size   accuracy_score   n_estimator   hyperparameter_value 

