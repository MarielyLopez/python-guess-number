# Aqui escribe tu codigo

import random

print " "
print "Welcome, we will play GUESS a Number "
print " "

COUNT = 0
NEW_GAME = True

while NEW_GAME == True:
    NUMBER_RANDOM = random.randint(1,20)
    for COUNT in range(1, 5):
        print NUMBER_RANDOM
        GUESS = int(raw_input ("Insert a Number: "))
        if GUESS == NUMBER_RANDOM:
            print "You win!"
            break
        elif GUESS < NUMBER_RANDOM:
            print "Wrong.Your number is very low. Try again "
        else:
            print "Wrong.Your number is very high. Try again"

    ANSWER = True
    while ANSWER == True:
        print "Do you want to play again? y/n: "
        PLAY_AGAIN = raw_input('> ')
        PLAY_AGAIN = PLAY_AGAIN.lower()
        if PLAY_AGAIN == "y":
            ANSWER = False
            NEW_GAME = True
        elif PLAY_AGAIN == "n":
            ANSWER = False
            NEW_GAME = False
            print "Good - Bye"
        else:
            print "Invalid Option"
