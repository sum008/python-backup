'''
Created on May 9, 2020

@author: Sumit
'''

import make_word as mw

w=mw.word()
play ="y"
board=[]
score=0
n=4
word=""
with open('english3.txt') as words:
         
    word=words.read()
word_array=word.split("\n")


for i in range(0,n):
    inner=[]
    for j in range(0,n):
        inner.append("0")
    board.append(inner)

def print_board(board):
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            print(board[i][j],end=" ")
        print()
    
while play=="y":
    print_board(board)
    pos=int(input("Your position? "))
    i=pos//len(board)
    j=pos%len(board)
    board[i][j]=input("Enter your character ")
    search=input("Do you want to search? y/n ")
    
    if search=="y":
        word=w.makeWord(i, j, board)
        word1=word[0]
        word2=word[1]
        
        if word1 in word_array:
            score+=1
            print("{} is present ".format(word1))
        elif word1[::-1] in word_array:
            score+=1
            print("{} is present ".format(word1[::-1]))
        if word2 in word_array:
            score+=1
            print("{} is present ".format(word2))
        elif word2[::-1] in word_array:
            score+=1
            print("{} is present ".format(word2[::-1]))
    search="n"
        
    play=input("Do you want to play again? y/n ")
    
    