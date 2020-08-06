t=int(input())
for i in range(t):
    
    d=input()
    print(d[len(d)-2])
    n=0
    for i in range(0,len(d)):
        if d[i]=="P":
            n+=1
            
    if n/len(d)>=0.75:
        print(-1)
    else:
        count=0        
        for i in range(2,len(d)-2):
            if d[i]=="A" and ((d[i-1]=="P" or d[i-2]=="P") and (d[i+1]=="P" or d[i+2]=="P")): 
                n+=1
                count+=1
                if n/len(d)>=0.75:
                    break;
                
        if count==0:
            print(-1)
        else:
            print(count)
