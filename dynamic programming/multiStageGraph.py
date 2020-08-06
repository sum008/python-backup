'''
Created on May 14, 2020

@author: Sumit
'''
c=[[0,0,0,0,0,0,0,0,0],
   [0,0,2,1,3,0,0,0,0],
   [0,0,0,0,0,2,3,0,0],
   [0,0,0,0,0,6,7,0,0],
   [0,0,0,0,0,6,8,9,0],
   [0,0,0,0,0,0,0,0,6],
   [0,0,0,0,0,0,0,0,4],
   [0,0,0,0,0,0,0,0,5],
   [0,0,0,0,0,0,0,0,0]]

n=9
path=[-1]*n
cost=[-1]*n
cost[n-1]=0
p=[-1]*(n//2)
for i in range(n-2,0,-1):
    m=99999
    for j in range(i+1,n):
        if c[i][j]!=0 and c[i][j]+cost[j]<m:
            m=c[i][j]+cost[j]
            path[i]=j
    cost[i]=m
p[0]=1
p[n//2-1]=n-1

for i in range(1,n//2-1):
    p[i]=path[p[i-1]]
print(cost)
print(path)
print(p)