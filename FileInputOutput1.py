# Here is a program that shows how to open a file and WRITE information TO it.
# FileIO Example 3
# Author: Francesco Rende
# Upper Canada College

# Tell the user what the program will do...

print ("This program will open a file and write information to it")
print ("It will then print the contents to the screen for you to see")

# So as before we will still have to open a file, but this time we specify for the parameter either "w" or "a"
# "w" means we are going to "write" information which overwrite everything  that was in the file from before.
# "a" means that we "append" which will add to the end of existing information.

def addSong():

	song = str(input("What is your favorite song?"))

	file = open("FileInfo1.txt", "a")
	file.write ("\n"+song)
	file.close()

	file = open("FileInfo1.txt", "r")
	print (file.read())

	addMore = input("Would you like to add another song? (y/n) \n")
	
	if addMore.lower() == "y":
		addSong()

	else:
		print("Thanks for your time!")

def giveSongs():

	file = open("FileInfo1.txt", "r")
	print(file.read())

def doSomething():

	choice = int(input("Would you like to:\n1. Add a new song or\n2. Get the list of songs\n"))

	if choice == 1:
		addSong()

	elif choice == 2:
		giveSongs()

	else:
		print("Invalid choice.")

	doItAgain = input("Would you like to try again? (y/n) \n")
	
	if doItAgain.lower() == "y":
		doSomething()

	else:
		print("Thanks for your time!")

doSomething()

# This is a way to gracefully exit the program
input("Press ENTER to quit the program")