# J.P. Leis, Period 6
# Rock Paper Scissors
# rps.py
import random
# Variables
pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "scissors"]

# Welcome Message
# Print a welcome message
print("Welcome to Rock Paper Scissors")
# Prompt for name
pName = input("What is your name? ")

# Score Tracker
# Make a function
def printScore():

	# Prints Score:
	print("Score: ")
# Shows player score
	print(pName + ": " + str(pScore))
# Shows computer score
	print("Computer Score: " + str(cScore))
# Shows ties
	print("Ties: " + str(ties))

# Game Loop
# loop until q in entered
while True:

# prompt for player move (r, p s, q)
	pMove = input("enter 'r' for Rock, 'p' for Paper, 's' for scissors or 'q' to quit")
# print the score
	printScore()
# check if q is entered, if so end the game
	if pMove == 'q':
		break		
# get a computer move (random)
	cMove = random.choice(cMoves)

# compare player move with the computer move
# player picks rock
	if pMoves == "r":
		print(pName + "picked Rock")
		if cMove == "rock":
			print("Computer picks Rock")
			print("Tie")
			ties += 1
		elif cMove == "paper":
			print("Computer picks Paper")
			print("Paper covers Rock")
			cScore += 1
		else: 
			print("Computer picks Scissors")
			print("Rock breaks Scissors")
			pScore += 1
# player picks paper
	elif pMoves == "p":
		pass
# player picks scissors
	elif pMoves == "s":
		pass
# check if pMove is valid
	else:
		print("That is not an option")

