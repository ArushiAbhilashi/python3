#!/usr/bin/env python
# coding: utf-8

# # calculating sum of n numbers using while loop

# In[5]:


n=int(input("ENTER THE NUMBER UPTO WHICH SUM HAS TO BE CALCULATED: "))
sum=0
i=0
while(i<n):
    i=i+1
    sum=sum+i
    
print(sum)


# # checking whether a number is prime or not

# In[15]:


x=int(input("ENTER A NUMBER:"))
for i in range(2,x):
    if(x%i==0):
       print(x," is not a prime number")
       break
else:
    print(x," is a prime number")
    

