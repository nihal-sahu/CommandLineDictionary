import json
from difflib import get_close_matches

data = json.load(open("data.json"))
#dictionary data

def word_definition(user_input): #function used to grab definitions
    user_input = user_input.lower()
    
    if user_input in data: #if the user word is found in the data
        return data[user_input] 
    elif user_input.title() in data:
        return data[user_input.title()]
    elif user_input.upper() in data:
        return data[user_input.upper()]
    else: 
        similar_words = get_close_matches(user_input, data.keys(), n = 3, cutoff = 0.8) 

        if len(similar_words) > 0: #check for small spelling mistakes
            yn = input("Hmmmmmm... Did you mean %s instead? Enter Y for yes, N for no: " % similar_words[0])
            if yn.lower() == "y":
                return data[similar_words[0]]
            elif yn.lower == "n":
                return "This word doesnt exist. Please check your spelling and try again."
            else: 
                return "Not a valid input."
        else:    
            return "This word doesn't exist. Please check your spelling and try again."


while True: #user controlled loop
    word = input("Enter a word (type \"\end\" to quit): ") #user inputted string
    
    if word == r"\end":
        break

    output = word_definition(word)

    if isinstance(output, list):
        for definition in output:
            print(definition)
    else:
        print(output)
