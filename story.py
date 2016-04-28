#!/usr/bin/env python2.7


import json
import os
import random
import sys


fp = open("./nodes.json", "r")

JOURNEY = json.load(fp)
fp.close()
store = []
num_islands = 3

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
			continue
		#sys.stdout.write('\n' +'\n' )
		sys.stdout.write(  JOURNEY[story]["branches"][JOURNEY[story]["branches"].keys()[move-1]])
		move = 9999



