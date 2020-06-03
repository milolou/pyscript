# PdfParanoia.py - Encrypt every PDF files in a folder and its subfolder,
# decrypt every PDF files in a folder and its subfolder.

import PyPDF2,os
from pathlib import Path

os.makedirs('encryptedPdfs',exist_ok=True)
# Encrypt every PDF files in a folder and its subfolder.
def encrypt(folder):
    absPath = os.path.abspath(folder)
    for folderName,subfolders,filenames in os.walk(absPath):
        for filename in filenames:
            if filename.endswith('.pdf'):
                try:
                    PdfFile = open(filename,'rb')
                    PdfReader = PyPDF2.PdfFileReader(PdfFile)
                    if not PdfReader.isEncrypted:
                        p = Path(filename)
                        PdfWriter = PyPDF2.PdfFileWriter()
                        for pageNum in range(PdfReader.numPages):
                            PdfWriter.addPage(PdfReader.getPage(pageNum))
                        PdfWriter.encrypt(p.stem)
                        resultPdf = open(os.path.join('encryptedPdfs',f'{p.stem}' + '_encrypted.pdf'),'wb')
                        PdfWriter.write(resultPdf)
                        resultPdf.close()
                        PdfFile.close()
                    elif PdfReader.isEncrypted:
                        PdfFile.close()
                except:
                    print(f'{filename} has some problems.')
'''
def test(folder):
    tabsPath = os.path.abspath(folder)
    for file in os.listdir(tabsPath):
        pa = Path(file)
        newFile = open(os.path.abspath(file),'rb')
        fileReader = PyPDF2.PdfFileReader(newFile)
        fileName = pa.stem
        l = len(fileName)
        password = fileName[:l-10]
        try:
            fileReader.decrypt(password)
            newFile.close()
        except:
            print('Wrong password!')

# Decrypt every PDF files in a folder and its subfolder.
def decrypt(folder):
    absPath = os.path.abspath(folder)
    for folderName,subfolders,filenames in os.walk(absPath):
        for filename in filenames:
            pdfFile = open(os.path.abspath(filename),'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if pdfReader.isEncrypted:
                pa = Path(file)
                fileName = pa.stem
                l = len(fileName)
                password = fileName[:l-10]
                pdfReader.decrypt(password)
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                resultFile = open(password + '.pdf','wb')
                pdfWriter.write(resultFile)
                resultFile.close()
                pdfFile.close()

'''
encrypt('Automate_the_Boring_Stuff_2e_onlinematerials')

