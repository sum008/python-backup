
def displayPathtoPrincess(m,grid):
    mi=0
    mj=0
    pi=0
    pj=0
    for i in range(0,m):
        for j in range(0,m):
            if grid[i][j]=="m":
                mi=i
                mj=j
            elif grid[i][j]=="p":
                pi=i
                pj=j
                            
    if (mi<pi and mj>pj):
        
        while mi!=pi or mj!=pj:
            if mi!=pi:
                mi+=1
                print("DOWN")
            if mi==pi and mj!=pj:
                mj-=1
                print("LEFT")
    
    elif (mi<pi and mj<pj):
        
        while mi!=pi or mj!=pj:
            if mi!=pi:
                mi+=1
                print("DOWN")
            if mi==pi and mj!=pj:
                mj+=1
                print("RIGHT")
                
    elif (mi>pi and mj>pj):
        
        while mi!=pi or mj!=pj:
            if mi!=pi:
                mi-=1
                print("UP")
            if mi==pi and mj!=pj:
                mj-=1
                print("LEFT")
                
    elif (mi>pi and mj<pj):
        
        while mi!=pi or mj!=pj:
            if mi!=pi:
                mi-=1
                print("UP")
            if mi==pi and mj!=pj:
                mj+=1
                print("RIGHT")
                
    elif (mi>pi and mj==pj):
        
        while mi!=pi:
            mi-=1
            print("UP")
            
    elif (mi<pi and mj==pj):
        
        while mi!=pi:
            mi+=1
            print("DOWN")
            
    elif (mi==pi and mj<pj):
        
        while mj!=pj:
            mj+=1
            print("RIGHT")
            
    elif (mi==pi and mj>pj):
        
        while mj!=pj:
            mj-=1
            print("LEFT")
            
                

grid=[["-","-","-"],
      ["-","-","-"],
      ["p","-","m"]]
m=3
displayPathtoPrincess(m,grid)
