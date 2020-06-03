# Strong password detection.

import re

def checkingMethod():
    print('''
    Input a password,we'll check if it's strong enough.
    please make sure your password is at least eight characters long
    and contains at least one character for lowercase letter,
    uppercase letter and number separately.
    ''')
    a_zPattern = re.compile(r'[a-z]')
    A_ZPattern = re.compile(r'[A-Z]')
    numPattern = re.compile(r'[0-9]')
    password = input()
    a_zMatch = a_zPattern.search(password)
    A_ZMatch = A_ZPattern.search(password)
    numMatch = numPattern.search(password)
    if len(password) < 8:
        print('The password you input is less than eight characters.')
    elif a_zMatch == None:
        print('The password you input contains no lowercase letters.')
    elif A_ZMatch == None:
        print('The password you input contains no uppercase letters.')
    elif numMatch == None:
        print('The password you input contains no numbers.')
    else:
        print('The password you input is strong.')

checkingMethod()
    
