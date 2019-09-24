# Here is a program to simulate a vending machine utilizing 'if/else' statements
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Francesco Rende
# Upper Canada College

# Put down some options for the user to choose from...

import random

numWater = random.randint(0,10)
numVitWater = random.randint(0,10)
numBar = random.randint(0,10)
numFruit = random.randint(0,10)

print("1. Water - $2.00")
print("2. Vitamin Water - $3.50")
print("3. Granola Bar - $1.00")
print("4. Fruit by the Foot - $1.25")

choice = int(input("Please make your selection. \n"))

def giveFood():
	global numWater, numVitWater, numBar, numFruit

	money = 0
	change = 0

	if choice == 1:
		if numWater == 0:
			print("Option not in stock.")

		else:
			numWater = numWater - 1
			money = float(input("Please input $2.00. \n"))
			
			if money == 2.0:
				print("Here is your water. Have a great day!")
			elif money < 2.0:
				print("Insufficient money, please try again.")
			elif money > 2.0:

				change = money - 2.0
				change = round(change, 2)
				print("You have $"+str(change)+" in change. Here is your water. Have a great day!")

	elif choice == 2:
		if numVitWater == 0:
			print("Option not in stock.")

		else:
			numVitWater = numVitWater - 1
			money = float(input("Please input $3.50. \n"))
			
			if money == 3.5:
				print("Here is your vitamin water. Have a great day!")
			elif money < 3.5:
				print("Insufficient money, please try again.")
			elif money > 3.5:

				change = money - 3.5
				change = round(change, 2)
				print("You have $"+str(change)+" in change. Here is your vitamin water. Have a great day!")

	elif choice == 3:
		if numBar == 0:
			print("Option not in stock.")
		
		else:
			numBar = numBar - 1
			money = float(input("Please input $1.00. \n"))
			
			if money == 1.0:
				print("Here is your granola bar. Have a great day!")
			elif money < 1.0:
				print("Insufficient money, please try again.")
			elif money > 1.0:

				change = money - 1.0
				change = round(change, 2)
				print("You have $"+str(change)+" in change. Here is your granola bar. Have a great day!")

	elif choice == 4:
		if numFruit == 0:
			print("Option not in stock.")

		else:
			numFruit = numFruit - 1
			money = float(input("Please input $1.25. \n"))
			
			if money == 1.25:
				print("Here is your Fruit by the Foot™. Have a great day!")
			elif money < 1.25:
				print("Insufficient money, please try again.")
			elif money > 1.25:

				change = money - 1.25
				change = round(change, 2)
				print("You have $"+str(change)+" in change. Here is your Fruit by the Foot™. Have a great day!")

	else:
		print ("This is not a valid choice")

giveFood()

# This is a way to gracefully exit the program
input("Press ENTER to quit the program")