from cmath import sqrt
a=6
b=-7
c=1
d=0
i=0
res=0

for i in range(1,10):
    res=a*pow(i,3)+b*pow(i,2)+c*i+d
    if res==0:
        break
    
if res!=0:
    for i in range(-10,0):
        res=a*(i**3)+b*(i**2)+c*i+d
        if res==0:
            break
    
print(i,res)    
res1=a
res2=res1*i+b
res3=res2*i+c

print(res1,res2,res3)

x=sqrt(res2*res2-4*res1*res3)
root2=(-res2+x)/(2*res1)
root3=(-res2-x)/(2*res1)

print("root1={0},root2={1},root3={2}".format(i,root2,root3))

