# Example 1. Loops and Iterations with Iterant or Iteration Variable "n"

n = 10
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
print(n)

n = 10
while n >= 0:
    print(n)
    n = n - 1
print('Blastoff')


# Example 2. Zero Trip. Similar to "IF" Statement.
n = 0
while n > 0:
    print('lather')
    print('rinse')
print('done with washing')

# Example 3. Infinite Loop
# n = 5
# while n > 0:
#    print('Lather')
#    print('Rinse')
# print('done with washing')


# Breaking Out of a Loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')


