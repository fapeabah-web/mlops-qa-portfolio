# 3.2 Re-write your pay program using try and except so that your program  
# handles non-numeric input gracefully by printing a message and exiting
# the program. The following shows two executions of the program
# Enter Hours: 20
# Enter rate: nine
# Error, please enter numberic input

# Enter Hours: forty
# Error, please enter numberic input

hr = input('Enter the hours: ')
rt = input("Enter the rate: ")
try:
    fhr = float(hr)
    frt = float(rt)
except:
    print('Error, please enter numberic input')
    quit()
    
reg = fhr * frt
if fhr > 40:
    print('Overtime')
    otp = (fhr - 40) * 1.5 * frt
    xp = reg + otp

else:
    print('Regular')
    xp = reg
print('Pay is:', xp)
