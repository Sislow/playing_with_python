import random

magic_num = None
player_guess = None
max_ = None
min_ = None

print(min_,max_)
if min_ == None:
	min_, max_ = 1, 10
print(min_,max_)
def menu():
	print("Hey! Basic guessing game you know the rules")
	print("1. New game")
	print("2. Settings")
	menuSelect = int(input("Menu Selection: "))
	if menuSelect == 1:
		magic_num = random.randint(min_,max_)
		runGame(magic_num)
	elif menuSelect == 2:
		settings()


def runGame(num):
	player_guess = int(input("Guess a number between " + str(min_) + " and " + str(max_) + ": "))
	if player_guess == num:
		print("You win!")
		menu()
	elif player_guess > num:
		print("Too high!")
		runGame(num)
	elif player_guess < num:
		print("Too low!")
		runGame(num) 	


def settings():
	print("Settings")
	print("1. Change Minimum Number")
	print("2. Change Maximum Number")
	print("3. back")
	menuSet = int(input("Menu Selection: "))
	if menuSet == 1:
		min_ = int(input("New minimum number: "))
		settings()
	elif menuSet == 2:
		max_ = int(input("New maximum number: "))
		settings()
	elif menuSet == 3:
		menu()
                   
                   
menu()
