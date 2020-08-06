print(7%9)
x=["s","d","g","y"]
current=[]
current+=x[0]
current+=x[1]
current+=x[2]
print(current)


t=int(input())
for _ in range(t):
    a=input()
    count=0
    ch=["c","e","f","h"]
    current=[]
    for i in range(0,len(a)-3):
        if a[i]=="c" or a[i]=="h" or a[i]=="e" or a[i]=="f":
            current+=a[i]
            if a[i+1]=="c" or a[i+1]=="h" or a[i+1]=="e" or a[i+1]=="f":
                current+=a[i+1]
                if a[i+2]=="c" or a[i+2]=="h" or a[i+2]=="e" or a[i+2]=="f":
                    current+=a[i+2]
                    if a[i+3]=="c" or a[i+3]=="h" or a[i+3]=="e" or a[i+3]=="f":
                        current+=a[i+3]
                        current.sort()
                        if current==ch:
                            count+=1
        current=[]
        
    if count==0:
        print("normal")
    else:
        print("lovely {}".format(count))
                    
                    