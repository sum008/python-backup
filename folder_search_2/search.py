'''
Created on Jun 12, 2020

@author: Sumit
'''
import cur_folder as c
import os


directory="D:\\backup_sonam"
cur_directory=directory
prev_list=os.listdir(directory)
for i in range(0,len(prev_list)):
    prev_list[i]=directory+"\\"+prev_list[i]
# print(prev_list)
print("****************************************************************************************")
count=1
def folder(prev_list):
    for j in prev_list:
        try:
            if  len(os.listdir(j))!=0:
                l=os.listdir(j)
                for i in range(0,len(l)):
                    l[i]=j+"\\"+l[i]
                f=c.cur("cur",l)
                for x in l:
                    print(x)
                count+=1
                folder(f.get_folder_list())
            else:
                return
        except:
            continue
        
folder(prev_list)
print(count)