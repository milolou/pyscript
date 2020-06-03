import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]
rowCount = sheet.rowCount
for i in range(2,rowCount+1):
    row = sheet.getRow(i)
    if row == ['','','','','','']:
        break
    try:
        if int(row[0]) * int(row[1]) != int(row[2]):
            print(f'Error found,line {i}:{int(row[0])} * {int(row[1])} = {int(row[2])}')
    except:
        print(f'Error founded,line {i}:None value appeared.')
