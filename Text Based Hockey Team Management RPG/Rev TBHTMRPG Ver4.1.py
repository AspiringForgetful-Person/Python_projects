#Text Based Hockey Team Management RPG, Tiana Tsang Ung, Last modified: 16/11/2018

import random 

def Commands(i, score, winrecord): # Checks input for known commands

	Commands = { # Dictionary of commands and details 
		"record": "displays match history",
		"playerstatus" : "shows which players are currently unable to play",
		"satisfaction" : "shows current satisfaction level of players and fans",
		"resign" : "quits game",
	}
	
	if i == "help": 
		for c in Commands:
			print (c, ":", Commands[c])
	
	elif i in Commands:  
		if i == "record":
			print("wins: " + str(winrecord[0]))
			print("losses: " + str(winrecord[1]))
			return 
			
		elif i == "playerstatus":
			areplayershurtcheck = 0 
			for ply in Team: 
				if ply[4] == 1: # If player status is 1 
					print(ply[1] + " is currently unable to play.")
					areplayershurtcheck = 1 
			if areplayershurtcheck == 0: 
				print("All players are able to play.") 
			return 
			
		elif i == "satisfaction":
			if score < 15: 
				print(":(")
			elif score < 40 and score >= 15: 
				print(":|")
			elif score >= 40 and score < 55: 
				print(":)")
			else: 
				print(":D") 
			return 
			
		elif i == "resign":
			quit() 
			
	else: 
		print("Command not recognised, please try again.") 
		return
		
def TeamCreation(): 

	global Team  
	Team = []
	templist = {}
	
	# for Team array: 0- name 1- position (LetterNumber) 2- assignednumber 3- playerscore 4- status
	playerlists = { 
		"0" : "LWPlayers.txt",
		"1" : "RWPlayers.txt",
		"2" : "CPlayers.txt",
		"3" : "LDPlayers.txt",
		"4" : "RDPlayers.txt",
		"5" : "GPlayers.txt",
	}
	
	numberplayers = { # Dictionary used to store the no. of players allowed in each position 
		"LW" : "3",
		"RW" : "3",
		"C" : "3",
		"LD" : "2",
		"RD" : "2",
		"G" : "1",
	}
	
	for p in range(15): 
		playerdetails = []
		for i in range(5):
			playerdetails.append(0)
		Team.append(playerdetails)
	
	listcounter = 0 
	while listcounter < 6: # Creates temporary dictionary from player text files for user to select players from
		
		position = playerlists[str(listcounter)] 
		position = position[:-11].strip()
		openfile = position + "Players.txt"
		
		for line in open(openfile): 
			line = line.rstrip("\n")  
			parts = line.split(",")	
			listingnumber = parts[0]  
			name = parts[1]
			print(str(listingnumber) + ". " + name)  
			templist[int(listingnumber)] = name 
		
		NumPositionPlayers = int(numberplayers[position]) 
		
		counter = 1
		print("Enter player number to pick:")  
		while counter <= NumPositionPlayers:
			printcheck = 0
			playerchoice = input("For line " + str(counter) + ": ")
			uniqueposition = position + str(counter)
			if not playerchoice:
				print("Invalid number. Please enter a number on the player list.")
			else: 
				playerchoice = int(playerchoice) 
				printcheck = 0 
			if playerchoice in templist: 
				player = templist[playerchoice]
				if player in Team: 
					print("Player already in team. Please pick again.")
				else:
					assignednumber = input("Assign a number for player: ")
					counter = counter + 1
					playerscore = random.randint(6,9)
					for a in Team[:-1]:
						if a[0] == 0:  
							a[0] = player  
							a[1] = uniqueposition
							a[2] = assignednumber
							a[3] = playerscore
							a[4] = 0
							break # Ends for loop once it has executed once 
			else: 
				if printcheck == 0:
					print("Invalid number. Please enter a number on the player list.")
		listcounter = listcounter + 1

	
def MatchOdds(winrecord, score):

	Teamscoretotal = 0 
	
	for a in Team:
		if a[4] == 0: # If injury/suspension status of player is none 
			getscore = a[3]
			Teamscoretotal = Teamscoretotal + getscore # Adds player's individual score to total team score 
		else:
			print(str(a[0]) + " will not be playing this game.") 	
	
	matchmultiplier = random.uniform(0.6,1.0)
	Winscore = Teamscoretotal * matchmultiplier	
	
	if (Winscore > 92):
		eventwin = True 
		print("Your team has won the match.")
		winrecord[0] = winrecord[0] + 1 
		score = score + 1 
	else:
		eventwin = False 
		print("Your team has lost the match.")
		winrecord[1] = winrecord[1] + 1 
		score = score - 1 
		
	print(winrecord) 
	
	return winrecord, eventwin, score 
	
