# pdfPasswordBreaker.py - unlock a pdf file whose password is a word.

import PyPDF2

def breaker(file):
    newFile = open(file,'rb')
    fileReader = PyPDF2.PdfFileReader(newFile)
    text = open('dictionary.txt')
    wordList = text.readlines()
    if not fileReader.isEncrypted:
        newFile.close()
    else:
        for word in wordList:
            password = word.strip()
            num = fileReader.decrypt(password)
            numl = fileReader.decrypt(password.lower())
            if num == 1 or numl == 1:
                if num == 1:
                    print(f'The real password is {password}.')
                    break
                else:
                    print(f'The real password is {password.lower()}.')
                    break
            elif num == 0 and numl == 0:
                continue
            else:
                print('Password was not found.')
            
breaker('nEncrypted.pdf')
