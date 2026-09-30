# FUNCTIONS

i = 42
type(i)
print(type(i))

# Ex 1. Function "thing()"
def thing():
    print('Hello')
    print('Fun')

thing()
print('zip')
thing()

# Ex 2. Function "max()" and "min()".
# Max = alphabet farthest from "A". lowercase > uppercase letters
# Max = since W is uppercase, max is "r"
# Min = "space" since " Hello" and "World" are separated by "space"
big = max('Hello World')
tiny = min('Hello World')
print(big, tiny)

# Ex 3. Function "conc_extract()"
def conc_extract():
    ab = input('Enter absorbance value: ')
    fab = float(ab)
    conc = (fab - 0.0657)/3.2295
    print('Concentration is:' , conc , 'mg/mL GAE')
    sample = input('Enter grams of sample extracted with 1 mL solvent: ')
    fsample = float(sample)
    tpc = conc / fsample
    print('TPC is:' , tpc , 'mg/g GAE')

conc_extract()

