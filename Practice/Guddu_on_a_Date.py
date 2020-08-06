t=int(input())
while t>=1:
    n=input()
    sum_=0
    for i in n:
        sum_+=int(i)
        
    x=sum_%10
    x=10-x
    sum_=n+str(x%10)
    print(sum_)
#     if sum_>10:
#         x=sum_%10
#         x=10-x
#         sum_=n+str(x)
#         print(sum_)
#     else:
#         x=abs(10-sum_)
#         sum_=n+str(x)
#         print(sum_)
    t-=1
        
    
    