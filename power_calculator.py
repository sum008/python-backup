def power(x,y):
    
    if y==0:
        return 1
    else:
        
        count=2
        result=x
        p=0
        q=x
        while count<=y:
            p=0
            for i in range(0,x):
                if p==0:
                    result=result+p
                    p=q
                else:
                    result+=p
            q=result
            count+=1
        return result
    
def armstrong(x):
    y=x
    x=str(x)
    res=0
    for i in x:
        res+=int(i)**len(x)
    print(y==res,res)
    
print(power(4,4))
armstrong(163)
    