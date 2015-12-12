import random
secret = random.randint(1,99)
guess = 0 
tries = 0
print "Hello and guess"
while guess != secret and tries < 6:
	guess = input("What's your guess?")
	if guess < secret:
		print "Too low"
	elif guess > secret:
		print "Too high"
	tries = tries + 1
if guess == secret:
	print "bingo"
else:
	print "No more guess"
	print "The secret number was", secret
	
