#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import openpyxl

# Import data locally
df = pd.read_csv('elections_gomoa_central.csv',header=0)
df.head()


# In[15]:


# NPP Wins in Polls
npp_wins = df.loc[(df['NPP'] > df['NDC'])].copy()
npp_wins


# In[16]:


# For NPP percentage wins
percent_npp_votes = (npp_wins['NPP']/npp_wins['Total valid votes'])*100
npp_wins['Percentage of votes'] = percent_npp_votes
npp_wins


# In[17]:


# Percentage win among total poll 
percent_poll_wins = (npp_wins.shape[0]/df.shape[0])*100
percent_poll_wins


# In[18]:


# Percentage of Registered Voters who did not vote for winning polls
reg_vote_not = ((npp_wins['Reg. votes'] - npp_wins['Total votes cast']) / npp_wins['Reg. votes'])*100
npp_wins['Percentage of non-voters'] = reg_vote_not
npp_wins


# In[19]:


# Percentage margin of winning over NDC
win_margin_percent = ((npp_wins['NPP'] - npp_wins['NDC'])/ npp_wins['Total valid votes'])*100
npp_wins['Percentage of win margin'] = win_margin_percent
npp_wins


# In[20]:


# NPP Losses in Polls
npp_losses = df.loc[(df['NPP'] < df['NDC'])].copy()
npp_losses


# In[21]:


# For NPP percentage losses
percent_npp_votes = (npp_losses['NPP']/npp_losses['Total valid votes'])*100
npp_losses['Percentage of votes'] = percent_npp_votes
npp_losses


# In[22]:


# Percentage of losses among total poll 
percent_poll_loss = (npp_losses.shape[0]/df.shape[0])*100
percent_poll_loss


# In[23]:


# Percentage of Registered Voters who did not vote for winning polls
reg_vote_not = ((npp_losses['Reg. votes'] - npp_losses['Total votes cast']) / npp_losses['Reg. votes'])*100
npp_losses['Percentage of non-voters'] = reg_vote_not
npp_losses


# In[24]:


# Percentage margin of loss over NDC
loss_margin_percent = ((npp_losses['NPP'] - npp_losses['NDC'])/ npp_losses['Total valid votes'])*100
npp_losses['Percentage of loss margin'] = loss_margin_percent
npp_losses


# In[25]:


# Saving cleaned to excel file
win_file_name = 'winselectionsdata.xlsx'
loss_file_name = 'losselectionsdata.xlsx'
npp_wins.to_excel(win_file_name)
npp_losses.to_excel(loss_file_name)


# In[ ]:




