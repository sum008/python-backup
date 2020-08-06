#CODE CHEF
x=[1 ,-3 ,2 ,-3]
x.sort()
print(x)
a=["h","f","e","c"]
a.sort()
p=["c","h","e","f"]
p.sort()
print(a==p)
t=int(input())
for _ in range(t):
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    c=[int(i) for i in input().split()]
    
    sm=0
    mid=0
    lg=0
    
    #for a
    if ((a[0]>=b[0] and a[1]>=b[1] and a[2]>b[2]) or (a[0]>b[0] and a[1]>=b[1] and a[2]>=b[2]) or (a[0]>=b[0] and a[1]>b[1] and a[2]>=b[2])) and ((a[0]>=c[0] and a[1]>=c[1] and a[2]>c[2]) or (a[0]>c[0] and a[1]>=c[1] and a[2]>=c[2]) or(a[0]>=c[0] and a[1]>c[1] and a[2]>=c[2])):
         
        lg+=1
         
    if ((a[0]<=b[0] and a[1]<=b[1] and a[2]<b[2]) or (a[0]<b[0] and a[1]<=b[1] and a[2]<=b[2]) or (a[0]<=b[0] and a[1]<b[1] and a[2]<=b[2])) and ((a[0]<=c[0] and a[1]<=c[1] and a[2]<c[2]) or (a[0]<c[0] and a[1]<=c[1] and a[2]<=c[2]) or(a[0]<=c[0] and a[1]<c[1] and a[2]<=c[2])):
        
        sm+=1
        
    if (((a[0]>=b[0] and a[1]>=b[1] and a[2]>b[2]) or (a[0]>b[0] and a[1]>=b[1] and a[2]>=b[2]) or (a[0]>=b[0] and a[1]>b[1] and a[2]>=b[2])) and ((a[0]<=c[0] and a[1]<=c[1] and a[2]<c[2]) or (a[0]<c[0] and a[1]<=c[1] and a[2]<=c[2]) or(a[0]<=c[0] and a[1]<c[1] and a[2]<=c[2]))) or (((a[0]>=c[0] and a[1]>=c[1] and a[2]>c[2]) or (a[0]>c[0] and a[1]>=c[1] and a[2]>=c[2]) or(a[0]>=c[0] and a[1]>c[1] and a[2]>=c[2])) and ((a[0]<=b[0] and a[1]<=b[1] and a[2]<b[2]) or (a[0]<b[0] and a[1]<=b[1] and a[2]<=b[2]) or (a[0]<=b[0] and a[1]<b[1] and a[2]<=b[2]))):
        
        mid+=1
        
        
    #for b
    
    if ((a[0]<=b[0] and a[1]<=b[1] and a[2]<b[2]) or (a[0]<b[0] and a[1]<=b[1] and a[2]<=b[2]) or (a[0]<=b[0] and a[1]<b[1] and a[2]<=b[2])) and ((b[0]>=c[0] and b[1]>=c[1] and b[2]>c[2]) or (b[0]>c[0] and b[1]>=c[1] and b[2]>=c[2]) or(b[0]>=c[0] and b[1]>c[1] and b[2]>=c[2])):
        lg+=1
        
    if ((a[0]>=b[0] and a[1]>=b[1] and a[2]>b[2]) or (a[0]>b[0] and a[1]>=b[1] and a[2]>=b[2]) or (a[0]>=b[0] and a[1]>b[1] and a[2]>=b[2])) and ((b[0]<=c[0] and b[1]<=c[1] and b[2]<c[2]) or (b[0]<c[0] and b[1]<=c[1] and b[2]<=c[2]) or(b[0]<=c[0] and b[1]<c[1] and b[2]<=c[2])):
        sm+=1
        
    if (((a[0]<=b[0] and a[1]<=b[1] and a[2]<b[2]) or (a[0]<b[0] and a[1]<=b[1] and a[2]<=b[2]) or (a[0]<=b[0] and a[1]<b[1] and a[2]<=b[2])) and ((b[0]<=c[0] and b[1]<=c[1] and b[2]<c[2]) or (b[0]<c[0] and b[1]<=c[1] and b[2]<=c[2]) or(b[0]<=c[0] and b[1]<c[1] and b[2]<=c[2]))) or (((b[0]>=c[0] and b[1]>=c[1] and b[2]>c[2]) or (b[0]>c[0] and b[1]>=c[1] and b[2]>=c[2]) or(b[0]>=c[0] and b[1]>c[1] and b[2]>=c[2])) and ((a[0]>=b[0] and a[1]>=b[1] and a[2]>b[2]) or (a[0]>b[0] and a[1]>=b[1] and a[2]>=b[2]) or (a[0]>=b[0] and a[1]>b[1] and a[2]>=b[2]))):
        mid+=1
        
    #for c
    
    if ((a[0]<=c[0] and a[1]<=c[1] and a[2]<c[2]) or (a[0]<c[0] and a[1]<=c[1] and a[2]<=c[2]) or (a[0]<=c[0] and a[1]<c[1] and a[2]<=c[2])) and ((b[0]<=c[0] and b[1]<=c[1] and b[2]<c[2]) or (b[0]<c[0] and b[1]<=c[1] and b[2]<=c[2]) or(b[0]<=c[0] and b[1]<c[1] and b[2]<=c[2])):
        lg+=1
        
    if ((a[0]>=c[0] and a[1]>=c[1] and a[2]>c[2]) or (a[0]>c[0] and a[1]>=c[1] and a[2]>=c[2]) or(a[0]>=c[0] and a[1]>c[1] and a[2]>=c[2])) and ((b[0]>=c[0] and b[1]>=c[1] and b[2]>c[2]) or (b[0]>c[0] and b[1]>=c[1] and b[2]>=c[2]) or(b[0]>=c[0] and b[1]>c[1] and b[2]>=c[2])):
        sm+=1
        
    if (( (a[0]<=c[0] and a[1]<=c[1] and a[2]<c[2]) or (a[0]<c[0] and a[1]<=c[1] and a[2]<=c[2]) or(a[0]<=c[0] and a[1]<c[1] and a[2]<=c[2])) and ((b[0]>=c[0] and b[1]>=c[1] and b[2]>c[2]) or (b[0]>c[0] and b[1]>=c[1] and b[2]>=c[2]) or(b[0]>=c[0] and b[1]>c[1] and b[2]>=c[2]))) or (((a[0]>=c[0] and a[1]>=c[1] and a[2]>c[2]) or (a[0]>c[0] and a[1]>=c[1] and a[2]>=c[2]) or(a[0]>=c[0] and a[1]>c[1] and a[2]>=c[2])) and ((b[0]<=c[0] and b[1]<=c[1] and b[2]<c[2]) or (b[0]<c[0] and b[1]<=c[1] and b[2]<=c[2]) or(b[0]<=c[0] and b[1]<c[1] and b[2]<=c[2]))):
        mid+=1
        
        
        
        
    if sm==1 and mid==1 and lg==1:
        print("yes")
    else:
        print("no")  