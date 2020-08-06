t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x=(n-1)//15
    if x==1:
        x=15
    else:
        x=((30+(x-1)*15)*x)//2
        
    sum_=(((2*3+(((n-1)//3)-1)*3)*((n-1)//3))//2)+(((2*5+(((n-1)//5)-1)*5)*((n-1)//5))//2) -x
    print(sum_)