'''
Program to confirm password is strong.
A strong password is: 
    - at least 8 char long
    - both upper and lower case characters
    - at least one digit
'''
# Import regex library
import re

def password_strong(password):
    upper = r'[A-Z]'
    lower = r'[a-z]'
    if re.search(upper, password) == None:
        print('Must include at least one uppercase letter.')
    elif re.search(lower, password) == None:
        print('Must include at least one lowercase letter.')
    elif len(password) < 8:
        print('Password must be at least 8 characters.')

password = input('Input your password: ')
password_strong(password)