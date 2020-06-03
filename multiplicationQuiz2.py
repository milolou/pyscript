# multiplicationQuiz2.py

import random,time

def multiplicationQuiz():
    numOfQuestions = 10
    correctAnswers = 0
    for i in range(numOfQuestions):
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        startTime = time.time()
        for i in range(4):
            print('#%s: %s x %s = ' % (i, num1, num2),end='')
            if i == 4:
                print('Incorrect!')
                break
            if time.time() - startTime > 8:
                print('Incorrect!')
                break
            answer = input()
            if time.time() - startTime > 8:
                print('Incorrect!')
                break
            if answer == str(num1 * num2):
                print('correct!')
                correctAnswers += 1
                break
            if time.time() - startTime > 8:
                print('Incorrect!')
                break
            else:
                print('Incorrect!')
    print('Score: %s / %s' % (correctAnswers, numOfQuestions))
            
multiplicationQuiz()

        
