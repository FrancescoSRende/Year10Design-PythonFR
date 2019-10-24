import requests
import json
import pprint
import webbrowser

articleNumber = 0
jsonData = ""
request = ""

#---------------------------------------------------------------------------------------------------------

def generalInfo():

	global request, jsonData

	response = requests.get("https://geo-info.co/43.65,-79.40")

	if (response.status_code == 200):
		request = requests.get("https://gnews.io/api/v3/top-news?token=e5509443651c0842b01c9142e25ef5f0")

		jsonData = request.json()

		numArticles = jsonData['articleCount']
		print(str(numArticles)+" articles were counted.")

	else:
		print("An error has occured.")

#---------------------------------------------------------------------------------------------------------

def specificArticle():

	global articleNumber

	articleNumber = int(input("Which article would you like to get more information about? Please input a number. \n")) - 1

	if articleNumber < 0:
		print("Invalid number given.")

	else:
		print("What information do you want about the article?")
		print("1. Title")
		print("2. Description")
		print("3. URL")
		print("4. Publish Date")
		print("5. Source")
		print("6. Source URL")
		informationRequested = input("Please input all fields you want to see. Ensure there are no spaces between numbers.\n")

		for i in range(len(informationRequested)):
			if informationRequested[i].isdigit:

				if 0 < int(informationRequested[i]) < 7:
					articleAttributeFunctions[int(informationRequested[i])]
				else:
					print("Invalid number; please ensure that they are from 1 to 6.")

			else:
				print("Invalid input.")

		openArticle = input("Would you like to open up your article? y/n \n")

		if openArticle.lower() == "y":
			webbrowser.open(jsonData['articles'][articleNumber]['url'])
		else:
			print("")

#---------------------------------------------------------------------------------------------------------

def getTitle():
	
	global articleNumber

	articleTitle = jsonData['articles'][articleNumber]['title']
	print("The title of your article is '"+articleTitle+"'.")

#---------------------------------------------------------------------------------------------------------

def getDescription():

	global articleNumber

	articleDescription = jsonData['articles'][articleNumber]['description']
	print(articleDescription)

#---------------------------------------------------------------------------------------------------------

def getURL():
	
	global articleNumber

	articleURL = jsonData['articles'][articleNumber]['url']
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint("The URL for your article is "+articleURL+".")

#---------------------------------------------------------------------------------------------------------

def getPublishDate():
	
	global articleNumber

	publishDate = jsonData['articles'][articleNumber]['publishedAt']
	print(str("Your article was published at "+publishDate+"."))

#---------------------------------------------------------------------------------------------------------

def getSource():
	
	global articleNumber

	articleSource = jsonData['articles'][articleNumber]['source']['name']
	print(str("Your article was published by "+articleSource+"."))

#---------------------------------------------------------------------------------------------------------

def getSourceURL():
	
	global articleNumber
	
	articleSourceURL = jsonData['articles'][articleNumber]['source']['url']
	print(str("Your article was published on "+articleSourceURL+"."))

#---------------------------------------------------------------------------------------------------------

articleAttributeFunctions = [getTitle(), getDescription(), getURL(), getPublishDate(), getSource(), getSourceURL()]

#---------------------------------------------------------------------------------------------------------

generalInfo()

getspecific = input("Would you like to get information about a specific article? y/n \n")

if getspecific.lower() == "y":
	specificArticle()

else:
	print("Thank you for using this program. Press ENTER to quit the program.")