s="3943"
k=1

def make_palindrome(s,k):
    
    a=[int(i) for i in s]
    changes=0
    for i in range(0,len(a)//2):
        x=len(a)-i-1
        if a[i]!=a[x]:
            if a[i]==9 or a[x]==9:
                changes+=1
            else:
                changes+=2
        
        
    for i in range(0,len(a)//2):
        x=len(a)-i-1
        
        if k==0:
            break
        if a[i]!=a[x]:
            if a[i]>a[x]:
                if (k-2)>=(changes//2) and a[i]!=9:
                    a[x]=9
                    a[i]=9              #092282
                    k-=2
                    changes-=2
                else:
                    a[x]=a[i]
                    k-=1
                    changes-=1
            elif a[x]>a[i]:
                if (k-2)>=changes//2 and a[x]!=9:
                    a[x]=9
                    a[i]=9
                    k-=2
                    changes-=2
                else:
                    a[i]=a[x]
                    k-=1
                    changes-=1
        elif a[i]==a[x] and a[i]!=9:
            if (k-2)>changes//2:
                a[x]=9
                a[i]=9
                k-=2
            elif (k-2)==0 and (changes//2)==0:
                a[x]=9
                a[i]=9
                k-=2
    print(k,changes)
#     i=0            
#     while k>0:
#         x=x=len(a)-i-1
#         if a[i]!=9 or a[x]!=9:
#             a[i]=9
#             a[x]=9
#             if count==0:
#                 k-=2
#             else:
#                 k-=1
#         i+=1
        
    for i in range(0,len(a)//2):
        x=len(a)-i-1
        if a[i]!=a[x]:
            return -1
    s=""
    for i in a:
        s+=str(i)
    return s
    
    
print(make_palindrome("993399", 5))