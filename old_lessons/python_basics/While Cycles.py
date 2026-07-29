#!/usr/bin/env python
# coding: utf-8

# In[1]:


attack = 80
current_health = 500
time = 0

while current_health>0:
    current_health = current_health - attack
    time += 1
else:
    print(time)


# In[2]:


balance = 10000
spent = 2800
count = 0
while balance > 0:
    print(balance)
    balance -= spent
else:
    print("Слишком большие расходы")




# In[3]:


count = 0
while (count < 9):

   print ('The count is:', count)
   count = count + 1
print ("Good bye!")


# In[2]:


volume = 1000
count = 0
step = 0
theSum = 0
while theSum < 1000:
    count +=1
    step +=5
    theSum+=step
    print(volume - theSum)
else:
    print(count)


# In[ ]:





# In[ ]:


theSum = 0
count


# In[ ]:





# In[ ]:


volume =1000
theSum=0
count=5
while volume > 0:
    print(volume -theSum)
    theSum +=count
    count+=5
else:
    print(theSum)

