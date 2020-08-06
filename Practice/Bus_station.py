n=8
a=[1 ,2 ,1 ,1 ,1 ,2 ,1 ,3]
k=0
b=[]
count=0
for i in range(1,sum(a)+1):
    k=0
    count=0
    for x in range(0,len(a)):
        k+=1
        if i >=a[x]:
            count+=a[x]
           
            if count==i:
                count=0
            elif count>i:
                break
        else:
            break
    if (x+1)==len(a) and count==0:
        b.append(i)    
print(b)