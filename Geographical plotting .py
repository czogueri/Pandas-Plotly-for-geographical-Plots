#!/usr/bin/env python
# coding: utf-8

# In[1]:


#choropleth maps


# In[22]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import pandas as pd


# In[5]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[6]:


init_notebook_mode(connected = True)


# In[17]:


data = dict(type='choropleth', 
           locations = ['AZ','CA','NY'],
           locationmode= 'USA-states', 
           colorscale='Portland',
           text =['text1','text2','text3'],
           z=[1.0,2.0,3.0],
           colorbar ={'title':'colorbar Title Goes Here'})


# In[18]:


data


# In[10]:


layout = dict(geo={'scope':'usa'})


# In[19]:


choromap = go.Figure(data = [data],layout = layout)


# In[21]:


iplot(choromap)


# In[39]:


df = pd.read_csv('Downloads/Refactored_Py_DS_ML_Bootcamp-master/09-Geographical-Plotting/2011_US_AGRI_Exports')


# In[40]:


df.head()


# In[50]:


data = dict(type = 'choropleth',
            colorscale = 'ylorbr',
            locations = df['code'],
            locationmode ='USA-states',
            z = df['total exports'],
            text = df['text'],
            marker = dict(line =dict(color = 'rgb(255,255,255)', width=2)),
            colorbar ={'title':'Millions USD'}
           )


# In[48]:


layout = dict(title = '2011 US Agriculture Exports by State',
             geo = dict(scope= 'usa', 
                        showlakes = True, 
                        lakecolor ='rgb(85,173,240)'))


# In[49]:


layout


# In[53]:


choromap2 = go.Figure(data = [data], layout =layout)


# In[55]:


iplot(choromap2)


# In[ ]:





# In[ ]:





# In[56]:


#Choropleth International Maps


# In[57]:


df = pd.read_csv('Downloads/Refactored_Py_DS_ML_Bootcamp-master/09-Geographical-Plotting/2014_World_GDP,)


# In[59]:


df.head()


# In[62]:


data = dict(type = 'choropleth',
           locations =df['CODE'],
           z= df['GDP (BILLIONS)'],
           text =df['COUNTRY'],
           colorbar={'title': 'GDP in Billions UDS'})


# In[68]:


layout = dict(title = '2014 Global GDP',
             geo = dict(showframe = False,
                       projection = {'type': 'mercator'}))


# In[69]:


choromap3 = go.Figure(data=[data], layout = layout)


# In[70]:


iplot(choromap3)


# In[ ]:




