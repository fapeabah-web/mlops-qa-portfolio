fname = input('Enter your first name: ')
lname = input('Enter your last name: ')
print('Welcome, ' + fname + ' ' + lname)

country = input('Enter you country of origin: ')
city = input('Enter your home city: ')
prov_state = input('Enter your province or state: ')
pcode = input('Enter you post code or zip code: ')
print('Your permanent address is: ' + city + ', ' + prov_state + ', ' + pcode + ', ' + country)

rate_day = 109.99
day_stay = input('How many days will you be staying? Enter only number, e.g. 5: ')
price_net = float(rate_day) * float(day_stay)
tax_mb = 0.12 * float(price_net)
amt = price_net + tax_mb
print('Your fee for' , day_stay , 'days will be: $' , amt)
