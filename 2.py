def aCalling(num):
    a = num + 1
    b = 1    
    for i in range(1,a):
        b = b*i
    print(b)
    return b


def sumOfOutput(number):
    f = 0
    for i in range(1,number):
        f = f+ aCalling(i)
    print(f)
    return f


def typeANumber(): 
    print('Please type an integer!')
    c = input()
    d = int(c)
    e = d + 1
    sumOfOutput(e)
  

typeANumber()

