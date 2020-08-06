t=int(input())
for i in range(0,t):
    
    p=input().split(" ")
    n=int(p[0])
    k=int(p[1])
    a=[int(x) for x in input().split()]
    a.sort()
    boundary_value_k=a[k-1] #k-1 because indexing starts form 0
    r=0
    n1=0
    result=1
    for i in range(0,n):
        if i<k and a[i]==boundary_value_k:
            n1+=1
            r+=1
        elif i>=k and a[i]==boundary_value_k:
            n1+=1
    if n1==0:
        print(result)
    else:        
        for i in range(1,r+1):
            result=(result*(n1+1-i))//i
        print(result)