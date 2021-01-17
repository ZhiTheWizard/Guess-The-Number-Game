import random
import sys

print("Hello! What is your name?")
username = input()
        
print('What is up, {0}. \nI am think of a number between 1 and 10. \nCan you guess what it is?'.format(username))

randomnum = random.randint(1, 10) #creates random number between 1 and 10

for guesses in range(1, 6):
    guess = int(input())
    if guess > randomnum:
        print("Too High")
    elif guess < randomnum:
        print("Too Low")
    else:
        break #stops the loop when chosen the correct number

def round2():
    print("Don't think you are good. That was just the warm up " + username + ". Now to bring up the difficulty")
    print("I am thinking of a number between 1 and 30. Now let see if you can guess it")

    randomnum2 = random.randint(1, 30)

    for guesses2 in range(10):
        guess = int(input())

        if guess > randomnum2:
            print("Too high")
        elif guess < randomnum2:
            print("Too low")
        else: 
            break

    
    if guess == randomnum2:
        print("Wow, you got it correct and took only {0} tries. I apologize for my disrespectfulness your majesty".format(guesses2))
    else:
        print("I knew you were bad at this game. The number was " + str(randomnum2))
    
if guess == randomnum:
    print("correct, nice guess. You only took {0} guesses".format(guesses))
    round2()
else:
    print("You ran out of tries \nIt was {0}".format(randomnum))
