def print_triangle(n):
    a=[]
    c=[]
    a.append(1)
    a.append(1)
    for i in range(n,-1,-1):
        for _ in range(1,i):
            print(" ",end=" ")
        if i<=n-2:
            if i!=0:
                print(" ",end=" ")
            print("1",end=" ")
            c.append(1)
            for k in range(0,len(a)-1):
                print(" ",end=" ")
                print(a[k]+a[k+1],end=" ")
                c.append(a[k]+a[k+1])
            print(" ",end=" ")
            print("1",end=" ")
            c.append(1) 
            a.clear()
            a=c.copy()
            c.clear()
        else:
            for _ in range(_,n):
                print(" ",end=" ")
                print(1,end=" ")
        print()
   
            
            
print_triangle(5)