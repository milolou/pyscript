# madLibs.py -- to substitute some words.

import re

def replaceKeywords(sentenceOne):
    newSentence = []
    for word in sentenceOne:
        if word == 'ADJECTIVE':
            newAdjective = input('Enter an adjective:\n')
            newSentence.append(newAdjective)
        elif word == 'NOUN':
            newNoun = input('Enter a noun:\n')
            newSentence.append(newNoun)
        elif word == 'ADVERB':
            newAdverb = input('Enter an adverb:\n')
            newSentence.append(newAdverb)
        elif word == 'VERB':
            newVerb = input('Enter a verb:\n')
            newSentence.append(newVerb)
        else:
            newSentence.append(word)
    return newSentence
            
def sentencePreProcess(sentenceTwo):
    period = re.compile(r'\.')
    comma = re.compile(',')
    newTextOne = period.sub(' .',sentenceTwo)
    newTextTwo = comma.sub(' ,',newTextOne)
    return newTextTwo

def sentenceEpiProcess(sentenceThree):
    perioda = re.compile(r' \.')
    commaa = re.compile(' ,')
    texta = perioda.sub('.',sentenceThree)
    textb = commaa.sub(',',texta)
    return textb

file = open('madLibsText.txt')
sentence = file.read()
print('Please substitute the ADJECTIVE\\NOUN\\ADVERB\\VERB appeared here:\n' + 
sentence)
textPre = sentencePreProcess(sentence)
textPreList = textPre.split()
replacedText = replaceKeywords(textPreList)
updatedText = ' '.join(replacedText)
finishedText = sentenceEpiProcess(updatedText)
print(finishedText)
newFile = open('replacedText.txt','w')
newFile.write(finishedText)
file.close()
newFile.close()
