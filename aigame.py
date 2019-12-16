import cards
import os
import random
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

def turn(player, passer, otherplayer, lie_passed, player_name, number_passer, opponent_known):
	global pile
	made_it = False
	call_bs = "bad input, try again"
	printed1 = False
	print("you are player " + player_name)
	while not made_it:
		if passer:
			print("opponent played " + str(passer) + " " + new_conversion[str(number_passer)] + "(s) (apparently).")
		else:
			print("first round")
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
						opponent_known.append(item)
					pile = []
			if len(otherplayer) == 0:
				return("Ai is winner")
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

''' NEW CODE STARTS HERE. Old code is 99% copy and paste with like 1 readablity change and one thing for the ai
also although the ai function has "accces" to the opponents cards it only has that modify them and only makes decisions off of the cards it knows'''

new_conversion = {
	'12':"queen",
	'13':"king",
	'11':"jack",
	'1':"ace",
	'2':'2',
	'3':'3',
	'4':'4',
	'5':'5',
	'6':'6',
	'7':'7',
	'8':'8',
	'9':'9',
	'10':'10'
}
def get_num_in_known_cards(lis, num_passer, name):
	count = 0
	for item in lis:
		if item.number == num_passer:
			count += 1
	return(count)
def remove_card_from_list(lis, card):
	for item in lis:
		if item.number == card.number and item.suite == card.suite:
			rem_index = lis.index(item)
	return lis.pop(rem_index)
def convert_strings(string):
	if type(string) == str:
		if string == "ace":
			return 1
		elif string == "jack":
			return  11
		elif string == "queen":
			return  12
		elif string == "king":
			return  13
	else:
		return string





def ai_turn(hand, pile, opponent_real, opponent_known, passer, num_passer, lie, last_played):
	amount = 0
	call_bs = False
	last_round = False
	for x in range(passer):
		for item in opponent_known:
				if item.number + 1 == num_passer:
					opponent_known.remove(item)
					break
	amount += get_num_in_known_cards(hand, num_passer-1, "hand")
	amount += get_num_in_known_cards(pile[:-passer], num_passer-1, "pile")
	amount += get_num_in_known_cards(opponent_known, num_passer-1, "o.k")
	if amount + passer > 4:
		call_bs = True
	if len(opponent_real) == 0:
		call_bs = True
		last_round = True
	if abs(last_played - num_passer) > 1 and number_passer != 20:
		call_bs = True
	
	if call_bs:
		print("The AI Called BS")
		if lie:
			for item in pile:
				opponent_real.append(item)
				opponent_known.append(item)
			pile = []
		else:
			if last_round:
				return("human is the winner")
			for item in pile:
				hand.append(item)
			pile = []
	
	playable = []
	for item in hand:
		if abs(item.number+1 - num_passer) <= 1:
			playable.append(item)
	if len(playable) == 1:
		pile.append(remove_card_from_list(hand, playable[0]))
		return[1,False,playable[0].number + 1, pile]
	elif len(playable) > 1:
		to_play = "hi"
		for item in playable:
			good = True
			for item2 in opponent_known:
				if abs(item2.number - item.number) <= 1:
					good = False
			if good:
				to_play = item
		if to_play == "hi":
			to_play = random.choice(playable)
		to_play = [to_play]
		for item in playable:
			if item.suite != to_play[0].suite and item.number == to_play[0].number:
				to_play.append(item)
		if len(to_play) == 1:
			pile.append(remove_card_from_list(hand, to_play[0]))
			return[1, False, to_play[0].number + 1, pile]
		else:
			for item in to_play:
				pile.append(remove_card_from_list(hand, item))
			return[len(to_play), False, to_play[0].number + 1, pile]
	if len(playable) == 0:
		distance_list = []
		for item in hand:
			distance_list.append(abs(abs(num_passer-1 - item.number)-6))
		index_for_lie = distance_list.index(min(distance_list))
		pile.append(remove_card_from_list(hand, hand[index_for_lie]))
		return[1, True, num_passer, pile]











deck = cards.Deck()
deck.shuffle()
hand = deck.draw(26)
opponent_real = deck.draw(26)
pile = []
opponent_known = []
#_, _, _, pile = ai_turn(hand,pile,opponent_real,opponent_known, 1, 1,5,True)
passer = False
lie_passed = False
number_passer = 20

while True:
	result = turn(opponent_real, passer, hand, lie_passed, "player1", number_passer, opponent_known)
	if result == "Ai is winner":
		print(result)
		break
	passer = result[1]
	lie_passed = result[2]
	number_passer2 = result[3]
	result = ai_turn(hand, pile, opponent_real, opponent_known, passer, convert_strings(number_passer2), lie_passed, convert_strings(number_passer))
	if type(result) != list:
		print(result)
		break
	passer = result[0]
	lie_passed = result[1]
	number_passer = result[2]
	pile = result[3]




'''
result = turn(opponent_real, 1, hand, False, "human",2)
ai_turn(hand, pile, opponent_real, [cards.Card("clubs",3)], 1, result[1], result[3], result[2])
print("hand")
for item in hand:
	print(item)
print("opponent")
for item in opponent_real:
	print(item)
'''