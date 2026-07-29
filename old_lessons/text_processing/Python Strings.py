#!/usr/bin/env python
# coding: utf-8

# In[6]:


rainbow_dict = {'каждый': 'красный', 
                'охотник': 'оранжевый', 
                'желает': 'жёлтый', 
                'знать': 'зелёный', 
                'где': 'голубой', 
                'сидит': 'синий', 
                'фазан': 'фиолетовый'}

for x,y in rainbow_dict.items():
    print(x,y)


# In[8]:


string = 'Вы - самый крутой студент в SkillFactory'
for letter in string:
    print(letter, end = '')


# In[26]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'.split()
print(proverb[0])


# In[1]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
result=proverb.split()[0]
print(proverb.split()[0])


# In[29]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
result = proverb.split()
print(result[0])
print(proverb.split()[0])


# In[131]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
x = len(proverb)
print(proverb[-13:-9])


# In[147]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
print(proverb[19:28]+'о')


# In[149]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
print(proverb[19:28],'о')


# In[166]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
print(proverb.split()[3][:-2])


# In[167]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
result=proverb.split()[3][:-2]+'о'
print(result)


# In[219]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
result_string=''
for x in range(len(proverb)):
    if int(x)%2==0:
        print(x, end = '')


# In[186]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
proverb_odd=proverb[::2]
proverb_even=proverb[1::2]
x = proverb_even.replace(proverb_even, proverb_odd)
print(x)


# In[181]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
odd = proverb[::2]
even=proverb[1::2]
result_string = ''
index = 0
for x in proverb:
    if (index % 2 != 0):
      s = result_string.join(x)
    index +=1
    print(s[::2],end='')
    

        
        


# In[185]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
odd = proverb[::2]
even=proverb[1::2]
index = 0

def proverb_new(str):
    result_string = ''
    for x in range(len(proverb)):
        if x % 2==0:
            result_string=result_string+str[x]
    return result_string
print(proverb_new(proverb))
        


# In[184]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
odd = proverb[::2]
even=proverb[1::2]
index = 0


# In[188]:


basic_word = 'программирование'
inverted_word = basic_word[::-1]
if basic_word == inverted_word:
    print('Слово "{}" является палиндромом'.format(basic_word))
else:
    print('Слово "{}" - это не палиндром'.format(basic_word))


# In[202]:


proverbs = ['Без труда не вытянешь и рыбку из пруда', 
            'Терпение и труд всё перетрут', 
            'Работа не волк - в лес не убежит', 
            'Чем труднее дело, тем выше честь', 
            'Учиться, учиться и учиться!']

counter = 0
for proverb in proverbs:
    if 'труд' in proverb:
        counter += 1
    counter= proverb.count('труд')
    print(counter)


# In[204]:


tongue_twister = 'Ехал Грека через реку, видит Грека - в реке рак. Сунул Грека руку в реку, рак за руку Греку - цап!'
counter = tongue_twister.count('Грек')
print(counter)


# In[1]:


proverb = 'Хорошо написанная программа - это программа, написанная 2 раза'

while True:
    index = proverb.find('программа')
    if index == -1:
        break
    secret = proverb[:index].split()[-1]
    proverb = proverb[index+9:] 
    print(secret)


# In[14]:


proverb = 'Хорошо написанная программа - это программа, написанная 2 раза'

while True:
    index = proverb.find('программа')
    if index == -1:
        break
    secret = proverb[:index].split()[-1]
    proverb = proverb[index+1:]
    print(proverb)


# In[1]:


email = 'VeryBigBoss@skillfactory.ru'
domain = email.find('@')
pos = email[domain+1:]
print(pos)
print(email[email.find('@')+1:])


# In[53]:


number = 56.257
new_number = []
for x in str(number):
    new_number += x
    b = (new_number[3:])
test_list = [int(i) for i in b]
print(sum(test_list))





# In[25]:


emails_list = ['vasya@mail.ru', 
          'akakiy@yandex.ru', 
          'spyderman@yandex.ru', 
          'XFiles@gmail.com', 
          'hello@mail.ru', 
          'noname@gmail.com', 
          'DonaldTrump@mail.ru', 
          'a768#af@yandex.ru', 
          'Ivan_Ivanovich@yandex.ru', 
          'thebestmail@yandex.ru']

print({i : emails_list[i] for i in range(0,len(emails_list))})


# In[71]:


string = 'Интернет-открытки - это лучшее средство для мужчины сказать женщине о своих чувствах прямо в глаза.'
secret = string[24:30]
new_string = string.replace(secret.lower(), secret.upper()) 
print(new_string)
print(string)


# In[3]:


food = input('Какое ваше любимое блюдо: ')
if food.lower() == 'ОВСЯНКА': 
        print('Да Вы гурман!')


# In[1]:


string = 'dick'
string = string.replace(string[0].lower(), string[0].upper())
print(string)


# In[23]:


string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
new_string=[]
for x in string:
    new_string.append(str(x.replace('-',':)').replace(',',':)')))
print({i:string[i] for i in range(0,len(string))})


# In[36]:


string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
print(string.replace('-', ':)').replace('.',':)').replace(', ',':)').replace(' - ',':)').replace('?',':)')i.replace)


# In[1]:


string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
new_string=string.replace('-', ':)').replace('.',':)').replace(', ',':)').replace(' - ',':)'0)
print(new_string)


# In[7]:


string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
for i in string:
    if i == '.' or  i =='!' or  i =='?' or  i ==',' or  i =='-':
        string=string.replace(i,':)')
print(string)


# In[25]:


vowels =['а','о','и','е','ё','э', 'ы','у','ю','я']
consonants = ['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ']
name = 'Севастиан'
name_new =''
counter=0
for x in name:
    if x.lower() in vowels or x.lower() in consonants:
        name_new.join(x)
print({x:name[x] for x in range(0,len(name))})
    


# In[4]:


vowels =['а','о','и','е','ё','э', 'ы','у','ю','я']
consonants = ['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ']

name = 'Севастиан'
for x in name:
    if x in vowels:
        print("{} - гласная буква".format(x))
    elif x.lower() in consonants:
        print("{}-согласная буква".format(x))


# In[6]:


vowels =['а','о','и','е','ё','э', 'ы','у','ю','я']

name = 'Севастиан'
for x in name:
    if x in vowels:
        print("{} - гласная буква".format(x))
    else:
        print("{} - согласная буква".format(x))


# In[1]:


vowels =['а','о','и','е','ё','э', 'ы','у','ю','я']
name = str(input("Введите свое имя: "))
for x in name:
    if x.lower in vowels:
        print("{} - гласная буква".format(x))
    else:
        print("{} - согласная буква".format(x))

