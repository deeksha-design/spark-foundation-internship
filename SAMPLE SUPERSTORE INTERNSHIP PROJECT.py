#!/usr/bin/env python
# coding: utf-8

# To perform EDA on samplesuperstore dataset and also  gain the insights to find out the weakareas where we can workout to gain more profit
# 

# In[2]:


##first import the libararies :
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("SampleSuperStore.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.isnull().sum()


# In[8]:


df.hist()


# In[9]:


df.describe()


# In[10]:


df.info()


# In[11]:


df.dtypes


# In[12]:


df.drop_duplicates()


# In[14]:


df.nunique()


# In[18]:


df = df.drop(['Postal Code'], axis=1)
df = df.drop(['Country'], axis=1)


# In[19]:


df.head()


# In[20]:


df.corr()


# In[ ]:


###graphical representation of data


# In[21]:


plt.figure(figsize=(10,5))
sns.heatmap(df.corr(),annot=True)


# In[22]:


sns.pairplot(df,hue='Ship Mode')


# In[23]:


df['Sub-Category'].value_counts()


# In[26]:


plt.figure(figsize=(16,8))
plt.bar('Sub-Category','Category', data=df)
plt.show()


# In[28]:


plt.figure(figsize=(12,10))
df['Sub-Category'].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()


# In[29]:


sns.countplot(x=df['Ship Mode'])


# In[30]:


sns.countplot(x=df['Region'])


# In[31]:


sns.countplot(x=df['State'],order=(df['State'].value_counts().head(20)).index)
plt.xticks(rotation=90)


# In[32]:


sns.countplot(x=df['Category'])


# In[33]:


sns.countplot(x=df['Sub-Category'], order=(df['Sub-Category'].value_counts().head(20)).index)
plt.xticks(rotation=90)


# In[ ]:


###visualization of sales ,quantity,discount,profit using histogram


# In[34]:


df.hist(figsize=(10,10),bins=50)
plt.show()


# In[35]:


pd.DataFrame(df.groupby('State').sum())['Profit'].sort_values(ascending=True)


# In[36]:


sns.lineplot(x="Discount", y="Profit",label = "Profit",data=df)
plt.legend()
plt.show()


# In[ ]:


###visualizing profit and sales accross different segments


# In[37]:


df.groupby("Segment")[['Profit', 'Sales']].sum().plot.bar(color = ["blue", "green"],figsize= (8,5))
plt.ylabel("Profit /loss and Sales")
plt.show()


# In[ ]:


##visualizing segment wise sales distribution in each region


# In[41]:


plt.figure(figsize=(12,8))
plt.title("Distribution of Segment wise sales in each region " , fontsize=15)
sns.barplot(x="Region",y='Sales',data=df,hue='Segment',order=df['Region'].value_counts().index,palette='Blues')
plt.xlabel('Region', fontsize=15)
plt.tick_params(labelsize=12) 
plt.show()


# In[ ]:


###Visualizing profit and sales (regions)


# In[42]:


df.groupby("Region")[['Profit', 'Sales']].sum().plot.bar(color = ["green", "yellow"],figsize= (8,5))
plt.ylabel("Profit /loss and Sales")
plt.show()


# In[ ]:


##visualizing profit and sales(states)


# In[43]:


dt = df.groupby("State")[["Sales", "Profit"]].sum().sort_values(by = "Sales", ascending = False)
dt[:].plot.bar(color = ["Red", "blue"],figsize= (18,8))
plt.title("Profit/Loss & Sales across States")
plt.xlabel("States")
plt.ylabel("Profit/Loss & Sales")
plt.show()


# In[ ]:


##high sales in states


# In[46]:


data= df['State'].value_counts().nlargest(10)


# In[47]:


data


# In[ ]:


###The observation of the dataset


# 1 Maximum number of buyers prefers to choose standard class ship mode.Maximum number of buyers are from states like California and New York.
# 
# 2 There is a weak relatinship between profit and discount, company should take further decisons accordingly.
# 
# 3 The Company has a lot of profit in sale of copier but the number of sales is very less so there is a need for increasing the     number of sales of copier
# 4  Western region has the highest sales and profit, southern region has the least sales , but a good profit with its sales.
# 
# 5.California and New York have high sales with a good profit but Texas, Pennsylvania, Ohio face huge losses.
# 
# 6.Technology and office supplies category have high sales and good profit but Furniture category has least profit when compared with the remaining categories.
# 7 Sales and Profit were highest in consumer segment and least in Home office segment.
# 
# ###TASK 3 COMPLETED
# 
# 
