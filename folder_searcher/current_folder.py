'''
Created on Jun 12, 2020

@author: Sumit
'''
import os

curr_dir='D:\\backup_sonam'
list_dir=os.listdir(curr_dir)
for i in range(0,len(list_dir)):
    list_dir[i]=curr_dir+"\\"+list_dir[i]
c=[]
# print(list_dir)
for i in list_dir:
    try:
        l=os.listdir(i)
        for j in range(0,len(l)):
            l[j]=i+"\\"+l[j]
        list_dir.extend(l)
    except:
        continue
    
print(len(list_dir))
for i in list_dir:
    print(i)
    