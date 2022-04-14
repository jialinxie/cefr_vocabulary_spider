#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import random
from requests.auth import HTTPBasicAuth
# from sqlalchemy import null


url = """http://vocabulary.englishprofile.org/dictionary/search/us/?pageSize=5000&q=&wl=305&p=1"""
page = requests.get(url, auth=('englishprofile', 'vocabulary'))

# path = '/Users/xiejialin/Downloads/cefr/b2/CEFR_B2.html'
# htmlfile = open(path, 'r', encoding='utf-8')
# htmlhandle = htmlfile.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text, 'lxml')
list = soup.findAll('span', { "class" : "base"})

#save to file
with open('cefr_c1.txt', 'w')as f:
    for item in list:
        f.write("%s\n" % item.text)

