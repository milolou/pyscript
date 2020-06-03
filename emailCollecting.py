import ezsheets

email = []
ss = ezsheets.Spreadsheet('1Kf7i1vIrABltqtxEsUE-2hIi3dkgnHxMwvfM9RU69wM')
sheet = ss[0]
column = sheet.getColumn(3)
for i in column:
    if i != '' and i != '您的邮箱是？':
        email.append(i)
print(email)
