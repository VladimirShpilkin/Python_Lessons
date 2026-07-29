#!/usr/bin/env python
# coding: utf-8

# In[1]:


phones = [['+79033923029', 'Мария Никитина'], ['+78125849204', 'Егор Савичев'], ['+79053049385', 'Александр Пахомов'], ['+79265748370', 'Алина Егорова'], ['+79030598495', 'Руслан Башаров']]
print(phones)


# In[29]:


employee_base = {'Мария Никитина':'+79033923029','Егор Савичев':'+78125849204', 'Александр Пахомов':'+79053049385', 'Алина Егорова':'+79265748370'}
print(employee_base)
print(employee_base['Алина Егорова'])


# In[34]:


draw_dict = {
    'Россия': 'A',
    'Португалия': 'B',
    'Франция': 'C',
    'Дания': 'C',
    'Египет': 'A'
}
print(draw_dict)


# In[86]:


draw_dict = {'Россия': 'A','Португалия': 'B','Франция': 'C','Дания': 'C','Египет': 'A'}
request ='Италия'
country = 'Италия'
if country in draw_dict:
    print(draw_dict[country])
else:
    print('unknown')


# In[96]:


draw_dict = {'Россия': 'A','Португалия': 'B','Франция': 'C','Дания': 'C','Египет': 'A'}
country_list ='Италия'
country = 'Италия'
for country in country_list:
    group = draw_dict.setdefault(country,'unknown')
    group=draw_dict[country]
print(group)
    


# In[1]:


draw_dict = {'Россия': 'A','Португалия': 'B','Франция': 'C','Дания': 'C','Египет': 'A'}
draw_new ={}
for country in draw_dict:
        if draw_dict[country]=='A':
            draw_new[country]=draw_dict[country]
print(draw_new)


# In[3]:


# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid','france': 'paris', 'germany':' berlin', 'norway': 'oslo' }

# Print europe
print(europe)


# In[9]:


# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())
print(europe['norway'])


# In[31]:


# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data ={'capital':'rome','population' :59.8}

# Add data to europe under key 'italy'

europe['italy'] = data
# Print europe
print(europe)


# In[33]:


# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany']='berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)


# In[35]:


# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy']='rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)


# In[37]:


Sample = {0: 10, 1: 20}
Sample[2] = 30
print(Sample)


# In[48]:


dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
new={**dic1,**dic2,**dic3}
print(new)


# In[52]:


Input = {'a': 100, 'b':200, 'c':300}
print('b' in Input)


# In[1]:


draw_dict = {'Россия': 'A','Португалия': 'B','Франция': 'C','Дания': 'C','Египет': 'A'}
draw_new={}
for country, position in draw_dict.items():
    if draw_dict[country] == 'A':
        draw_new[country] = draw_dict[country]
print(draw_new)


# In[8]:


save_spend = {'2019-04-01': 2504, '2019-04-02': 4994, '2019-04-03': 6343}
sum_spend = sum(save_spend.values())
print(sum_spend)


# In[12]:


phones = {'Гордиенко Виктория': 5140, 'Анисимов Кирилл': 5145,'Кузнецова Дарья': 5142}
for record in phones:
    if record == 'Кузнецова Дарья' and phones[record] == 5142:
        print('Номер верен')


# In[14]:


phones = {'Гордиенко Виктория': 5140, 'Анисимов Кирилл': 5145,'Кузнецова Дарья': 5142}
if phones['Кузнецова Дарья'] == 5142:
    print('Номер верен')


# In[16]:


for name, phone in phones.items():
    if name == 'Кузнецова Дарья' and phone == 5142:
        print('Номер верен')


# In[27]:


inventory = {'gold' : [500], 'pouch' : ['flint', 'twine', 'gemstone'], 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)


# In[1]:


inventory['backpack'] = ['xylophone','dagger', 'bedroll','bread loaf']


# In[10]:


csv_file = [
    ['100412', 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 9],
    ['100728', 'Скейтборд Jdbug RT03', 32],
    ['100732', 'Роллерсерф Razor RipStik Bright', 11],
    ['100803', 'Ботинки для сноуборда DC Tucknee', 20],
    ['100898', 'Шагомер Omron HJA-306', 2],
    ['100934', 'Пульсометр Beurer PM62', 17],
]
pulsometer_id=csv_file[5]
print(pulsometer_id)


# In[37]:


csv_file = [
    ['100412', 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 9],
    ['100728', 'Скейтборд Jdbug RT03', 32],
    ['100732', 'Роллерсерф Razor RipStik Bright', 11],
    ['100803', 'Ботинки для сноуборда DC Tucknee', 20],
    ['100898', 'Шагомер Omron HJA-306', 2],
    ['100934', 'Пульсометр Beurer PM62', 17],
]

for csv_file_filtered in csv_file:
    if csv_file_filtered[2] > 10:
        print('Количество', csv_filtered[1], 'на складе - {} штук'.format(csv_file_filtered[2]))
    
    


# In[56]:


