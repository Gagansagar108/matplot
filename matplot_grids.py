#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


ax=plt.subplot2grid((2,2),(0,0))


# In[38]:


plt.figure(figsize=(10,10))
plt.subplot(4,2,1)   #three rows and 2 coloumns , 1st fig
plt.subplot(4,2,2)
plt.subplot(4,2,6)
plt.subplot(4,2,8)


# In[40]:


ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)


# In[48]:


plt.figure(1)
ax1=plt.subplot2grid((3,3),(0,0),colspan=2)
ax2=plt.subplot2grid((3,3),(1,2),rowspan=2)
ax3=plt.subplot2grid((3,3),(2,0))


# In[54]:


import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(4, 4)   #width_ratios=[1, 2], height_ratios=[4, 1]
#gs.update(left=0.05, right=0.48, wspace=0.05)

ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[1, :-1])


# In[69]:


gs = gridspec.GridSpec(3, 3,wspace=.4)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, :-1])
ax3 = plt.subplot(gs[1:, -1])
ax4 = plt.subplot(gs[-1, 0])
ax5 = plt.subplot(gs[-1, -2])


# In[65]:


gs = gridspec.GridSpec(3, 3,right=2,wspace=1)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, :-1])
ax3 = plt.subplot(gs[1:, -1])
ax4 = plt.subplot(gs[-1, 0])
ax5 = plt.subplot(gs[-1, -2])


# In[ ]:




