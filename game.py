# just FYI don't put a space after the comma when typing cards
import cards
import os
deck = cards.Deck()
deck.shuffle()
player1 = deck.draw(26)
player2 = deck.draw(26)
pile = []
def same_card(card1, card2):
	if card1.suite == card2.suite and card1.number == card2.number:
		return True
	else:
		return False
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

conversion2 = {
	"hearts":0,
	"clubs":1,
	"diamonds":2,
	"spades":3,
}

def turn(player, passer, otherplayer, lie_passed, player_name, number_passer):
	global pile
	made_it = False
	call_bs = "bad input, try again"
	printed1 = False
	print("you are player " + player_name)
	while not made_it:
		if passer:
			print("opponent played " + str(passer) + " " + str(number_passer) + "(s) (apparently).")
		else:
			print("first round")
		'''
		if roundnum == 11:
			roundnum2 = "jack"
		if roundnum == 12:
			roundnum2 = "queen"
		if roundnum == 13:
			roundnum2 = "king"
		if roundnum == 1:
			roundnum2 = "ace"
		else:
			roundnum2 = roundnum
		print("you are on round number " + str(roundnum2))
		'''
		if call_bs == "bad input, try again":
			call_bs = input("do you want to call bs? Input yes or no (no caps)\n")
		if call_bs == "yes" or call_bs == True	:
			call_bs = True
		elif call_bs == "no" or call_bs == False:
			call_bs = False
		else:
			call_bs = "bad input, try again"
		if call_bs == True or call_bs == False:
			if call_bs:
				if lie_passed and not printed1:
					print("They were lying! (or played an incorrect number) They gain cards in the pile. \n")
					printed1 = True
					for item in pile:
						otherplayer.append(item)
					pile = []
				elif not printed1:
					print("oops! they were truthful. (or it was the first round) You gain the cards in the pile (if there are any). \n")
					printed1 = True
					for item in pile:
						player.append(item)
					pile = []
			if len(otherplayer) == 0:
				return("winner")
			for item in player:
				print(item, end = " ,")
			print("\n")
			number = (input("What cards do you want to play? Input in the form # of Suite,# of suite, etc. (match format and spaces otherwise it will not register) \n"))
			number = number.split(",")
			playing = []
			move_on = True
			for item in number:
				words = item.split(" ")
				#print(words)
				if words[0] =="queen":
					words[0] = 11
				elif words[0] =="king":
					words[0] = 12
				elif words[0] =="jack":
					words[0] = 10
				elif words[0] == "ace":
					words[0] = 0
				else:
					try:
						words[0] = int(words[0]) - 1
					except:
						print("bad input, try again 2")
						move_on = False
				#print(words)
				try:
					playing.append(cards.Card(words[2], int(words[0])))
				except:
					print("bad input, try again 3")
					move_on = False
			checkcounter = 0
			for item in playing:
				for item2 in player:
						if same_card(item, item2):
							checkcounter += 1
			if checkcounter != len(playing):
				print("bad input, try again 4")
				pass
				#bad things
			elif move_on: 
				for item in playing:
					for item2 in player:
							if same_card(item, item2):
								player.remove(item2)
				for item in playing:
					pile.append(item)
				to_pass = len(playing)
				checkern = False
				while not checkern:
					fake_num = input("Which number do you want to say you played? \n")
					try:
						fake_num = int(fake_num)
						if fake_num <= 10 and fake_num >= 2:
							number_to_pass = fake_num
							checkern = True
						else:
							print("bad input, try again 5")
					except:
						if fake_num == "king" or fake_num == "queen" or fake_num == "ace" or fake_num == "jack":
							number_to_pass = fake_num
							checkern = True
						else:
							print("bad input, try again 6")
				if number_passer =="queen":
					num_conv = 11
				elif number_passer =="king":
					num_conv  = 12
				elif number_passer =="jack":
					num_conv  = 10
				elif number_passer == "ace":
					num_conv = 0
				else:
					num_conv = int(number_passer) - 1
				if number_to_pass =="queen":
					convnum = 11
				elif number_to_pass=="king":
					convnum  = 12
				elif number_to_pass =="jack":
					convnum  = 10
				elif number_to_pass == "ace":
					convnum = 0
				else:
					convnum = number_to_pass - 1
				lie = False
				for item in playing:
					if (item.number) != convnum or (abs(num_conv - convnum) != 1 and abs(num_conv - convnum) != 12 and abs(num_conv - convnum) != 0):
						lie = True
				if number_passer == 20:
					lie = False
				made_it = True

		else:
			print(call_bs + " 1")
	cls()
	return([player, to_pass, lie, number_to_pass])
passer = False
lie_passed = False
number_passer = 20
while True:
	result = turn(player1, passer, player2, lie_passed, "player1", number_passer)
	if result == "winner":
		print(result + " is player2")
		break
	passer = result[1]
	lie_passed = result[2]
	number_passer = result[3]
	result = turn(player2, passer, player1, lie_passed, "player2", number_passer)
	if result == "winner":
		print(result + " is player1")
		break
	passer = result[1]
	lie_passed = result[2]
	number_passer = result[3]







