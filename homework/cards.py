import random
import unittest

# SI 507 Winter 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: Thursday 4:00-5:30
# People you worked with: N/A

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

class Hand:
	def __init__(self, list_of_card_objects):
		self.cards = list_of_card_objects
		self.size = len(list_of_card_objects)

	def add_card(self, card):
		if card not in self.cards:
			self.cards.append(card)

	def remove_card(self, card):
		if card in self.cards:
			self.cards.remove(card)
			return card
		else:
			return None

	def draw(self, deck):
		card_from_deck = deck.pop_card()
		self.add_card(card_from_deck)

def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		print('p1 rank_num=', p1_card.rank_num, 'p1 rank_num=', p2_card.rank_num)
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:

			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########







##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class TestCard(unittest.TestCase):

	def test_create(self):
		queen_of_clubs = Card(1, 12)
		ace_of_hearts = Card(2, 1)
		three_of_spades = Card(3, 3)
		self.assertEqual(queen_of_clubs.suit, "Clubs")
		self.assertEqual(queen_of_clubs.rank, "Queen")
		self.assertEqual(ace_of_hearts.suit, "Hearts")
		self.assertEqual(ace_of_hearts.rank, "Ace")
		self.assertEqual(three_of_spades.rank, 3)
		self.assertEqual(queen_of_clubs.suit_names,["Diamonds","Clubs","Hearts","Spades"])

	def test_method(self):
		seven_of_hearts = Card(2, 7)
		king_of_spades = Card(3, 13)
		self.assertEqual(seven_of_hearts.__str__(), "7 of Hearts")
		self.assertEqual(king_of_spades.__str__(), "King of Spades")

class TestDeck(unittest.TestCase):

	def test_create(self):
		deck_instance = Deck()
		self.assertEqual(len(deck_instance.cards),52)

	def test_method(self):
		deck_instance = Deck()
		popped_card = deck_instance.pop_card()
		self.assertIsInstance(popped_card, Card)
		self.assertEqual(len(deck_instance.cards),51)
		self.assertNotIn(popped_card,deck_instance.cards) #this test checks that after the pop_card method is invoked, the returned card is no longer fouond in the deck
		deck_instance.replace_card(popped_card)
		self.assertIn(popped_card, deck_instance.cards) #this test checks that the replace_card method adds the popped card back to the deck
		self.assertEqual(len(deck_instance.cards),52)

class TestGame(unittest.TestCase):

	def test_game_return(self):
		return_value = play_war_game(testing=True)
		self.assertIsInstance(return_value,tuple)
		self.assertEqual(len(return_value), 3)
		self.assertIsInstance(return_value[0],str)

class TestHand(unittest.TestCase):

	def test_create(self):
		list_of_card_objects = []
		for i in range(5):
			list_of_card_objects.append(Card(rank=i))
		hand_instance = Hand(list_of_card_objects)
		self.assertIsInstance(hand_instance.cards[0], Card)
		self.assertEqual(hand_instance.size,5)
		for card in hand_instance.cards:
			self.assertIn(card,list_of_card_objects)

	def test_add_and_remove(self):
		list_of_card_objects = []
		for i in range(5):
			list_of_card_objects.append(Card(rank=i))
		hand_instance = Hand(list_of_card_objects)
		new_card = Card(3, 11)
		hand_instance.add_card(new_card)
		self.assertIn(new_card,hand_instance.cards)
		self.assertEqual(len(hand_instance.cards),6)
		hand_instance.add_card(new_card)
		self.assertEqual(len(hand_instance.cards),6)
		removed_card = hand_instance.remove_card(new_card)
		self.assertNotIn(new_card, hand_instance.cards)
		self.assertEqual(removed_card,new_card)
		self.assertEqual(len(hand_instance.cards),5)
		not_in_hand = hand_instance.remove_card(new_card)
		self.assertEqual(not_in_hand,None)

	def test_draw(self):
		list_of_card_objects = []
		for i in range(5):
			list_of_card_objects.append(Card(rank=i))
		hand_instance = Hand(list_of_card_objects)
		deck_instance = Deck()
		hand_instance.draw(deck_instance)
		self.assertNotIn(hand_instance.cards[-1],deck_instance.cards)
		self.assertEqual(len(deck_instance.cards),51)
		self.assertEqual(len(hand_instance.cards),6)


#############
## The following is a line to run all of the tests you include:
if __name__ == "__main__":
	unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
