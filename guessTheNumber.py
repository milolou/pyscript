# Basic function
import random
def collatz(number):
   if number % 2 == 0:
       print(number // 2)
       return number // 2
   elif number % 2 == 1:
       print(3 * number + 1)
       return 3 * number + 1
# Ask the player to type a number calling the function until it returns 1
def aCalling():
   print('Type an integer you want , we will return you a 1 at last!')
   try:
       num = int(input())
       while num != 1:
           num = int(collatz(num))
   except ValueError:
           print('Invalid value')
      
aCalling()
