print(1%10)
t=int(input())

while t>=1:
    
    nk=input().split(" ")
    n=int(nk[0])
    k=int(nk[1])
    print(k%n)
    if n==k:
        print("YES")
        
    elif n>k:
        x=n//k
        if x%k==0:
            print("NO")
        else:
            print("YES")
    t-=1
    
            