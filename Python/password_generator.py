import random

a = int(input('''What do you want your password's length to be-> 8-16: '''))
strength = input('Which strength do you want-> Low, Medium or High?: ')
lowercase = ('abcdefghijklmnopqrstuvwxyz')
uppercase = lowercase.upper()
digits = ('0123456789')
symbols = ('''`~!@#$%^&*()-_=+[]{}\|;:'"<>,./?''')

password = ''

upper, lower, digi, symb = True, True, True, True

if strength == 'low' or 'Low' or 'LOW':
    if upper:
        password += uppercase
    if lower:
        password += lowercase

if strength == 'medium' or 'Medium' or 'MEDIUM':
    if upper:
        password += uppercase
    if lower:
        password += lowercase
    if digi:
        password += digits

if strength == 'high' or 'High' or 'HIGH':
    if upper:
        password += uppercase
    if lower:
        password += lowercase
    if digi:
        password += digits
    if symb:
        password += symbols

length = a

password_gen = ''.join(random.sample(password, length))
print("The password is:", password_gen)
