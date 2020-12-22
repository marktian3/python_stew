#regex version of strip method
#if no other arguement is passed other than string to strip, then whitespace will be removed from beginning and end of the string
#if other arguement is passed to the function, then it will be removed from the string
import re

def regexStrip(strings, toRemove = None):

    whitespaceRegex = re.compile(r'(\s)*(.*)(\s)$')
    removeRegex = re.compile(r'(%s)*' %toRemove)
    if toRemove == None:
        spaceStrip = whitespaceRegex.findall(strings)
        print(spaceStrip[0][1])
    else: 
        wordStrip = removeRegex.sub('', strings)
        print(wordStrip)

strings = ' hello my name is name mark '
#toRemove = 'name'
regexStrip(strings, toRemove)

 
