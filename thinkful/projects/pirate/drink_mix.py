import random


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

preferences = {}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

        

def bartender():
    """You tell me what you like, I make it!"""
    print("I'm a function. My name is {}".format(bartender.__name__))
    print("I'm a bit slow, I only accept yes or no answers")
    for k, v in questions.items():
        print (v)
        ans = input()
        if ans == "yes":
            preferences[k] = True
        if ans == "no":
            preferences[k] = False


def make_your_drink ():
    """I'll mix a tasty drink made especially for you"""
    print("let me mix up a nice tasty beverage for you now")
    drink = []
    for k, v in preferences.items():
        if v:
            drink.append(random.choice(ingredients[k]))
        
    return drink

if __name__ == '__main__':
    bartender()
    drink = make_your_drink()
    print (drink)

    
            

    
    

