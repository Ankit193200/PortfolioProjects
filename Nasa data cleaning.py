#!/usr/bin/env python
# coding: utf-8

# In[76]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 


# In[109]:


df = pd.read_json('https://data.nasa.gov/resource/y77d-th95.json')


# In[110]:


df.head(2)


# In[111]:


df.isnull().sum()


# In[112]:


df.info()


# In[113]:


df.shape


# In[114]:


df.head(2)


# In[115]:


df=df.drop([':@computed_region_cbhk_fwbd'],axis=1)
df=df.drop([':@computed_region_nnqa_25f4'],axis=1)


# In[116]:


df.head()


# In[117]:


df.info()


# In[118]:


df.isnull().sum()


# In[119]:


df['mass'].replace([np.nan], df['mass'].mean(), inplace=True)


# In[120]:


df.isnull().sum()


# In[121]:


df.info()


# In[122]:


df['reclat'].replace([np.nan], df['reclat'].mean(), inplace=True)


# In[123]:


df['reclong'].replace([np.nan], df['reclong'].mean(), inplace=True)


# In[124]:


df['year'].unique()


# In[125]:


df.select_dtypes(include='object').fillna("NULL", inplace=True)


# In[126]:


df.info()


# In[127]:


df.isnull().sum()


# In[128]:


df = df.fillna(method = 'pad') 


# In[129]:


df.isnull().sum()


# In[130]:


df.info()


# In[131]:


df.head()


# In[132]:


df['mass'].unique()


# In[133]:


df.head()


# # question 
# Get all the Earth meteorites that fell before the year 2000
# ● Get all the earth meteorites co-ordinates who fell before the year 1970
# ● Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more
# than 10000kg
# 

# In[134]:


df[['Year', "month", "day"]] = df['year'].str.split("-", expand = True)


# In[135]:


df.head()


# In[136]:


df['Year'].isnull().sum()


# In[137]:


df['Year'].unique()


# In[139]:


df=df.drop(['month','day'],axis=1)


# In[138]:


df.info()#df['Year'].fillna(method = 'pad')


# In[140]:


df.head()


# In[141]:


df.info()


# In[142]:


df['Year']=df['Year'].astype(int)


# In[143]:


df.info()


# # question 
# Get all the Earth meteorites that fell before the year 2000
# ● Get all the earth meteorites co-ordinates who fell before the year 1970
# ● Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more
# than 10000kg

# In[144]:


filtered_df = df[df['Year']<2000]


# In[145]:


filtered_df['name']


# # Get all the earth meteorites co-ordinates who fell before the year 1970

# In[68]:


filtered_df = df[df['Year']<1970]


# In[69]:


filtered_df['geolocation']


# In[70]:


df.head()


# # Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more than 10000kg

# In[146]:


filtered_df = df[df['mass']>10000]


# In[147]:


filtered_df['mass'].unique()


# In[74]:


df.to_csv("cleaned-nasa_dataset")


# In[ ]:




