#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pyttsx3


# In[2]:


import pyttsx3


# In[9]:


comp = pyttsx3.init()

speech = input("reply   ")

comp.say("how are you Amal")

comp.say(speech)

comp.runAndWait()


# In[ ]:




