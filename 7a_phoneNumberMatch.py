#Checks if a phone number matches pattern of xxx-xxx-xxxx 

def isPhoneNumber(text):

  #checks overall length of number
  if len(text) != 12:
    return False


  for i in range(0,3):
    if not text[i].isdecimal():
      return False
  if text[3] != '-':
    return False
  for i in range(4,7):
    if not text[i].isdecimal():
      return False
  if text[7] != '-':
    return False
  for i in range(8, 11):
    if not text[i].isdecimal():
      return False
    else:
      return True

#Requests user input
print('Enter a phone number')
entry = input()
if isPhoneNumber(entry):
  print('Valid phone number')
else:
  print('Not a valid phone number')


#Checks a message input to see if any phone numbers are within message 
print('Enter a message that includes a phone number')
messageEntry = input()
#each loop takes 12 new characters from message input
for i in range(len(messageEntry)):
  chunk = messageEntry[i:i+12]
  if isPhoneNumber(chunk):
    print('Phone Number Found: ' + chunk)



#We can accomplish this faster using regular expressions:
import re

#phoneNumRegex will contain regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #/d for digit

testMessage = "Hi my number is 222-111-1231"

#we search regex object, returns either Match or None 
regSearch = phoneNumRegex.search(testMessage)
#we extract actual message using .group() method 
print('Phone number found: '+ regSearch.group())






  

