#!/usr/bin/env python
# coding: utf-8

# In[88]:


import json
with open('D:\Python\JSON\example_2.json','rb') as infile:
    x = json.load(infile)
    info = x['quiz']
    print(info)


# In[50]:


import json
with open('D:\Anakonda\JSON\example_2.json','rb') as infile:
    x = json.load(infile)
    info = x["quiz"]
    print(info)


# In[84]:


import json
with open('D:\Anakonda\JSON\Sample-employee-JSON-data.json','rb') as infile:
    x = json.load(infile)
    info = x['Employees']
    print(info)


# In[89]:


import json
with open('‪D:\Anakonda\JSON\sales.json','rb') as infile:
    x =json.load(infile)
    i = x['conformsTo']
    print(i)


# In[83]:


import json
import requests
r = requests.get('https://data.cityofnewyork.us/api/views/zt9s-n5aj/rows.json?accessType=DOWNLOAD')
j = r.json()
data = json.load(j)
print(j['meta'])

