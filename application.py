"""Guess Number, we go playing!"""
# Aqui escribe tu codigo

import random

print " "
print "Welcome, we will play GUESS a Number "
print " "

#COUNT = 0
NEW_GAME = True

while NEW_GAME == True:
    NUMBER_RANDOM = random.randint(1, 20)
    TURN = 4
    for COUNT in range(1, TURN+1):
        print NUMBER_RANDOM
        try:
            print "Turno numero: ",COUNT
            if COUNT < 5:
                GUESS = int(raw_input("Insert a Number: "))
                while GUESS <0 or GUESS >= 20:
                    #"Tyr"
                    GUESS = int(raw_input("Insert a Number: "))
                if GUESS == NUMBER_RANDOM:
                    print "You win!"
                    break
                elif GUESS < NUMBER_RANDOM:
                    if COUNT < 4:
                        print "Wrong.Your number is very low."
                elif GUESS > NUMBER_RANDOM:
                    if COUNT < 4:
                        print "Wrong.Your number is very high."
                COUNT += 1
            if COUNT == 5:
                print "Game Over"
        except ValueError:
                print "Enter only numbers"

    ANSWER = True
    while ANSWER == True:
        print "Do you want to play again? y/n: "
        PLAY_AGAIN = raw_input('> ')
        PLAY_AGAIN = PLAY_AGAIN.lower()
        if PLAY_AGAIN == "y": #
            ANSWER = False
            NEW_GAME = True
        elif PLAY_AGAIN == "n":
            ANSWER = False
            NEW_GAME = False
            print "Good - Bye"
        else:
            print "Invalid Option"