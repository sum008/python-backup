t=int(input())
for i in range(0,t):
    
    a = [int(x) for x in input().split()]
    n=int(a[0])
    k=int(a[1])
    a = [int(x) for x in input().split()]
    a.sort(key=None, reverse=True)
    qualifier_score=a[k-1]
    count=0
    for i in a:
        if i>=qualifier_score:
            count+=1
            
    print(count) 