#!/usr/bin/env python
# coding: utf-8

# In[3]:


animals = 'кошка,собака,хомяк,морская свинка,попугай,лошадь'.split()
print(animals)


# In[5]:


OurBestStudents = ['Александр', 'Константин', 'Мария', 'Диана', 'Алексей', 
                   'Максим', 'Светлана', 'Арина', 'Серафим', 'Doomer', 
                   'Павел', 'Виктория', 'Елена', 'Галина', 'Вячеслав']
print(OurBestStudents[0])
print(OurBestStudents[5])
print(OurBestStudents[3])
print(OurBestStudents[13])
print(OurBestStudents[8])
print(OurBestStudents[14])
print(OurBestStudents[10])


# In[18]:


body = ['голова', 'руки', 'ноги', 'глаза', 'уши', 'рот', 'нос', 'туловище']
body[-5:-1]


# In[19]:


body = ['голова', 'руки', 'ноги', 'глаза', 'уши', 'рот', 'нос', 'туловище']
body[-3:7]


# In[20]:


body = ['голова', 'руки', 'ноги', 'глаза', 'уши', 'рот', 'нос', 'туловище']
body[-5:7]


# In[14]:


body = ['голова', 'руки', 'ноги', 'глаза', 'уши', 'рот', 'нос', 'туловище']
body[-5:-1]


# In[21]:


body = ['голова', 'руки', 'ноги', 'глаза', 'уши', 'рот', 'нос', 'туловище']
body[-1:-5]


# In[27]:


body = ['голова', 'руки', 'ноги', 'глаза', 'уши', 'рот', 'нос', 'туловище']
body[:]


# In[30]:


body = ['голова', 'руки', 'ноги', 'глаза', 'уши', 'рот', 'нос', 'туловище']
body[-7:-5]


# In[26]:


body = ['голова', 'руки', 'ноги', 'глаза', 'уши', 'рот', 'нос', 'туловище']
body


# In[24]:


body = ['голова', 'руки', 'ноги', 'глаза', 'уши', 'рот', 'нос', 'туловище']
body[1:]


# In[2]:


OurBestStudents = ['Александр', 'Константин', 'Мария', 'Диана', 'Алексей', 
                   'Максим', 'Светлана', 'Арина', 'Серафим', 'Doomer', 
                   'Павел', 'Виктория', 'Елена', 'Галина', 'Вячеслав']
print(len(OurBestStudents))
print(OurBestStudents[14])


# In[34]:


int(4**1/2)


# In[42]:


body[7:-1]


# In[53]:



s = 0

for x in range(2):

 for y in range(2):

     s = s+10*x+y
print(s)


# In[55]:


sparta = ['Иванов', 'Петров', 'Сидоров', 'Зайцев', 'Дятлов', 
          'Козлов', 'Лисичкин', 'Огурцов', 'Капустин', 'Арбузов']
print(sparta[0:10:2])


# In[57]:


sparta = ['Иванов', 'Петров', 'Сидоров', 'Зайцев', 'Дятлов', 
          'Козлов', 'Лисичкин', 'Огурцов', 'Капустин', 'Арбузов']
sparta[::-3]


# In[58]:


sparta = ['Иванов', 'Петров', 'Сидоров', 'Зайцев', 'Дятлов', 
          'Козлов', 'Лисичкин', 'Огурцов', 'Капустин', 'Арбузов']
sparta[-2:1:-3]


# In[65]:


names = ['Андрей', 'Илья', 'Александр', 'Ипполит', 'Анна', 'Константин', 'Елена', 'Мария']
my_list = []
for name in names:
    my_list.append(len(name))
name_length = min(my_list)
result = my_list.count(name_length)
print(result)


# In[66]:


my_list = [1, 10, 45, 31, 12, 54, 111, 398, 97, 63]
my_list.sort(reverse = True)
print(my_list[2])


# In[73]:


my_list = [1, 10, 45, 31, 12, 54, 111, 398, 97, 63]
result = my_list.count('batman')
print(result)


# In[74]:


my_list = [1, 10, 45, 31, 12, 54, 111, 398, 97, 63]
my_list.sort(reverse = True)
new_list = my_list[::2]
result = 0
for number in new_list:
    result += number
print(result)


# In[83]:


my_list = [1]
for i in range(10):
    my_list.append(my_list[i] * 2)
