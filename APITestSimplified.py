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

		if '1' in informationRequested:
			articleTitle = jsonData['articles'][articleNumber]['title']
			print("The title of your article is '"+articleTitle+"'.")

		if '2' in informationRequested:
			articleDescription = jsonData['articles'][articleNumber]['description']
			print(articleDescription)

		if '3' in informationRequested:
			articleURL = jsonData['articles'][articleNumber]['url']
			pp = pprint.PrettyPrinter(indent=4)
			pp.pprint("The URL for your article is "+articleURL+".")

		if '4' in informationRequested:
			publishDate = jsonData['articles'][articleNumber]['publishedAt']
			print(str("Your article was published at "+publishDate+"."))

		if '5' in informationRequested:
			articleSource = jsonData['articles'][articleNumber]['source']['name']
			print(str("Your article was published by "+articleSource+"."))

		if '6' in informationRequested:
			articleSourceURL = jsonData['articles'][articleNumber]['source']['url']
			print(str("Your article was published on "+articleSourceURL+"."))

		openArticle = input("Would you like to open up your article? y/n \n")

		if openArticle.lower() == "y":
			webbrowser.open(jsonData['articles'][articleNumber]['url'])
		else:
			print("")

#---------------------------------------------------------------------------------------------------------

generalInfo()

getspecific = input("Would you like to get information about a specific article? y/n \n")

if getspecific.lower() == "y":
	specificArticle()

else:
	print("Thank you for using this program. Press ENTER to quit the program.")