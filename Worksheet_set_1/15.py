#!/usr/bin/env python
# coding: utf-8

# In[ ]:


str1=input("Enter the string ")
freq=[None]*len(str1)
for i in range(0,len(str1)):
  freq[i]=1
  for j in range(i+1,len(str1)):
    if(str1[i]==str1[j]):
        freq[i]=freq[i]+1
        str1=str1[:j]+'0'+str1[j+1:];
print("Character and its frequency");
for i in range(0,len(freq)):
    if(str1[i]!=' ' and str1[i]!='0'):
        print(str1[i]+"="+str(freq[i]))


# In[ ]:




