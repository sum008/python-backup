t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    a.append(0)
    a.append(1)
    for i in range(2,n):
        a.insert(i, (a[i-1]+a[i-2])%10)
        
    pos=0
    toggle=0
    while len(a)!=1:
        print(a)
        if toggle==0:
            if (pos%len(a))%2==0:
                a.pop(pos%len(a))
                toggle=1
        elif toggle==1:
            if (pos%len(a))%2!=0:
                a.pop(pos%len(a))
                toggle=0
        if pos==len(a):
            pos=0
            toggle=0
        else:
            pos+=1
    print(a)