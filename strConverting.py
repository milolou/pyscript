def strVersionOfList(aList):
    a = len(aList)
    b = a - 1
    c = aList[0]
    for i in range(1,b):
        c = c + ',' + ' ' + aList[i]
    c = c + ',' + ' ' + 'and' + ' '  + aList[b]
    print(c)
    return c

def pasreList(alist):
    L = []
    for i in range(0, len(alist)):
        s = alist[i]
        s = s[1:(len(s)-1)]
        L.append(s)
    return L

def makeACalling():
    print('please input a list , we will give you a string in a form back !')
    #firstStr = input()
    firstStr = "['apples','bananas','tofu','cats']"
    length = len(firstStr)
    aNum = length - 2
    newStr = firstStr[2:aNum]
    newList = newStr.split("','")
    print(newList)
   # aL = pasreList(newList)
  #  print(aL)
    strVersionOfList(newList)

makeACalling()