csv_file = [
    ['100412', 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 9],
    ['100728', 'Скейтборд Jdbug RT03', 32],
    ['100732', 'Роллерсерф Razor RipStik Bright', 11],
    ['100803', 'Ботинки для сноуборда DC Tucknee', 20],
    ['100898', 'Шагомер Omron HJA-306', 2],
    ['100934', 'Пульсометр Beurer PM62', 17],
]
csv_file_filtered=[]

for record in csv_file:
    if record [2] > 10:
        csv_file_filtered.append(record)
print(csv_file_filtered)


# In[3]:


csv_dict = [
    {'id': '100412', 'position': 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 'count': 9},
    {'id': '100728', 'position': 'Скейтборд Jdbug RT03', 'count': 32},
    {'id': '100732', 'position': 'Роллерсерф Razor RipStik Bright', 'count': 11},
    {'id': '100803', 'position': 'Ботинки для сноуборда DC Tucknee', 'count': 20},
    {'id': '100898', 'position': 'Шагомер Omron HJA-306', 'count': 2},
    {'id': '100934', 'position': 'Пульсометр Beurer PM62', 'count': 17},
]

csv_dict_boots=list()

for record in csv_dict:
    if "Ботинки" in record['position']:
        csv_dict_boots.append(record)
print(csv_dict_boots)
    


# In[10]:


results = [
{'cost': 98, 'source': 'vk'}, {'cost': 153, 'source': 'yandex'}, {'cost': 110, 'source': 'facebook'}, ]

csv_dict = list()

for x in results:
    csv_dict.append(x['cost'])
print(csv_dict)
print(min(csv_dict))


    


# In[32]:


results = [
{'cost': 98, 'source': 'vk'}, {'cost': 153, 'source': 'yandex'}, {'cost': 110, 'source': 'facebook'}, ]

csv_dict = list()

for x in results:
    csv_dict.append(x['source'][])
print(csv_dict)
print(min(csv_dict))


# In[22]:


defect_stats = [
	{'step number': 1, 'damage': 0.98},
	{'step number': 2, 'damage': 0.99},
	{'step number': 3, 'damage': 0.99},
	{'step number': 4, 'damage': 0.96},
	{'step number': 5, 'damage': 0.97},
	{'step number': 6, 'damage': 0.97},
]

step=0
damage_rate=1

for i in defect_stats:
    damage_rate = damage_rate * i['damage']
    step +=1
    if damage_rate <0.9:
        print(step)
        break
        
        



    


# In[157]:


currency = {
	'AMD': {
		'Name': 'Армянских драмов',
		'Nominal': 100,
		'Value': 13.121
	},

	'AUD': {
		'Name': 'Австралийский доллар',
		'Nominal': 1,
		'Value': 45.5309
	},

	'INR': {
		'Name': 'Индийских рупий',
		'Nominal': 100,
		'Value': 92.9658
	},

	'MDL': {
		'Name': 'Молдавских леев',
		'Nominal': 10,
		'Value': 36.9305
	},
}
currency_rate = list()

for i in currency.values():

    rate = i['Value']/i['Nominal']
    currency_rate.append(rate)
print((currency_rate))
    
    
    


# In[29]:


bodycount = {
	'Проклятие Черной жемчужины': {
		'человек': 17
	}, 

	'Сундук мертвеца': {
		'человек': 56,
		'раков-отшельников': 1
	},

	'На краю света': {
		'человек': 88
	},

	'На странных берегах': {
		'человек': 56,
		'русалок': 2,
		'ядовитых жаб': 3,
		'пиратов зомби': 2
	}
}

sum1 = 0
result = {}

for key,value in bodycount.items():
   if value and 'человек' in value.keys():
    sum1+=value['человек']
print(sum1)
    


# In[36]:


bodycount = {
	'Проклятие Черной жемчужины': {
		'человек': 17
	}, 

	'Сундук мертвеца': {
		'человек': 56,
		'раков-отшельников': 1
	},

	'На краю света': {
		'человек': 88
	},

	'На странных берегах': {
		'человек': 56,
		'русалок': 2,
		'ядовитых жаб': 3,
		'пиратов зомби': 2
	}
}
sum1=0
for s in bodycount.values():
    sum1+=sum(s.values())
print(sum1)
    


# In[41]:


arrivals = {
	'Париж': {'время': '15:25', 'статус': 'ожидается', 'рейс': ['Аэрофлот']},
	'Пекин': {'время': '15:35', 'статус': 'опаздывает', 'рейс': ['China Southern Airlines', 'Россия']},
	'Лиссабон': {'время': '15:40', 'статус': 'ожидается', 'рейс': ['Nordwind', 'Аэрофлот']},
}

print(arrivals['Лиссабон']['время'])


# In[44]:


arrivals = {
	'Париж': {'время': '15:25', 'статус': 'ожидается', 'рейс': ['Аэрофлот']},
	'Пекин': {'время': '15:35', 'статус': 'опаздывает', 'рейс': ['China Southern Airlines', 'Россия']},
	'Лиссабон': {'время': '15:40', 'статус': 'ожидается', 'рейс': ['Nordwind', 'Аэрофлот']},
}

print(len(arrivals['Пекин']['рейс']))


# In[45]:


import json
with 

