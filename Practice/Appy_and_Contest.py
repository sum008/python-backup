t=int(input())
for i in range(0,t):
    
    p=input().split(" ")
    n=int(p[0])
    a=int(p[1])
    b=int(p[2])
    k=int(p[3])
    count1=0
    count2=0
    for i in range(2,n+1):
        if i%a==0 and i%b!=0:
            count1+=1
        elif i%b==0 and i%a!=0:
            count2+=1
            
    if count1+count2>=k:
        print("Win")
    else:
        print("Lose")