#!/usr/bin/env python
# coding: utf-8

# Perform ‘Exploratory Data Analysis’ on dataset ‘Global Terrorism’

# In[ ]:


##import all neccessary libraries


# In[9]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import os
os.getcwd()
os.chdir('G:\\')


# In[11]:


df = pd.read_csv("globalterrorism.csv",encoding='latin1')


# In[12]:


df.head()


# In[13]:


df.shape


# In[14]:


df.isnull().sum()


# In[15]:


##rename columns :
df.rename(columns={'iyear':'year','imonth':'month','iday':'day','country_txt':'Country','region_txt':'Region','provstate':'State','natlty1_txt':'nationality_of_target','weaptype1_txt':'WeaponType','nkill':'killed','nwound':'wounded'},
          inplace=True)


# In[ ]:


##I choose some relevant features for data analysis


# In[16]:


df=df[['year','month','day','Country','Region','city','extended','latitude','longitude','vicinity','suicide','success','State','nationality_of_target','WeaponType','killed','wounded']]


# In[17]:


df.describe().T


# In[18]:


df['year'].value_counts() ##calculate the value counts(),


# In[19]:


df['month'].value_counts()


# In[20]:


df['day'].value_counts()


# In[21]:


df['Country'].value_counts()


# In[22]:


df['nationality_of_target'].value_counts()


# In[ ]:


##Number of Killings in each Region


# In[23]:


killings_per_region=df.groupby(['Region'],as_index=False)['killed']


# In[24]:


killings_per_region.sum()


# In[26]:


killings_per_region.max()


# In[29]:


#Sum of all wounded cases
df['wounded'].sum()


# In[32]:


##Total Casualities

df['casualities']=df['killed']+df['wounded']
df['casualities'].sum()


# In[ ]:


##Sum of all casualities in accordance to Region


# In[33]:


df1=df.groupby('Region')['casualities'].sum()
df2=df1.to_frame()
df2.reset_index()


# In[ ]:


##Year and Regionwise casulatity Count


# In[34]:


region_and_yearwise_casualitycount=df.groupby(['Region', 'year'])['casualities'].count().head()


# In[35]:


region_and_yearwise_casualitycount


# In[37]:


##Plotting Year and Regionwise casulatity Count


# In[38]:


plt.subplots(figsize=(18,8))
df.groupby(['Region', 'year']).count()['casualities'].plot()
plt.xticks(rotation=90)
plt.ylabel("Casualities")


# In[ ]:


#Terrorist Attacks


# In[39]:


print('Country with Highest Terrorist Attacks:',df['Country'].value_counts().index[0])
print('Regions with Highest Terrorist Attacks:',df['Region'].value_counts().index[0])
print('Maximum people killed in an attack are:',df['killed'].max(),'that took place in',df.loc[df['killed'].idxmax()].Country)
print("Nationality of the maximally targetted group is:", df['nationality_of_target'].value_counts().index[0])


# In[40]:


#Count of the weapons used in these attacks


# In[41]:


plt.subplots(figsize=(15,4))
sns.countplot('WeaponType',data=df,palette='inferno',order=df['WeaponType'].value_counts().index)
plt.xticks(rotation=90)
plt.xlabel('Weapon Type')
plt.title('Weapons used by Terrorists')
plt.show()


# In[42]:


sns.set_style('whitegrid')
print(df.success.value_counts())
sns.countplot('success',data=df).set_title('Success Outcome')


# In[ ]:


##How number of kills varies with increase in the year with respect to the extended parameter that is if the people killed were involved in an encounter for more than 24 hours


# In[43]:


sns.lmplot(x='year',y='killed',data=df,fit_reg=False,hue='extended',legend=True,palette="Set1")


# In[ ]:


#Top Countries affected by terrorist attacks


# In[44]:


plt.subplots(figsize=(15,8))
sns.barplot(df['Country'].value_counts()[:30].index,df['Country'].value_counts()[:30].values,palette='RdYlGn_r')
plt.title('Top countries Affected')
plt.xticks(rotation=90)
plt.xlabel('Countries')
plt.ylabel('Count')
plt.show()


# In[ ]:


#Number Of Terrorist Activities Each Year


# In[45]:


plt.subplots(figsize=(15,8))
sns.countplot('year',data=df,palette='RdYlGn_r',edgecolor=sns.color_palette('dark',7))
plt.xticks(rotation=90)
plt.xlabel('Year of attack')
plt.title('Number Of Terrorist Activities Each Year')
plt.show()


# In[46]:


##Terrorist Activities by region in each year


# In[47]:


df_region=pd.crosstab(df.year,df.Region).plot(kind='area',figsize=(20,10))
plt.title('Terrorist Activities by region in each year')
plt.ylabel('Attacks')
plt.show()


# In[ ]:




