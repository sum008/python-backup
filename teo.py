a=9898




def fib(n,count):
    print(a)
    if len(arr)>n:
        if arr[n]%2==0:
            count+=arr[n]
        return arr[n]
    else:
        
        if n<2:
            return n
        else:
            x=fib(n-1,count)+fib(n-2,count)
            arr.append(x)
            if x%2==0:
                count+=x
            return arr[n]

t = int(input())
arr=[]
count=0
for a0 in range(t):
    n = int(input().strip())
    arr.append(0)
    arr.append(1)
    fib(n,count)
    print(arr,count)
    arr.clear()
    count=0
    


