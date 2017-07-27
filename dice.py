import random
output = None

def loadMenu():
	print("1. Roll Die")
	print("2. Roll Dice")
	print("3. Settings")
	menuSelection = int(input("Enter menu selection: "))
	if (menuSelection == 1): 
		rollDie()
	elif (menuSelection == 2):
		numOfDies = int(input("How many dice would you like to roll: "))
		x = 0
		while x < numOfDies:
			rollDie()
			x = x + 1
	elif (menuSelection == 3):
		print("natta")

def rollDie():
	output = random.randint(1,6)
	print(str(output))

loadMenu()
