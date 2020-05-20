#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
f=open(r'C:\Users\shpilkvl\Anaconda3\CSV\electronic-card-transactions-march-2020-csv-tables.csv')
data = csv.reader(f)
for x in data:
    print


# In[3]:


a = open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
data = csv.reader(a)
for x in data:
    print


# In[47]:


a = open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
males = 0
females = 0
for x in a:
    info = x.split(',')
    gender = info[0][1:-1]
    if gender == 'male':
        males+=1
    elif gender == 'female':
        females+=1
print('Всего мальчиков {}, а девочек {}'.format(males,females))
        
print(males)
print(females)


# In[60]:


x=open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
educated=0
for z in x:
    info=z.split(',')
    diploma=info[2][1:-1]
    if diploma=="high school" or diploma=="some college" or diploma=="associate's degree":
        educated+=1
print('There are {} educated parents in the class'.format(educated))   
print(educated)
        


# In[58]:


x=open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
bachelor=0
for y in x:
    divide=y.split(',')
    diploma=divide[2][1:-1]
    if diploma=="bachelor's degree":
        bachelor+=1
print(bachelor)
print('There are {} bachelor degree parents in the class'.format(bachelor))
    

       


# In[49]:


x=open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
lunch=0
total=0
for y in x:
    divide=y.split(',')
    total_amount=divide[3][1:-1]
    if len(total_amount)>0:
        total+=1
print(total)


# In[35]:


x=open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
lunch=0
total=0
for y in x:
    divide=y.split(',')#creating a list using the split function
    had_lunch=divide[3][1:-1]#slicing the list by the fourth element and cutting the 0th and the last bracket
    if had_lunch=="standard":
        lunch+=1
    else:
        total+=1
print(lunch/(lunch+total))
print('{} students had standard lunch before the exam and {} students did not'.format(lunch,total))


# In[31]:


import csv
x=open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
unique_values=[]
for y in x:
    divide=y.split(',')#creating a list using the split function
    diplomed=divide[2][1:-1]#slicing the list by the third element and cutting the 0th and the last bracket and creating new variable
    if diplomed not in unique_values:
        unique_values.append(diplomed)
print(unique_values[1:])
print(len(unique_values)-1)


# In[61]:


import csv
x=open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
groupC=0
for y in x:
    div=y.split(',')
    eth=div[1][1:-1]
    if eth=='group C':
        groupC+=1
    else:
        pass
print(groupC)
    


# In[1]:


import csv
x=open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
eth_types=[]
for y in x:
    divide=y.split(',')
    types=divide[1][1:-1]
    if types not in eth_types:
        eth_types.append(types)
print(len(eth_types[1:]))
    


# In[5]:


import csv
y=[]
x=open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
for line in x:
    info=line.split(',')
    if info[0]=='gender':
        continue
    else:
        y.append(info[5][1:-1])
print(y[1:])


# In[71]:


#Вычислите средний балл абитуриентов на экзамене по чтению (reading score).
marks=[]
x=open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
for line in x:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        y = int(info[6][1:-1])
        marks.append(y)
median=sum(marks)/len(marks)

print(median)


# In[43]:


#Вычислите средний балл абитуриентов на экзамене по чтению (reading score).

import re

reading=[]

f= open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')

for exam_results in f:
    info=exam_results.split(',')
    if info[0]=='"gender"':
        continue
    else:
        reading.append(int(info[-2][1:-1]))
        median=sum(reading)/len(reading)
        for x in reading:
            test=[]
            if x<=median:
                test.append(x)


# In[69]:


#Сколько абитуриентов получили на экзамене по чтению (reading score) оценку ниже среднего?
import re
exams=[]
pattern=re.compile('\d+')
avg=69.169
f= open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
for exam_results in f:
    info=exam_results.split(',')
    if info[0]=='gender':
        continue
    else:
        if info[6][1:-1]=='reading score':
            continue
        else:
            mark=int(info[6][1:-1])
            if mark<avg:
                exams.append(mark)
print(len(exams))


# In[68]:


#Какой средний балл на экзамене по чтению (reading score) получили девочки?
import re
exams=[]
f = open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
for exam_results in f:
    info=exam_results.split(',')
    if info[0]=='gender':
        continue
    else:
        if info[6][1:-1]=='reading score':
            continue
        elif info[0][1:-1]=='male':
            continue
        else:
            mark=int(info[6][1:-1])
            exams.append(mark)
print(sum(exams)/len(exams))


# In[213]:


#Сколько абитуриентов получили на экзамене по письму (writing score) оценку выше 90?
import re
exams=[]
good=[]
f =open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
for exam_results in f:
    info=exam_results.split(',')
    if info[0]=='gender':
        continue
    elif info[7][1:-2] =='writing score':
        continue
    elif int(info[7][1:-2])<90:
        continue
    else:
        mark=int(info[7][1:-2])
        exams.append(mark)
print(exams)


# In[272]:


#Сколько абитуриентов получили на экзамене по письму (writing score) оценку выше 90?
import re
exams=[]
good=[]
f =open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
for exam_results in f:
    info=exam_results.split(',')
    if info[0]=='gender':
        continue
    elif info[7][1:-2] =='writing score':
        continue
    else:
        mark=int(info[7][1:-2])
        if mark>90:
            exams.append(mark)            
print(len(exams))


# In[300]:


#Сколько абитуриентов получили на экзамене по письму (writing score) оценку выше 90?
import re
exams=[]
good=[]
f =open(r'C:\Users\shpilkvl\Anaconda3\CSV\StudentsPerformance.xls')
for exam_results in f:
    info=exam_results.split(',')
    if info[0]=='gender':
        continue
    elif info[7][1:-2] =='writing score':
        continue
    else:
        mark=int(info[7][1:-2])
        lunch=info[3][1:-1]
        if mark>90 and lunch == 'standard':
            exams.append(mark)            
print(len(exams))
print(len(exams)/68)


# In[ ]:




