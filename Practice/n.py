
t=int(input())
for i in range(0,t):
    n=int(input())
    a = [int(x) for x in input().split()]
    x=1
    pos=0
    while True:
        
        if (a[pos]+a[x])%2==0:
            y=(a[pos]+a[x])
            a.pop(x)
            a.pop(pos)
            a.insert(0, y)
            x=1
            pos=0
            print(a)
        elif x<len(a)-1:
            x+=1
        else:
            pos+=1
            x=pos+1
            
        if pos==len(a)-1:
            break
        
    print(len(a))
            



# t=int(input())
# for i in range(0,t):
#     
#     a = input().split(" ")
#     l = int(a[0])
#     r = int(a[1])
#     if l%2==0 and r%2==0:
#         y=r-l
#         if y%2==0:
#             print("Even")
#         else:
#             print("Odd")
#     elif (l%2==0 and r%2!=0) or (l%2!=0 and r%2==0) :
#         y=((r-l)+1)//2
#         if y%2==0:
#             print("Even")
#         else:
#             print("Odd")
#     else:
#         y=(((r-l)+1)//2)+1
#         if y%2==0:
#             print("Even")
#         else:
#             print("Odd")