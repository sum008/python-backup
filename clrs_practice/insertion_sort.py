# a=[5, 2, 4, 6, 1, 3,0,9,7,8]
# 
# for i in range(1,len(a)):
#     key = a[i]
#     j=i-1
#     while j>=0 and a[j]>key:
#         a[j+1]=a[j]
#         j=j-1
#         print(a)
#     a[j+1]=key
#     print(a,"--")    
# print(a)


def mergeSort(myList):
    if len(myList)>1:
        mid=len(myList)//2
        left=myList[:mid]
        right=myList[mid:]
        mergeSort(left) #left here is reference(not copy so any changes occur in left which is
#                         (as left will act as myList) the changes also reflect to left and
#                         these changes will also remain same for its previous stack--> 4681=46,81-->
#                         46, 18 (this 18 will remail same for its previous recursive call or previous stack))
        
        mergeSort(right) #same as above
        
        i=0
        j=0
        k=0
        print("----->",myList,left,right)
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                myList[k]=left[i]
                i+=1
            elif left[i]>right[j]:
                myList[k]=right[j]
                j+=1
            
            k+=1
    
        while i<len(left):
            myList[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            myList[k]=right[j]
            j+=1
            k+=1
            
    print("l",myList)

    

myList = [4,6,8,1,2,7,3,0]
mergeSort(myList)


        
        
