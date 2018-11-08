from random import shuffle
import time

SUITS = "\u2663 \u2665 \u2666 \u2660".split()
VALUES = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

face_cards = ["J", "Q", "K"]
deck = []
player_total = 0
dealer_total = 0 

def evaluate_user_input(answer):
	if answer == "hit":
		time.sleep(2)
		hit()
		if bust() or blackjack():
			return True
		return False
	elif answer == "stand":
		display_hand_total()
		return True
	else:
		return input("hit or stand? ")

def display_hand_total():
	time.sleep(1)
	print("you have: ")
	print(get_hand_total())

def build_deck():
	for suit in SUITS:
	  for face in VALUES:
	    deck.append(face+suit)

def shuffle_deck():
	shuffle(deck)

def deal():
	global hand
	hand = []
	for i in range(2):
		hand.append(deck.pop(0))
	print(hand)
	blackjack()

def get_hand_total():
	total = 0
	for card in hand:
		if (len(card) > 2 or card[0] in face_cards):
			total += 10
		elif (card[0] == "A"):
			total += 11
		else:
			total += int(card[0])
	return total

def hit():
	print("here is your card")
	time.sleep(1)
	hand.append(deck.pop(0))
	time.sleep(1)
	print(hand)
	time.sleep(1)
	display_hand_total()

def blackjack():
	if get_hand_total() == 21:
		time.sleep(1)
		print("Blackjack!")
		return True

def bust():
	if get_hand_total() > 21:
		time.sleep(1)
		print("Bust!")
		return True

def player_turn():
	response = input("hit or stand? ")
	while not evaluate_user_input(response):
		response = input("hit or stand? ")


def dealer_turn():
	time.sleep(1)
	deal()
	while get_hand_total() < 17:
		hit()
		
build_deck()
shuffle_deck()
deal()
player_turn()
player_total = get_hand_total()
if not get_hand_total() > 20:
	dealer_turn()
	dealer_total = get_hand_total()
	if dealer_total < player_total:
		print("You win!")
	elif dealer_total > 21:
		print("Dealer busts, you win!")
	elif dealer_total == player_total:
		print("Push!")
	else:
		print("Dealer wins...")
else:
	print("You lose...")



