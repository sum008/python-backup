#----------------------CODE CHEF-->CHEF AND PAIR----------------------------------------

t=int(input())
while t>=1:
    a=[]
    count=0
    sum_=0
    x=0
    n=int(input())
    a = [int(x) for x in input().split()]
    a.append(0)
    toggle=0    
    for i in range(0,n+1):
        if a[i]%2==0 :
            x+=sum_*count
            sum_=0
            count+=1
        elif a[i]%2!=0:
            sum_+=1
    print(x)
    t-=1