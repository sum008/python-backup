t=int(input())
dic={"monday" : 1,"tuesday" : 2,"wednesday" : 3,"thursday" : 4,"friday" : 5,"saturday" : 6,"sunday" : 7}
for i in range(t):
        
    n=input().split(" ")
    s=dic[n[0]]
    e=dic[n[1]]
    l=int(n[2])
    r=int(n[3])
    count=0
    res=0
    if s>e:
        x=s-e
        x=7-x+1
    else:
        x=e-s+1
        
    while l>x:
        x+=7
      
    for i in range(l,r+1):
        if i==x:
            count+=1
            res=i
        if i>x:
            x+=7
    
              
    if count==1:
        print(res)
    elif count>1:
        print("many")
    elif count==0:
        print("impossible")
             
         