my_list.sort(reverse = True)
print(my_list)


# In[109]:


my_list = [1]
for i in range(10):
    my_list.append(my_list[i] * 2)
my_list.sort(reverse = True)
print(my_list)


# In[91]:


fruits = 'яблоко банан апельсин баклажан перец помидор арбуз ананас'.split()
my_list = []
for fruit in fruits:
    my_list.append(fruit[0])
    print(my_list)


# In[94]:


fruits = 'яблоко банан апельсин баклажан перец помидор арбуз ананас'.split()
my_list = []
for fruit in fruits:
    my_list.append(fruit[0])
print(my_list.count(my_list[0]))


# In[101]:


fruits = 'яблоко банан апельсин баклажан перец помидор арбуз ананас'.split()
my_list = []
for fruit in fruits:
    my_list.append(fruit[0])
my_list.sort()
my_list.count(my_list[0])
print(my_list.count(my_list[0]))


# In[127]:


my_list = []
for count in range(3,51,3):
    my_list.append(count)
print(sum(my_list))
    


# In[144]:


raw_list = ['переменные', 'циклы', 'условия', 'списки', 'словари', 'файлы', 'функции']
my_list=[]
for list in raw_list:
    my_list.append(len(list))
max_len = max(my_list)
min_len = min(my_list)
print(max_len + min_len)
    


# In[184]:


raw_list = [2, 8, 10, 23, 64, 49, 11, 52, 71, 14]
x_min=min(raw_list)
x_max=max(raw_list)
my_list_odds=[]
my_list_evens=[]
my_list=[]
for i in raw_list:
    if i%2==0:
        my_list_odds.append(i*x_min)
    elif i%2 !=0:
        my_list_evens.append(i*x_max)
        my_list=(my_list_evens+my_list_odds)
        my_list.sort()
print(my_list)
result = (max(my_list))
print(result)


        
    


# In[187]:


powers = [x**y for x in range(1, 10) for y in [2,10]]
print(powers)


# In[192]:


powers = [x**x for x in range(1, 10)]
print(powers)


# In[194]:


numbers = [x*y for x in range(1, 10) for y in [3, 5, 7]]
print(numbers)


# In[196]:


numbers = [x for x in range(3,100) if [x%y for y in range(2,x)].count(0) == 0]
print(numbers)


# In[198]:


my_list = [x for x in 'п р и в е т'.split()]
print(my_list)


# In[199]:


my_list = 'привет'.split()[if x in ['п', 'р', 'в', 'т']]
print(my_list)


# In[201]:


my_list = [x for x in 'привет' for y in ['п', 'р', 'в', 'т']]
print(my_list)


# In[203]:


my_list = [x for x in 'привет' if x in ['п', 'р', 'в', 'т']]
print(my_list)


# In[205]:


my_list = sorted([x for x in 'синхрофазотрон'])
print(my_list)


# In[208]:


my_list = 'синхрофазотрон'.split().sort()
print(my_list)


# In[210]:


my_list = [x for x in 'синхрофазотрон' if x > x[0]]
print(my_list)


# In[212]:


my_list = [x for x in 'синхрофазотрон' if x > x[0]]
print(my_list)


# In[218]:


my_list = []
for x in range(1, 50):
    if x%7 == 0:
        my_list.append(x**0.5)
print(my_list)


# In[233]:


my_list=[x**0.5 for x in range(1,50) if x%7==0]
print(my_list)


# In[250]:


my_list = []
for x in range(90, 100):
    first_digit = x//10
    last_digit = x%10
    my_list.append(first_digit + last_digit)
print(my_list)


# In[259]:


my_list = []
for x in range(90, 100):
    first_digit=x//10
    last_digit = x%10
    my_list.append(last_digit)
print(my_list)


# In[263]:


my_list = []
for x in range(90, 100):
    first_digit=x//10
    my_list.append(first_digit)
print(my_list)


# In[269]:


my_list = [(x//10 + x%10) for x in range(90,100)]
print(my_list)


# In[270]:


phones = [['+79033923029', 'Мария Никитина'], ['+78125849204', 'Егор Савичев'], ['+79053049385', 'Александр Пахомов'], ['+79265748370', 'Алина Егорова'], ['+79030598495', 'Руслан Башаров']]
print(phones)

