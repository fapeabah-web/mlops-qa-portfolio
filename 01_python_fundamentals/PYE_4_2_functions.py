# FUNCTIONS

# Ex 1. Introducing Arguments into Our Own Function

x = 5
print('Welcome, Brother')

def print_lyrics():
    print('I am a food scientist')
    print('I bring the good in food and make food good')

print("Who are you?")
print_lyrics()
x = (x - 0.06589) / 3.258
print('Sorghum concentration on my mind. The value is:' , x , 'mg/g GAE')
print("Oh wow, that's awesome; good to know")

# Ex 2. Introducing Arguments into Our Own Function with Variable "lang"

def greet(lang):
    if lang == 'es':
        return 'Holla'
    elif lang == 'fr':
        return 'Bonjour'
    elif lang == 'twi':
        return 'maakye'
    else:
        return 'Hello'


print(greet('en'),'Sally')
print(greet('es'),'Rodrigues')
print(greet('fr'),'Pierre')
print(greet('twi'),'Yaa')

# Ex 3. Introducing Arguments into Our Own Function with "Return"

greet('en')

def greet():
    return 'Hello'
print(greet(), 'Chaley')
