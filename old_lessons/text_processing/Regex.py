#!/usr/bin/env python
# coding: utf-8

# In[27]:


#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
import re
def text_match(text):
    pattern = '^a+.b$'
    if re.search(pattern,text):
        print('A match')
    else:
        print('No match')
print(text_match('alb'))


# In[45]:


#Write a Python program that matches a word at the beginning of a string
import re
def text_match(text):
    pattern = '^\w+'
    if re.search(pattern, text):
        print('A match')
    else:
        print('No match')
print(text_match('Suck some dick'))
print(text_match('  some dick'))


# In[67]:


#Write a Python program that matches a word at the end of string, with optional punctuation.
import re
def text_match(text):
    pattern='\w+\S*$'
    if re.search(pattern, text):
        return('A match')
    else:
        return('No match')
print(text_match('Suck some dick!'))
print(text_match('Suck some '))
print(text_match('Suck some dick!!!!!'))


# In[1]:


#Write a Python program that matches a word containing 'z'.
import re
def text_match(text):
    pattern='^\w*z.\w*$'
    if re.search(pattern, text):
        return('A match')
    else:
        return('No match')
print(text_match('azb'))
print(text_match('abc'))


# In[7]:


#Write a Python program where a string will start with a specific number. - Option 1

import re
def num_match(number):
    pattern='^5'
    if re.search(pattern, number):
        return('A match')
    else:
        return('No match')
print(num_match('567-678'))
print(num_match('666-566'))


# In[13]:


#Write a Python program where a string will start with a specific number. - Option 2

import re
def num_match(str_number):
    pattern=re.compile(r'^5')
    if re.match(pattern,str_number):
        return('A match')
    else:
        return('No match')
print(num_match('567-765'))
print(num_match('6780-567'))


# In[123]:


#Write a Python program to remove leading zeros from an IP address - Option 1

import re
ip_num = '02001:db8:0:01234:0:567:8:1'
pattern=re.subn('[0]','',ip_num)
print(pattern)


# In[111]:


import re

s = 'aaa@xxx.com bbb@yyy.com ccc@zzz.com'

print(re.sub('[a-z]*@', 'ABC@', s))


# In[124]:



#Write a Python program to remove leading zeros from an IP address - Option 2

import re
ip_num = '02001:db8:0:01234:0:567:8:1'
print(re.sub('[0]','',ip_num))


# In[132]:


#Write a Python program to check for a number at the end of a string. - Option 1

import re
def num_match(num):
    pattern= re.compile(r'5$')
    if re.search(pattern,num):
        return('A match')
    else:
        return('No match')
print(num_match('675-677'))
print(num_match('678-875'))


# In[141]:


#Write a Python program to check for a number at the end of a string. - Option 1

import re
def num_match(num):
    pattern=re.compile('.*[0-9]$')
    if re.search(pattern,num):
        return('A match')
    else:
        return('No match')
print(num_match('675'))
print(num_match('6777'))


# In[148]:


#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

import re

number='123456789678134512'
x=re.findall('[123]',number)
print(x)


# In[150]:


import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# In[165]:


#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. - Option 1

import re

string="Exercises number 1, 12, 13, and 345 are important"
pattern='\d+'
x=re.findall(pattern,string)
print(x)


# In[175]:


#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. - Option 2

import re

def match(quo):
    pattern='\d+'
    return(re.findall(pattern,quo))
print(match("Exercises number 1, 12, 13, and 345 and 567 are important"))


# In[190]:


#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. - Option 3
import re

def match(quo):
    pattern='([0-9]{1,3})'
    return(re.findall(pattern,quo))
print(match("Exercises number 1, 12, 13, and 345 are important"))


# In[214]:


#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. - Option 4
import re
result= re.finditer('([0-9]{1,3})',"Exercises number 1, 12, 13, 345 and 9000 are important")
for x in result:
        print(x.group(0))


# In[215]:


import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13,345 and 90000 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))


# In[265]:


#Write a Python program to search some literals strings in a string.- Option 1
#Searched words : 'fox', 'dog', 'horse'
import re
string='The quick brown fox jumps over the lazy dog.'
pattern='\W'
result=re.split(pattern,string)
print(result)
for x in result:
    if x== 'fox' or x== 'dog' or x=='horse':
        print(x)


# In[280]:


#Write a Python program to search some literals strings in a string.- Option 1
#Searched words : 'fox', 'dog', 'horse'

import re
pattern=['fox','dog','horse']

string='The quick brown fox jumps over the lazy dog.'

for x in pattern:
    print('Looking for "%s" in "%s"' % (x,string),)
    if re.search(x, string):
        print('A match')
    else:
        print('No match')
    

