# Design the data structures for a generic deck of cards. Explain how you would
# subclass the data structures to implement blackjack. 

import random

class Deck:

	def __init__(self):
		cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
		suits = ['Club', 'Diamond', 'Heart', 'Spade']
		deck = []
		for card_val, card in enumerate(cards, 1):
			for suit_val, suit in enumerate(suits):
				deck.append(Card(suit_val, card_val))
		self.cards = deck
		self.hands = []
		self.card_index = 0

	def shuffle(self):
		random.shuffle(self.cards)
		self.card_index = 0

	def dealCards(self, cards_dealt, num_hands):
		for hand in range(0, num_hands):
			self.hands.append(Hand())
		for card_num in range(0, cards_dealt):
			for hand in self.hands:
				hand.addCard(self.cards[self.card_index])
				self.card_index += 1


class Card:
	def __init__(self, suit, val):
		self.suit = suit
		self.val = val

class Hand:
	def __init__(self):
		self.cards = []

	def addCard(self, card):
		self.cards.append(card)

	def score(self):
		score = 0
		for card in self.cards:
			score += card.val
		return score