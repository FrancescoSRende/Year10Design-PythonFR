import random

yourHP = 0
enemyHP = 500

yourATK = []
enemyATK = [30,45]

yourDEF = []
enemyDEF = [0,20]

yourACC = 0
enemyACC = 75

print("Please choose your class.\n")
playerClass = input("1. Soldier, 2. Berserker, 3. Wizard and 4. Knight.\n")

if int(playerClass) == 1:
	yourHP == 500;
	yourATK = [25,40,60];
	yourDEF = [10,20];
	yourACC = 80;
	print("Your HP is "+str(yourHP)+"HP.")
elif int(playerClass) == 2:
	yourHP == 400;
	yourATK = [40,60,85];
	yourDEF = [5,15];
	yourACC = 75;
	print("Your HP is "+str(yourHP)+"HP.")
elif int(playerClass) == 3:
	yourHP == 550;
	yourATK = [25,35,50];
	yourDEF = [10,20];
	yourACC = 90;
	print("Your HP is "+str(yourHP)+"HP.")
elif int(playerClass) == 4:
	yourHP == 600;
	yourATK = [20,35,55];
	yourDEF = [20,30];
	yourACC = 80;
	print("Your HP is "+str(yourHP)+"HP.")
else:
	print("Invalid field input.")

while yourHP > 0 and enemyHP > 0:
	attack = print("Would you like to attack? y/n\n")
		if attack == "y":
			if random.randint(0,100) < yourACC:
				chanceYourATK = random.randint(0,len(yourATK)-1)
				chanceEnemyDEF = random.randint(0,len(enemyDEF)-1)
				if yourATK[chanceYourATK] > enemyDEF[chanceEnemyDEF]:
					enemyHP = enemyHP - yourATK[chanceYourATK] + enemyDEF[chanceEnemyDEF]
					if enemyHP <= 0:
						print("Enemy is dead.")
					else:
						print("Enemy's health is "+str(enemyHP)+"HP.")
				else:
					print("Enemy dodged attack.")
			else:
				print("Attack failed.")
	if random.randint(0,100) < enemyACC:
		chanceEnemyATK = random.randint(0,len(enemyATK)-1)
		chanceYourDEF = random.randint(0,len(yourDEF)-1)
		if enemyATK[chanceEnemyATK] > yourDEF[chanceYourDEF]:
			yourHP = yourHP - enemyATK[chanceEnemyATK] + 
