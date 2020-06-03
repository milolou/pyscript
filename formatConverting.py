import ezsheets

def formatConverting(fileOne,fileTwo):
    ss = ezsheets.upload(fileOne)
    ss.downloadAsExcel(fileTwo)
