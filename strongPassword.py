#function that uses regular expressions to make sure password string it is passed is strong
#(does not support special characters)

#Strong password: at least 8 characters, contains both upper and lower case, and at least 1 digit
import re
def strongPassword(password):
    sortedPassword = ''.join(sorted(password)) #a sorted password will be in the order of numbers, then capitals, then smaller characters
    passRegex = re.compile(r'\d+[A-Z]+[a-z]+') #since we sort the password we don't need a complex regex

    if (len(sortedPassword) >= 8) and (bool(passRegex.search(sortedPassword))):
        print('This is a strong password!')
    else:
        print('This is a weak password')


print('Please enter a password (not your actual password)')
passIn = input()
strongPassword(passIn)
