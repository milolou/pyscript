tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    colWidth = [0] * len(table)
    for x in range(0,len(table)):
        lengthOfString = []
        for y in range(0,len(table[x])):
            length = len(table[x][y])
            lengthOfString.append(length)
        l = lengthOfString[0]
        for z in range(1,len(lengthOfString)):
            if lengthOfString[z] > l:
                l = lengthOfString[z]
            else:
                continue
        colWidth[x] = l
    for m in range(0,len(table[0])):
        for n in range(0,len(table)):
            print(table[n][m].rjust((colWidth[n] + 2)),end = '')
        print()

    
printTable(tableData)
