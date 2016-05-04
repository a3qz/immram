#!/usr/bin/env python2.7


import json
import os
import random
import sys


fp = open("./nodes.json", "r")

JOURNEY = json.load(fp)
fp.close()
store = []
num_islands = 9999
os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("Welcome Traveler! You are about to embark on an epic quest.  You have recieved a prophecy that revaled to you great blessings will come if you return home safely from a sea voyage.  Therefore, you are going to set sail with a company of your closest and bravest companions, with whom you would trust your life.  " )
sys.stdout.write('\n' +'\n')
while not ((num_islands > 2 ) & (num_islands < 8)):
	num_islands = input("Please enter the number of islands you would like to visit on this journey (3-7 please):  ")
for i in range(num_islands):
	os.system('cls' if os.name == 'nt' else 'clear')
	store = []
	move = 9999 
	story = random.choice(JOURNEY.keys())
	sys.stdout.write(story + '\n' +'\n' + JOURNEY[story]["text"]+ '\n' +'\n' )
	while not move == 0:
		sys.stdout.write('\n' +'\n')
		sys.stdout.write( "You have the options: \n \n")
		num = 0
		sys.stdout.write(str(num)+":  "+"Leave this place"+'\n'+ '\n')
		num += 1
		for key in (JOURNEY[story]["branches"].keys()):
			sys.stdout.write(str(num)+":  "+key+'\n'+ '\n')
			num += 1
		store = [x for x in range(num)]
		sys.stdout.write('\n' +'\n')

		while move not in store:
			move = int(raw_input('Please enter the number corresponding to what you would like to visit:  '))
			sys.stdout.write('\n' +'\n' )
		os.system('cls' if os.name == 'nt' else 'clear')
		if move == 0:
                        del JOURNEY[story]
			continue
                elif move in [1,2]:
                        sys.stdout.write(  JOURNEY[story]["branches"][JOURNEY[story]["branches"].keys()[move-1]])
                        raw_input("\n\n\nPress enter to continue on to the next island\n")
                        del JOURNEY[story]
                        os.system('cls' if os.name == 'nt' else 'clear')
                        move = 0




switch = random.randint(0,4)
if switch == 0:
	sys.stdout.write("You have reached the end of your voyage, and have returned home safely!  You are welcomed back with a majestic feast, but slowly life returns to normal.  However, you can't shake the feeling that things just keep going your way these days.  " )
elif switch == 1:
	sys.stdout.write("You have managed to reach the end of your voyage without losing too much blood, congratulations.  As you walk back onto the shore, you are approached by a stranger you have never seen before.  He asks about your voyage, and you tell him your tale.  He listens with fascination, and when you complete the tale, he slips a small bag stuffed full of gold and precious gems into your hand and thanks you before walking away.  You sit there stunned, and before you realize it, he is out of your sight.  ")
elif switch == 2:
	sys.stdout.write("As your company approaches home, you are elated, as it seems like you are finally out of danger.  However, a chill soon runs over the crew as you catch site of home.  You see a little too much smoke in the air, and see no boats slightly offshore, as is usual.  As you land at the port, you see your entire village has been abandoned, and your town hall burned to the ground.  ")
elif switch == 3:
	sys.stdout.write("You reached home.  You leave the boat and celebrate, but everything feels hollow and different now.  After your time at sea, your life on the land feels monotonous, and you cannot escape the feeling of being trapped.  ")
elif switch == 4:
	sys.stdout.write("You reach home, happy to finally be back where you belong.  You go back to your normal life, find a spouse to happily marry, and have a large family that you are proud of.  ")
sys.stdout.write('\n' +'\n')








