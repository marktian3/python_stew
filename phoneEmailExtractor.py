#a program that searches text in clipboard for phone numbers and email addresses and replaces text 

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?  #area code 
(\s|-|\.)?          #separator
(\d{3})             #first 3 digits 
(\s|-|\.)?          #separator
(\d{4})             #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? #extension. the whole line is group #6, (ext|x|ext.) is group 7, and (\d{2,5}) is group 8. this is similar to how group 0 extends to the whole regex
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+  #username
@                  #@ symbol
[a-zA-Z0-9.-]+     #domain name
(\.[a-zA-Z]{2,4})  #dot something
)''', re.VERBOSE)

#find matches in clipboard
text = str(pyperclip.paste())
matches = []

#we want the phone numbers to be appeded as a single format
for groups in phoneRegex.findall(text):
  phoneNum = '-'.join([groups[1], groups[3], groups[5]])
  if groups[8] != '': #for the extension 
    phoneNum += ' x' + groups[8]
  matches.append(phoneNum)

for groups in emailRegex.findall(text):
  matches.append(groups[0])

#there is one tuple for each match, and each tuple contains strings for each group in the regex
#group[0] matches entire regex

#join matches into string for clipboard
if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print('The following emails and phone numbers were identified:')
  print('\n'.join(matches))
else:
  print('No phone numbers or email addresses found.')
