'''
Created on Jul 7, 2020

@author: Sumit
'''
class Bst():
    data=0
    left=None
    right=None
    
    def __init__(self,data):
        self.data=data
        
root=None
       
def insert(data):
    p=1
    global root
    if root==None:
        root=Bst(data)
    else:
        current=root
        prev=root
        while current!=None:
            
            prev=current
            if data<current.data:
                current=current.left
            else:
                current=current.right
        if data<prev.data:
            prev.left=Bst(data)
        else:
            prev.right=Bst(data)
            
def remove(data):
    current=root
    prev=root
    while not current.data==data:
        prev=current
        if data<current.data:
            current=current.left
        else:
            current=current.right
        
    if current.left!=None:
        x=current.left
        if prev.left!=None and prev.left.data==data:
            prev.left=x
        elif prev.right!=None and prev.right.data==data:
            prev.right=x
            
        if current.right!=None:
            y=current.right
            prev=x
            current=x.right
            while current!=None:
                prev=current
                current=current.right
            prev.right=y
            
    elif current.right!=None and current.left==None:
        
        x=current.right
        if prev.left!=None and prev.left.data==data:
            prev.left=x
        elif prev.right!=None and prev.right.data==data:
            prev.right=x
        
    elif current.left==None and current.right!=None:
        prev.right=current.right
    elif current.right==None and current.left!=None:
        prev.right=current.right
    elif current.left==None and current.right==None:
        current=None
        

def show():
    list=[root]
    for i in list:
        if i.left!=None:
            list.append(i.left)
        if i.right!=None:
            list.append(i.right)
        print(i.data)
        

insert(6)
insert(7)
insert(3)
insert(2.5)
insert(4)
insert(3.5)
insert(5)
insert(9)
insert(8)
show()
print()
remove(4)
show()
    