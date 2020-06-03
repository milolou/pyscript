from pathlib import Path
import re
p = Path(r'C:\Users\lou\Desktop\pyscript')
pattern = input()
compiledPattern = re.compile(pattern)
dirList = list(p.glob('*.txt'))
for txtFile in dirList:
    file = open(str(txtFile))
    stringList = file.readlines()
    for string in stringList:
        result = compiledPattern.findall(string)
        if result != None:
            print(string)
