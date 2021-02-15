import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys()) [0])
        decide = input("press y for yess or n for no = ")
        if decide == "y":
            return data(get_close_matches(word, data.keys()) [0])
        elif decide == "n":
            return("please check the word and try again")
        else:
            return("you have entered the wrong input please enter y or n")
    else:
        print("please check the word and try again")

word = input("enter the word you want to search = ")
output = translate(word)
print(output)
