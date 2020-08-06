import json
from difflib import get_close_matches

def word_dictionay():
    
    data = json.load(open("076 data.json"))
    word = input("Enter word : ").lower()
    
    if(word in data):
        print(data[word])
        
        
word_dictionay()