st="sumit"
list1=[]

print(list1)
a=[4,5,6]
print(a.index(6))
a[0]=9
print(a)
t=int(input())
for _ in range(t):
    a=input().split(" ")
    n=int(a[0])
    k=int(a[1])
    s=int(a[2])
    d=n//k
    sun=7
    i=d
    if d==0:
        print(-1)
    else:
        for i in range(d,s+1,d):
            if i>sun:
                sun+=7
                
            if (i+1)%7==0:
                break
        print(i)    
        if i==s:
            print(s%d)
        
        elif (i+1)==sun:
            if i==s:
                print(s%d)
            elif i+1==s:
                print(-1)
            else:
                print(-1)
                
        elif (i+1)<sun:
            if s<sun:
                print(s%d)
            
            
   
    
    