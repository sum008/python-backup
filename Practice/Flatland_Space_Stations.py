# a = open("C:\\Users\\Sumit\\Desktop\\input15.txt","r")
# con = a.read()
# b=list(con.split(" "))
# c=[]
# for i in b:
#     c.append(int(i))
# 
# c.sort(reverse=False)   
# print(c)
c=[93 ,41 ,91 ,61 ,30 ,6 ,25 ,90 ,97]
c.sort(reverse=False)
print(c)
count=0
n=100
max_=0
x=0
temp=0
pos=0
prev=abs(0-c[temp])
for i in range(1,n):
    
    if i<len(c):
        
        if abs(i-c[temp]) <= abs(i-c[i]):
            
            x=abs(i-c[temp])
        else:
            x=abs(i-c[i%len(c)])
            temp+=1
        
        pos=i
    else:
        if abs(i-c[temp]) <= abs(i-c[i%len(c)]):
            x=abs(i-c[temp])
        else:
            x=abs(i-c[i%len(c)])
            if temp<len(c)-1:
                temp+=1
    print("uuuuuuuuuuuuuuuu ",x,i, i%len(c),temp)
    
    
    if x>max_:
        max_= x

print( max_ )