#Conditional, you don't get a paycheck unless you show up and work
print("Welcome to Ticket Bot")
print("You must be at least 18 to see R rated movies")
age = int(input("How old are you"))

if age > 17: 
	print("You can go see an R rated movie")
else:
	print("You can not go see an R rated movie")

print("Thank you")

mysteryNum = 69
guess = int(input("Guess a number between 1 and 100: "))

if guess == mysteryNum:
	print("Good guess :)")
elif guess > 100:
	print("Your dumb read the directions")
elif guess > mysteryNum:
	print("Lower")
else:
	print("Higher")

# conditional operators: >, <, >=, <=, == (is equal to), != (is not equal)

birthday = input("Is today your birthday(yes/no): ")
if birthday == "yes":
	print("Happy Birthday!")
elif birthday == "no":
	print("Have a good day anyway")
else:
	print("Please read the directions")


