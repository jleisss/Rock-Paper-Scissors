import random

mysteryNumber = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Guess a number between 1 and 100: "))
	score += 1 # the same as score = score + 1
	if guess == mysteryNumber:
		print("Nice job, you guessed correctly")
		break
	elif guess > mysteryNumber:
		print("Lower")
	else:
		print("Higher")

print("You guessed " + str(score) + " times")
