#CODE CHEF

t=int(input())
for _ in range(t):
    x=input().split(" ")
    a=int(x[0])
    b=int(x[1])
    n=int(x[2])
    
    if n==0:
        print(0)
        
    elif a<0 and b>=0:
        if n%2==0:
            if abs(a)>b:
                print(1)
            elif b>abs(a):
                print(2)
            elif abs(a)==b:
                print(0)
        elif n%2!=0:
            print(2)
            
    elif a>=0 and b<0:
        if n%2==0:
            if abs(b)>a:
                print(2)
            elif a>abs(b):
                print(1)
            elif abs(b)==a:
                print(0)
        elif n%2!=0:
            print(1)
            
    elif a<0 and b<0:
        if n%2==0:
            if abs(a)>abs(b):
                print(1)
            elif abs(b)>abs(a):
                print(2)
            elif abs(a)==abs(b):
                print(0)
                
        else:
            if a>b:
                print(1)
            elif a<b:
                print(2) 
            elif a==b:
                print(0)
            
    elif a>b:
        print(1)
    elif b>a:
        print(2)
    else:
        print(0)
    