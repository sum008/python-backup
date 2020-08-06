def shift(s,a):
    count=0
    s1=""
    for i in a:
        if i[0]==0:
            count-=i[1]
        else:
            count+=i[1]
    if count<0:
        start=abs(count)%len(s)
        for i in range(start,len(s)+start):
            s1+=s[i%len(s)]
    else:
        start=abs(len(s)-count)
        for i in range(start,len(s)+start):
            s1+=s[i%len(s)]
            
    return s1

s="abc"
a=[[0,1],[0,1],[1,2],[1,7]]
print(shift(s, a))
print(chr(122))