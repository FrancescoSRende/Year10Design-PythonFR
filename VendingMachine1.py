# Here is a program to simulate a vending machine utilizing 'if/else' statements
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Francesco Rende
# Upper Canada College

#Randomly setting up whether the items are in stock or not, proportional to their apparent popularity

import random

numWater = random.randint(0,10)
numVitWater = random.randint(0,8)
numBar = random.randint(0,5)
numFruit = random.randint(0,3)
numSpinalFluid = random.randint(0,1)

options = [numWater, numVitWater, numBar, numFruit, numSpinalFluid]

priceWater = 2.00
priceVitWater = 3.5
priceBar = 1.00
priceFruit = 1.25
priceSpinalFluid = 10000.00

prices = [priceWater, priceVitWater, priceBar, priceFruit, priceSpinalFluid]

# Put down some options for the user to choose from...

# Basic skeleton of how to take a variable from one function and use it in another function

# def func1():
# 	mynewvar = 10
# 	func2(mynewvar)

# def func2(var):
# 	print(str(var))

# func1()

money = float(input("How much money do you have? \n"))

def giveFood():
	
	global money, choice, prices

	print("1. Water - $2.00")
	print("2. Vitamin Water - $3.50")
	print("3. Granola Bar - $1.00")
	print("4. Fruit by the Foot - $1.25")
	print("5. Spinal Fluid - $10,000.00")

	choice = int(input("Please make your selection. \n"))

	
	if options[choice - 1] == 0:
		print("Option not in stock.")

	else:
		options[choice - 1] == options[choice - 1] - 1

		if money == prices[choice - 1]:
			money == money - prices[choice - 1]
			print("Here is your item. Have a great day.")

		elif money < prices[choice - 1]:
			print("Insufficient credit, please try again.")

		elif money > prices[choice - 1]:

			money == money - prices[choice - 1]

			print("Here is your item. You have $"+str(money)+" in change.")

	wantsMore = input("Would you like to shop again? (y/n) \n")
	
	if wantsMore.lower() == "y":
		giveFood()

	else:
		print("Enjoy your purchases!")
		stockUpdate(numWater, numVitWater, numBar, numFruit, numSpinalFluid)

def stockUpdate(numWater, numVitWater, numBar, numFruit, numSpinalFluid):

	if choice == 1:

		if numWater != 0:
			print("There are now "+str(numWater)+" bottles of water left.")
		else:
			print("Water is now out of stock.")

	elif choice == 2:

		if numVitWater != 0:
			print("There are now "+str(numVitWater)+" bottles of vitamin water left.")
		else:
			print("Vitamin water is now out of stock.")

	elif choice == 3:

		if numBar != 0:
			print("There are now "+str(numBar)+" granola bars left.")
		else:
			print("Granola bars are now out of stock.")

	elif choice == 4:
		
		if numFruit != 0:
			print("There are now "+str(numFruit)+" Fruit by the Foot™s left.")
		else:
			print("Fruit by the Foot™ is now out of stock.")

	elif choice == 5:
		
		if numFruit != 0:
			print("There are now "+str(numSpinalFluid)+" vials of spinal fluid left.")
		else:
			print("Spinal fluid is now out of stock.")

giveFood()

stockUpdate(numWater, numVitWater, numBar, numFruit, numSpinalFluid)

# This is a way to gracefully exit the program
input("Press ENTER to quit the program")