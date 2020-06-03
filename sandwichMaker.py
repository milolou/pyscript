# sandwichMaker.py - Let the user create a sandwich themself!

import pyinputplus as pyip

price = 0
breadType = {'wheat':1.99,'white':1.59,'wourdough':2.29}
proteinType ={'chicken':3.00,'turkey':3.49,'ham':2.49,'tofu':2.69}
cheeseType = {'cheddar':2.09,'swiss':2.30,'mozzarella':2.49}
additionalFood = {'mayo':1.89,'mustard':1.99,'lettuce':2.39,'tomato':2.00}

def sandwichMaker():
    promptOne = 'What kind of bread do you want?'
    promptTwo = 'What kind of protein do you want?'
    promptThree = 'What kind of cheese do you want?'
    promptFour = 'What kind of additional food do you want?'
    promptFive = 'Do you want a cheese?\n'
    promptSix = 'Do you want any additional food?\n'
    promptSeven = 'How many sandwiches do you want?\n'
    breadMenu = list(breadType.keys())
    proteinMenu = list(proteinType.keys())
    cheeseMenu = list(cheeseType.keys())
    additionalFoodMenu = list(additionalFood.keys())
    print(promptOne)
    bread = pyip.inputMenu(breadMenu,lettered=True)
    breadPrice = breadType[bread]
    print(promptTwo)
    protein = pyip.inputMenu(proteinMenu,lettered=True)
    proteinPrice = proteinType[protein]
    cheeseOrNot = pyip.inputYesNo(promptFive)
    cheesePrice = 0
    if cheeseOrNot == 'yes':
        print(promptThree)
        cheese = pyip.inputMenu(cheeseMenu,lettered=True)
        cheesePrice = cheeseType[cheese]
    additionalFoodOrNot = pyip.inputYesNo(promptSix)
    addedPrice = 0
    if additionalFoodOrNot == 'yes':
        print(promptFour)
        addedFood = pyip.inputMenu(additionalFoodMenu,lettered=True)
        addedPrice = additionalFood[addedFood]
    priceOfOneSandwich = breadPrice + proteinPrice + cheesePrice + addedPrice
    numOfSandwiches = pyip.inputInt(promptSeven,min=1)
    totalPrice = priceOfOneSandwich * numOfSandwiches
    print('The total price is %s$'%(totalPrice))

sandwichMaker()
