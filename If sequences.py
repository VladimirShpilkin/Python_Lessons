#!/usr/bin/env python
# coding: utf-8

# In[1]:


number = 169
корень = number **(1/2)
if корень % 1 == 0:
    print("Квадратный корень из " + str(number) + " - целое число.")
else:
     print("Квадратный корень из " + str(number) + " - не целое число.")


# In[5]:


number = 170
корень = number **(1/2)
корень_2 = int(корень)
if корень - корень_2 == 0:
    print("Квадратный корень из {} - целое число.".format(number))
else:
     print("Квадратный корень из {} - не целое число.".format(number))


# In[3]:


number = 1
корень = number **(1/2)
print(корень % 1)


# In[4]:


number = 170
корень = number **(1/2)
корень_2 = int(корень)
print(корень_2)
print(корень - корень_2)


# In[5]:


print(8**5*36**(1/2))


# In[6]:


print(18 +6.996+(45*(13/2)**2))


# In[7]:


print(1267 - 20*((5**3)/2)**2)


# In[8]:


float(input(150))


# In[9]:


a = 23
b = a * 3
print("Вы ввели число, которое при умножении на 3 даёт",b)


# In[10]:


number = 5
if number == 1:
    print("понедельник")
elif number == 2:
    print("вторник")
elif number == 3:
    print("среда")
elif number == 4:
    print("четверг")
elif number == 5:
    print("пятница")
elif number == 6:
    print("суббота")
else:
    print("воскресенье")


# In[11]:


"5a"<"5b" and 123/2 > 30 or True


# In[12]:


False and True or 12<5**2 and "Python" > "Ruby"


# In[13]:


"Python" > "Ruby"


# In[14]:


False and True


# In[15]:


"239" < "30"


# In[16]:


flower = 'роза' 
color = 'фиолетовый'
if "роза" in flower and "синий" in color and "белый":
    print("Ане понравятся эти цветы")
else:
    print("Аня не фанат таких цветов")


# In[17]:


height = str(180)
weight = 92
color = 'синий'
if "170" in height and weight < 80 and color == "красный":
    print( "Ваша половинка нашлась!")
else:
    print("Попробуем поискать ещё...")


# In[18]:


fav_word = 'Аппликация'
if fav_word == "рептилия"  and "питон" and  "змея":
    print("gay")
elif fav_word == "плюс" and "плюсы":
    print("C++")
else:
    print("Python")


# In[19]:


hour = 19
minute = 59
if hour==10 and minute <=30 or 12 <= hour <= 13 and  0 <= minute <=40 or 15 <= hour <18 or hour>= 19 and minute > 30 or 19 == hour < 20 and minute > 30:
    print("Преподаватель свободен.")
elif hour == 12 and minute == 0 and hour == 15 and minute == 0 and hour == 18 and minute == 0:
    print("Преподаватель занят.")
else:
    print("Преподаватель занят.")


# In[ ]:





# In[20]:


hour = 13
minute = 1
if hour==10 and minute <=30:
    print("Преподаватель свободен.")
elif 12 <= hour <= 13 and 0 < minute <=40
    


# In[ ]:


#Y = int(input())
#Z = int(input())
Y = 170000
Z = 1000000
year = 0
mult = 1.1
while Y < Z:
    Y = Y*mult
    year += 1
else:
    print(year)


# In[ ]:


weight = 77
max_weight = 400
total_weight = 0
overweight = max_weight-total_weight
while total_weight<max_weight:
    total_weight += weight
else:
    print("Перевес", total_weight-max_weight, "кг")


# In[21]:


weight = 77
max_weight = 400
total_weight = 0
overweight = max_weight-total_weight
while total_weight<max_weight:
    total_weight += weight
else:
    print("Перевес", total_weight-max_weight, "кг")


# In[ ]:





# In[ ]:




