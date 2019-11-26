#!/usr/bin/env python
# coding: utf-8

# # FATIMA MUNIR 
# 19B-143-SE
# # practice problem chap no:02
# 

# In[4]:


a=3*'A'
print (a)


# In[6]:


s='hello'
'h' in s
'g' in s


# In[2]:


s1='ant'
s2='bat'
s3='cod'
a=s1+''+s2+''+s3
b=a*5
print (b)


# In[9]:


a=s1*10
print(a)


# In[10]:


s='0123456789'
s[0],s[1],s[5],s[7],s[8]


# In[13]:


pets=['cat','dog','horse','parrot']
a=pets+pets
print(a)
'rabbit' in pets


# # Exercises

# # 2.11

# In[18]:


a=(-7)+(-1)
print(a)


# In[20]:


a=9
b=10
c=11
d=12
avg=(a+b+c+d)/5
print(avg)


# In[22]:


a=2**-20
print(a)


# In[26]:


a=61//4356
print(a)


# In[27]:


a=4356%61
print(a)


# # 2.12

# In[29]:


s1='-'
s2='+'
print(s1+s2)


# In[31]:


print(s1+s2+s1)


# In[33]:


print(s2+s1+s1)


# In[34]:


print(s2+s1+s1+s2+s1+s1)


# In[35]:


a=s2+s1+s1
print(a*10)


# In[36]:


a=s2+s1+s2*3+s1*2
print(a*5)


# # 2.13

# In[37]:


a='abcdefghijklmnopqurstuvwxyz'
a[-1],a[-2],a[-11]


# # 2.14

# In[41]:


s='goodbye'
s[0]=='g'


# In[42]:


s[6]=='g'


# In[44]:


s[0]=='g'and s[1]==a


# In[45]:


s[-2]=='x'


# In[53]:


a=int(len(s)/2)
s[a]=='d'


# In[52]:


(s[-1],s[-2],s[-3],s[-4])=='tion'


# # 2.15

# In[54]:


a='anachronistically'
b='counterintuitive'
if len(a)>len(b):
    print(a)
else:
    print(b)


# In[60]:


a=['misrepresentation','misinterpretation']
a.sort()
print(a)


# In[66]:


a='floccinaucinihilipilification'
if 'e'==a:
    print("e does  appear in word")
else:
    print("'e' does not appear in word")


# In[69]:


a='counterrevolution'
x='counter'
x2='revolution'
b=len(a)==(len(x)+len(x2))
print (b)


# # 2.16

# In[1]:


a=6
b=7
c=(a+b)/2
print(c)


# In[3]:


lst=['paper','staples','penciles']
print(lst)


# In[14]:


first='john'
middle='fitzgerald'
last='kenedy'
name=(first+" "+middle+' '+last)
print("name: ",lst2)


# # 2.17

# In[10]:


a=17
b=-9
sum=a+b
if sum<10:
    print("The sum is less than 10")
else:
    print("The sum is greater than 10")


# In[19]:


a=(len(lst)*5)==len(name)
print(a)


# In[20]:


avg=(a+b)/2==6.75
print(avg)


# In[21]:


length=len(last)>(len(middle))>(len(first))
print(length)


# In[22]:


a=len(lst)>10 and len(lst)==0
print(a)


# # 2.18

# In[1]:


flower=['rose','bougainvillea','yucca','marigold','daylilly','lilly of the valley']
'potato' in flower


# In[2]:


thorny=[]
thorny=flower[:3]
print(thorny)


# # 2.19

# In[4]:


answers=['Y','N','Y','N','N','N','Y','Y','Y']
answers.count('Y')


# In[5]:


answers.count('N')


# In[11]:


answers.sort()
print (answers)


# In[ ]:




