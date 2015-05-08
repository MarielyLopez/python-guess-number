# Aqui escribe tu codigo

import random

print " "
print "Welcome, we will play Guess a Number "
print " "
number_random = random.randint(1,20)
print number_random
guess = int(raw_input ("Insert a Number: "))
if guess == number_random:
	print "You win!" 
elif guess < number_random:
	print "Wrong.Your number is very low. Try again "
else:
	print "Wrong.Your number is very high. Try again"
