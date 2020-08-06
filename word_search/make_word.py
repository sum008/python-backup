'''
Created on May 10, 2020

@author: Sumit
'''
class word:
    
    def makeWord(self,i,j,board):
        
        tempi=0
        
        #FOR VERTICAL
        if i!=0:
            for k in range(i,-1,-1):
                if board[k][j]=="0":
                    tempi=k+1
                    break
                else:
                    tempi=k
        
        word1=""    
        if i!=tempi:
            for k in range(tempi,len(board)):
                if board[k][j]!="0":
                    word1+=board[k][j]
                else:
                    break
        
        
        #FOR HORIZONTAL
        tempj=0
        word2=""
        if j!=0:
            for k in range(j,-1,-1):
                if board[i][k]=="0":
                    tempj=k+1
                    break
                else:
                    tempj=k
        if tempj!=j:
            for k in range(tempj,len(board)):
                if board[i][k]!="0":
                    word2+=board[i][k]
                else:
                    break  
            
        return [word1,word2]  
        