def InjuryChance(score, currentinjured, matchcounter): # Triggers random injury events, runs once per "match" 
	
	injuries = { 
		"1" : "concussion",
		"2" : "groin injury",
		"3" : "shoulder injury",
		"4" : "meniscus injury",
		"5" : "ankle injury",
		"6" : "ACL injury",
	}
	
	duration = {  
		"1" : "2,8",
		"2" : "8,14",
		"3" : "8,14",
		"4" : "10,12",
		"5" : "4,8",
		"6" : "8,14",
	}
	
	offences = { 
		"1" : "embellishment",
		"2" : "spearing",
		"3" : "licking",
		"4" : "slew footing",
		"5" : "elbowing",
		"6" : "illegally checking",
	}	
		
	tempcheckcounter = 0 
	while tempcheckcounter < 13: 
		if currentinjured[tempcheckcounter] == "empty": 
			tempcheckcounter = tempcheckcounter + 1 
		elif int(currentinjured[tempcheckcounter]) == 0: 
			Team[tempcheckcounter][4] = 0 # Reset player status
			currentinjured[tempcheckcounter] = "empty"
			tempcheckcounter = tempcheckcounter + 1 
			
		else:
			decreasedduration = int(currentinjured[tempcheckcounter]) - 1 
			currentinjured[tempcheckcounter] = decreasedduration 
			print(str(currentinjured[tempcheckcounter]))
			tempcheckcounter = tempcheckcounter + 1 
			
	
	injuryluck = random.randint(1,26) 
	
	if injuryluck == 1: 
		injurednum = random.randint(0,12) 
		injured = Team[injurednum][0] 
		Team[injurednum][4] = 1 # Changes status of injured player 
		injurynum = random.randint(1,6) 
		injury = injuries[str(injurynum)] 
		injuredperiod = duration[str(injurynum)] 
		rangeinjured = injuredperiod.split(",")
		lower = int(rangeinjured[0])
		higher = int(rangeinjured[1])
		injuredperiod = random.randint(lower,higher) 
		
		print(injured + " has suffered a " + injury + " and will unable to play for " + str(injuredperiod) + " games.") 
		
		currentinjured[injurednum] = int(injuredperiod) 
	
	if injuryluck == 12:
		suspendedcheck = 0 
		while suspendedcheck == 0:
			suspend = random.randint(0,12) 
			if currentinjured[suspend] == "empty":
				Team[suspend][4] = 1
				suspendduration = random.randint(2,4)
				currentinjured[suspend] = int(suspendduration) 
				suspendedcheck = 1
				suspension = offences[str(random.randint(1,6))]
				suspendplayer = Team[suspend][0]
				
				print(suspendplayer + " has been suspended for " + suspension + " the opposition and will be unable to play for " + str(suspendduration) + " games.")
			
	matchcounter = matchcounter + 1
	
	return score, currentinjured, matchcounter
	
def Events(score, eventwin): 
	tempevent = []
	# for tempevent array 0- outputoption 1- response 2- scoreaffect 3- matchoddsaffect 
	for O in range(3): 
		optiondetails = []
		for i in range(4):  
			optiondetails.append(O)
		tempevent.append(optiondetails)
	if eventwin == True:
		pickevent = random.randint(1,10)
	else:
		pickevent = random.randint(1,12)
	randomchance = random.randint(0,2)
	
	event = "event" + str(pickevent) + ".txt"
	with open(event) as f:
		situation = f.readline().strip()
	l = 0 
	eindex = 0 
	for line in open(event):		
		l = l + 1 
		if l > 1:
			line = line.rstrip("\n") 
			eventdetails = line.split(",")
			optiontext = eventdetails[0]
			
			affectscore = eventdetails[1]
			affectoutcome = eventdetails[2]
			response = eventdetails[3]
			
			tempevent[eindex][0] = optiontext
			tempevent[eindex][1] = affectscore
			tempevent[eindex][2] = affectoutcome	
			tempevent[eindex][3] = response
			
			eindex = eindex + 1 
				
	if eventwin == False or eventwin == 1:
		print(situation) 
		printoptionscount = 1 
		for e in tempevent:
			print(str(printoptionscount) + " " + str(e[0]))
			printoptionscount = printoptionscount + 1 
		
		while 1:
			userpick = input("Enter 1, 2 or 3 to choose: ")
			
			if userpick.isdigit():
				userpick = int(userpick)
				
				if userpick >= 1 and userpick <= 3:
					index = userpick - 1 
					scorechange = int(tempevent[index][1])
					oddschange = int(tempevent[index][2])
				
					print(tempevent[index][3])
			
					Team[14][3] = Team[14][3] + oddschange
					score = score + scorechange
					return score 
					
				else:
					print("Invalid choice, please enter a number from the choice list.")
				
			else:
				print("Invalid choice, please enter a number from the choice list.")
		
def Main(): 
	print('Welcome to TBHTMRPG!!!') 
	winrecord = [0] * 2 
	# for winrecord 0- no. of wins 1- no. of loses 
	
	currentinjured = {
		0 : "empty",
		1 : "empty", 
		2 : "empty", 
		3 : "empty", 
		4 : "empty", 
		5 : "empty", 
		6 : "empty", 
		7 : "empty", 
		8 : "empty", 
		9 : "empty", 
		10 : "empty", 
		11 : "empty", 
		12 : "empty",
	}
	
	score = 50
	matchcounter = 0 
	inputvalid = 0
	eventwin = False
	
	TeamCreation()
	
	print('Type ' + '"' + 'help' + '"' + ' to see commands list or press ENTER to start the next match')
	
	while score >= 0:
		while 1: 
			i = input(">> ") 
			if i == "":
				break
			else:	
				Commands(i, score, winrecord) 
		winrecord, eventwin, score = MatchOdds(winrecord, score)
		score, currentinjured, matchcounter = InjuryChance(score, currentinjured, matchcounter)
		print(currentinjured)
		score = Events(score, eventwin)
	print("You have been fired !!") 
	end = input("Press enter to quit.")
	quit()
	
if __name__ == "__main__": 
	Main()
