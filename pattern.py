def draw(n):
    count=0
    max1=0
    temp=0
    for i in range(1,2*n):
        for j in range(2*n-1,0,-1):
            
            if i<=2*n//2:
                if count<=max1:
                    print(str(n-count),end=" ")
                    temp=count
                    count+=1
                elif count>max1 and not count>j:
                    print(str(n-temp),end=" ")
                else :
                    temp-=1
                    print(str(n-temp),end=" ")
                
                    
            else:
                if count<=max1:
                    print(str(n-count),end=" ")
                    temp=count
                    count+=1
                elif count>max1 and not count>j:
                    print(str(n-temp),end=" ")
                else :
                    temp-=1
                    print(str(n-temp),end=" ")
                
        if i<2*n//2: max1+=1
        else: max1-=1
        count=0
        print()
        
        
draw(5)
                
                