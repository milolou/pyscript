# spreadsheetToText.py - copy the text in a spreadsheet into severals textfile.

import openpyxl

def fileMaker(spreadsheet):
    wb = openpyxl.load_workbook(spreadsheet)
    sheet = wb.active
    n = sheet.max_column
    for i in range(n):
        newText = open(f'text{i}.txt','w')
        textLine = []
        for cellObj in list(sheet.columns)[i]:
            textLine.append(cellObj.value)
        newTextLine = []
        for word in textLine:
            if word != None:
                newTextLine.append(word)
        textString = ''.join(newTextLine)
        newText.write(textString)
        newText.close()
    wb.close()

fileMaker('textSpreadsheet.xlsx')
