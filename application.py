"""Guess Number, we go playing!"""
import random

print " "
print "            Welcome, we will play GUESS a Number "
print " "
#COUNT = 0
NEW_GAME = True

while NEW_GAME == True: # While New Game is running true to me.
    NUMBER_RANDOM = random.randint(1, 20) #This is the random number that will give the user.
    TURN = 4 #total shift.
    for COUNT in range(1, TURN+1): # In the range of one will add to the variable TURN a number.
        print NUMBER_RANDOM # Here it will print the random number.
        try:# Here will show a number shift and it will print the random number.
            print "    Number shift: ", COUNT
            if COUNT < 5: #Condition if. Initiate shift count.
                GUESS = int(raw_input("Insert a Number: ")) # Here will indicate the shift number.
# While the number entered by the user is less than 0 or equal to or greater than 20 me run this.
                while GUESS < 0 or GUESS >= 20:
     #Here will indicate the shift number.
                    GUESS = int(raw_input("Enter a number between 1 and 20 : "))
#if The number equals the random number will print "You win!."
                if GUESS == NUMBER_RANDOM:
                    print "You win!"
                    break # Here it will cut the program ,if is met.
# If the above condition is not met this condition it will run.
                elif GUESS < NUMBER_RANDOM:
 #The count the condition "if" is less than four it will print the next line.
                    print "Wrong.Your number is very low."
                else:
                    print "Wrong.Your number is very high."
                COUNT += 1 # Here it will add a number  more at the count
            if COUNT == 5: # If the count is equal to 5 it will print.
                print "Game Over"
        except ValueError: #Errors accepted
            print "Enter only numbers"

    ANSWER = True
    while ANSWER == True:
        print "Do you want to play again? y/n: " # Here will ask the user.
        PLAY_AGAIN = raw_input('> ')#Here the user that enter your answer.
        PLAY_AGAIN = PLAY_AGAIN.lower() # This will convert the user's response to lowercase
        if PLAY_AGAIN == "y":
            ANSWER = False
            NEW_GAME = True
        elif PLAY_AGAIN == "n":
            ANSWER = False
            NEW_GAME = False
            print "Good - Bye"
        else:
            print "Invalid Option"
            