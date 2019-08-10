#!/usr/bin/env python
# coding: utf-8

# In[201]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[202]:


df=pd.read_csv(r'C:\Users\ananyya srivastava\Desktop\bank.csv')


# In[203]:


df.head()


# In[204]:


df.tail()


# In[205]:


df.shape


# In[206]:


df.info()


# In[207]:


df.isnull().sum()


# In[208]:


df.describe()


# In[209]:


df['job']=df['job'].replace(['management','admin.'],'whitecollar')
df['job']=df['job'].replace(['housemaid','technician'],'pinkcollar')
df['job']=df['job'].replace(['retired','students','unemployed','unknown','services'],'others')


# In[210]:


df['job'].value_counts()


# In[211]:


mapping={'single':0,'married':1,'divorced':2}
df['is_marital']=df['marital'].map(mapping)


# In[212]:


sns.boxplot(x=df.age)


# In[213]:


sns.distplot(df.age,bins=20)


# In[214]:


df.groupby('deposit').marital.value_counts()


# In[215]:


t1=pd.crosstab(df.marital,df.deposit)
t1.plot(kind='bar')


# In[216]:


t2=pd.crosstab(df.poutcome,df.deposit)
t2.plot(kind='bar')


# In[217]:


t3=pd.crosstab(df.job,df.deposit)
t3.plot(kind='bar')


# In[218]:


t4=pd.crosstab(df.education,df.deposit)
t4.plot(kind='bar')


# In[219]:


sns.boxplot(x='balance',y='marital',data=df,hue='deposit')
plt.show()


# In[220]:


sns.countplot(x='deposit', data=df, label='Count')


# In[221]:


sns.scatterplot(x='age', y='balance',hue='deposit', data=df)


# In[222]:


c=df.corr()
print(c)


# In[223]:


plt.figure(figsize=(10,8))
sns.heatmap(c)


# In[224]:


cov1=df.cov()
print(cov1)


# In[225]:


map1={'yes':1,'no':0,'Yes':1,'No':0}
df['deposits']=df['deposit'].map(map1)


# In[226]:


df['house']=df['housing'].map(map1)
df['loans']=df['loan'].map(map1)


# In[227]:


map2={'secondary':0,'primary':1,'tertiary':2,'unknown':3}
df['educations']=df['education'].map(map2)


# In[228]:


df.drop(['contact','month','day'],axis=1,inplace=True)


# In[229]:


df.groupby('deposit').marital.value_counts()


# In[230]:


df.groupby('deposit').poutcome.value_counts()


# In[231]:


sns.pairplot(df,hue='deposit')
plt.show()


# In[232]:


mapp={'whitecollar':0,'blue-collar':1,'technician':2,'others':3,'pinkcollar':4,'self-employed':5,'entrepreneur':6}
df['is_jobs']=df['job'].map(mapp)


# In[178]:


df.head()


# In[179]:


df.drop(['job','marital','education','loan','housing','deposit'],axis=1,inplace=True)


# In[180]:


df.head()


# In[181]:


map5={'failure':0,'success':1,'unknown':2,'other':3}
df['outcome']=df['poutcome'].map(map5)


# In[182]:


df.head()


# In[183]:


df.drop(['poutcome'],axis=1,inplace=True)


# In[184]:


df.head()


# In[185]:


df['is_default']=df['default'].map(map1)


# In[186]:


df.drop(['default'],axis=1,inplace=True)


# In[187]:


df.head()


# In[188]:


sns.boxplot(x=df.duration,data=df)


# In[192]:


plt.figure(figsize = (10,6))
sns.barplot(x='is_jobs', y = 'duration', data = df)


# In[200]:


plt.figure(figsize = (10,6))
sns.barplot(x='outcome', y = 'duration', data =df)
plt.legend(['failure','success','unknown','other'],loc='upper left')


# In[197]:


plt.figure(figsize=(20,10))
sns.heatmap(data=df.corr(), annot=True, cmap='viridis')


# In[ ]:




