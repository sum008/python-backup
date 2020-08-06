t=int(input())
for i in range(0,t):
    
    n=int(input())
    a = [int(x) for x in input().split()]
    count=0
    mx=0
    temp=""
    stk=[]
    a1=[]
    p=0
    for i in a:
        a1.append(i)
    while True:
        p+=1
        for i in a1:
            temp+=str(i)
        
        if not stk.__contains__(temp):
            stk.append(temp)
            if len(a)!=n:
                for i in a1:
                    a.append(i)
            for i in range(0,n,2):
                count+=abs(a[i]-a[i+1])
            
            if count>mx:
                mx=count
            
            count=0
            
            a1=[]    
            temp=""
            x=a.pop()
            a1.append(x)
            for i in a:
                temp+=str(i)
        
        else:
        
            temp=""
            if len(a)==0:
                break 
            x=a.pop()
            a1.append(x)
            for i in a:
                temp+=str(i)
    
    print(mx,p)
    print(stk)
        