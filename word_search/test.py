'''
Created on May 10, 2020

@author: Sumit
'''
word=""
with open('english3.txt') as words:
         
    word=words.read()
word=word.split("\n")  
print("poop" in word)