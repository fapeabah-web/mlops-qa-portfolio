#3.3 Write a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range, print an error. If the score is
#between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
#>= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable
# error message and exit. For the test, enter a score of 0.85.

score = input('Enter Score between 0.0 - 1.0: ')
try:
    score_grade = float(score)
except:
    score_grade > 1.0 or score_grade < 0.0
    
if score_grade >= 0.9 and score_grade <= 1.0:
    print('Your Grade is: A')
elif score_grade >= 0.8 and score_grade < 0.9:
    print('Your Grade is: B')
elif score_grade >= 0.7 and score_grade < 0.8:
    print('Your Grade is: C')
elif score_grade >= 0.6 and score_grade < 0.7:
    print('Your Grade is: D')
elif score_grade >= 0.0 and score_grade < 0.6:
    print('Your Grade is: F')
else:
    print('Wrong entry. Enter a decimal number between 0.0 and 1.0')
