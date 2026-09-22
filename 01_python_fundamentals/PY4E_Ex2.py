print(38.6 * 498.3)
x = 38.6
y = 498.3
print(x * y)
print(x / y)
print(y / x)
print(y % x)
print(12 * x)
z = 12 * x
print(y - z)
a = 12
a = a * 46.3
print(a)
print(int(a))
hours = 12
rate = 20.95
pay = hours * rate
print(pay)
print(int(pay))
week1 = hours * 4
week2 = hours * 3
biweekly = week1 + week2
print(biweekly)
biweekly_pay = biweekly * rate
print(biweekly_pay)
income_tax = 0.108
tax_amount = biweekly_pay * income_tax
print(tax_amount)
cpp_levy = 0.0595
ei_levy = 0.0163
union_dues = 0.02
gp_insurance = 90
deductions = (biweekly_pay * cpp_levy) + (biweekly_pay * ei_levy) + (biweekly_pay * union_dues) + gp_insurance + tax_amount
net_pay = biweekly_pay - deductions
print(net_pay)
print(int(net_pay))
x = 0.6
x = 3.9 * x * (1- x)
print(x)
print(int(x))
x=1+2**3/4*5
print(x)
print(int(x))
y = 1 + 4
print(y)
y = 1 * 4
print(y)
y = 16 * 4
print(y)
y = 16 / 4
print(y)
eee = 'Hello' + 'there'
print(eee)
eee = 'Hello' + ' ' + 'there'
print(eee)
print(eee + ' ' + str(1))
print(type(eee)) # "Types of variables: str, int, float"
print(type(y))
print(type(x))
print(type(pay))
print(99 + 100)
print(float(99) + 100)
zzz = '99 + 100'
print(zzz + ' ' + '+' + str(101))
print(zzz + ' ' + '+' + ' ' + str(101))
zzz = int('99')
print(type(zzz))
print(zzz + 100)
y = zzz + 100 / 12
print(type(y))
print(y)

# Input - Prompt the user for information and registration
name1 = input("Please enter your name: ")   
print("Welcome, " + name1)                  
origin1 = input("Country of origin: ")
print("Great to know you're from " + origin1)
City1 = input("City of residence: ")
province1 = input("Province of residence: ")
postcode1 = input("Postal code: ")
print("Your address is: " + City1 + ", " + province1 + ", " + postcode1)
days1 = input("How many days will you be staying? A day is $100.00. Please enter the number of days: ")
paymt1 = input("Please enter your visa card number and follow the prompts to make payment: ")
when_done = input("Press Enter to complete the order.")
print("Thank you for your order. You'll receive a confirmation email shortly.")

# Input - Convert European floor number to US floor number
inp = input("Europe floor number: ")
usf = int(inp) + 1
print("US floor number: ", str(usf))

# 2.2 Write a code that prompts a user for their name and welcomes them. 
# Note that input will pop up a dialog box. 
# Enter Sarah when prompted so your output will match the desired output.
# Desired Output: Hello Sarah
name2 = input("Please enter your name: ")
print('Hello', name2)

# 2.3 Write a program to prompt a user for hours and rate per hour using input to compute gross pay. 
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking or bad user data.
hours = float(input("Please enter the number of hours worked: "))
rate = float(input("Please enter the hourly rate: "))
gross_pay = hours * rate
print("Gross pay:", gross_pay)

# Alternative to nesting input and float() functions:
hours1 = input("Enter the number of hours worked: ")
rate1 = input("Enter the rate/hour based on your role: ")
gross_pay1 = float(hours1) * float(rate1)
print("pay:", gross_pay1)
x = 1 + 2 * 3 - 8 / 4
print(x)