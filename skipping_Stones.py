def solve(x1,y1,x2,y2):
    n1=0
    n2=0
    if x1>x2:
        n1=x1-x2+1
        n1-=2
    else:
        n1=x2-x1+1
        n1-=2
        
    if y1>y2:
        n2=y1-y2+1
        n2-=2
    else:
        n2=y2-y1+1
        n2-=2
    
    if n1>n2:
        return n2
    else:
        return n1
    
print(solve(21 ,-87 ,-81 ,-33))