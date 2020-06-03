# Strip function.

'''import re

print('You can strip some characters by strip method,\n
just put the characters you want to strip in the parenthese\n
followed function strip')
print('Please input the text you wanna strip.')
text = input()
print('Please use the strip function.')

def strip(string):
    preWhiteSpace = re.compile(r'^\s+')
    epiWhiteSpace = re.compile(r'\s+$')
    specificPattern = re.compile(r'%s'%string)
    if string == None:
        textOne = preWhiteSpace.sub('',text)
        textTwo = epiWhiteSpace.sub('',text)
        print('The stripped text is:\n' + textTwo)
        return textTwo
    else:
        textThree = specificPattern.sub('',text)
        print('The stripped text is:\n' + textThree)
        return textThree

# start the program.
functionCall = input()
n = len(functionCall)
if n > 7:
    stripString = functionCall[6:(n-1)]
elif n == 7:
    stripString = None
else:
    print('The input is not valid.')
strip(stripString)'''

import re

# Another version.
def strip(text,characters):
    preWhiteSpace = re.compile(r'^\s+')
    epiWhiteSpace = re.compile(r'\s+$')
    specificPattern = re.compile(r'%s'%characters)
    if characters == None:
        textOne = preWhiteSpace.sub('',text)
        textTwo = epiWhiteSpace.sub('',text)
        print('The stripped text is:\n' + textTwo)
        return textTwo
    else:
        textThree = specificPattern.sub('',text)
        print('The stripped text is:\n' + textThree)
        return textThree

# start the program.
print('please use the strip function.')
functionCall = input()
n = len(functionCall)
coreString = functionCall[7:(n-2)]
variableList = coreString.split("','")
newText = variableList[0]
newCharacters = variableList[1]
strip(newText,newCharacters)

