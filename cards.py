from random import shuffle
import os

class Card():
	def __init__(self, suite, number):
		self.suite = suite
		self.number = number
	def __str__(self):
		if self.number == 12:
			return("king of " + self.suite)
		if self.number == 11:
			return("queen of " + self.suite)
		if self.number == 10:
			return("jack of " + self.suite)
		if self.number == 0:
			return("ace of " + self.suite)
		else:
			return(str(self.number + 1) + ' of ' + self.suite)

class Deck():
	def __init__(self):
		self.cards = []
		self.conversion = {
			0:"hearts",
			1:"clubs",
			2:"diamonds",
			3:"spades",
		}
		for x in range(2):
			for y in range(13):
				card = Card(self.conversion[x], y)
				self.cards.append(card)
		for x in range(2):
			for y in range(13):
				card = Card(self.conversion[x+2], y)
				self.cards.append(card)
	def reset(self):
		self.cards = []
		for x in range(2):
			for y in range(13):
				card = Card(conversion[i], y)
				self.cards.append(cards)
		for x in range(2):
			for y in range(13):
				card = Card(conversion[x+2], y)
				self.cards.append(cards)
	def shuffle(self):
		shuffle(self.cards)
	def draw(self, num):
		dealed = []
		for x in range(num):
			dealed.append(self.cards.pop(0))
		return dealed

