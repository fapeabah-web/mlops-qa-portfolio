# Logical Operators
# BOOLEAN EXPRESSIONS
a = 1
b = 2
print(a > b)
print(not(a > b))

x = 12
print(x > 0 and x < 10)

x = 12
print(x > 0 or x < 10)

x = 12
print(not(x > 0 and x < 10))

print(17 and True)
print(17 and False)


# IF-ELSE Expressions

x = 12

if x > 0 and x < 10 :
    print('correct')
else:
    print('wrong')

n = 4
if n%2 == 0 or n%3 == 0:
    print('correct')
else:
    print('wrong')

m = 4
if m%2 == 0 and m%3 == 0:
    print('correct')
else:
    print('wrong')

p = 18
if p%2 == 0 and p%3 == 0:
    print('correct')
else:
    print('wrong')

x = 4**2 + 12 / 10 * 8
y = 2**4 + 12 / 8 * 10

if x == y:
    print("correct")
else:
    print('wrong')
print(x,y)

if not(x > y):
    print('yes')
else:
    print('no')

# IF-ELIF-ELSE EXPRESSIONS
x = input('Enter one letter of the alphabet to win a prize: ')
if x == 't':
    print('Good Guess! Pick up your price at the counter')
elif x == 'a':
    print('Not Quite')
else:
    print('Bad Guess! Sorry')
print('End of the Game :D')

y = input('Enter your exam score: ')
if float(y) >= 90:
    print('You had an A! Congratulations')
elif float(y) < 90 and float(y) >= 80:
     print('You had a B! Excellent')
elif float(y) < 80 and float(y) >= 70:
     print('You had a C! Good')
elif float(y) < 70 and float(y) >= 60:
     print('You had a D! Average')
elif float(y) < 60 and float(y) >= 50:
     print('You had an E! Below Average')
else:
     print('You had an F! Failed, Sorry')
print('Thanks for using the Grade Checker')

# CONVERT FAHRENHEIT TO CELSIUS TEMPERATURE
inp = input('Enter Temperaure in Fahrenheit: ')
fahr = float(inp)
cel = (fahr - 32) * 5 / 9
print('The temperature is', cel, 'oC')
