import tkinter as tk
from tkinter import *
import random, time
from PIL import Image, ImageTk


root = tk.Tk()
root.title("TheCrafter6JGV.com - Card Deck")
root.iconbitmap("images/brisca.ico")
root.geometry("1000x600")
root.configure(background="green")
deck = []
player1 = []
player2 = []
trump = []
trump_cards = []
scores = [0,0]
player1_button1 = tk.Button(root)
player1_button2 = tk.Button(root)
player1_button3 = tk.Button(root)
player1_button4 = tk.Button(root)
player1_button5 = tk.Button(root)
player1_button6 = tk.Button(root)
player2_button1 = tk.Button(root)
player2_button2 = tk.Button(root)
player2_button3 = tk.Button(root)
player2_button4 = tk.Button(root)
player2_button5 = tk.Button(root)
player2_button6 = tk.Button(root)
winner_index = 0
player1_played = 0
player2_played = 0
first_play = 0


# Resize Cards
def resize_cards(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	our_card_resize_image = our_card_img.resize((90, 145))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Shuffle The Cards
def shuffle():
# Clear all the old cards from previous games
#	player1_label_1.config(image='')
#	player1_label_2.config(image='')
#	player1_label_3.config(image='')
#	player1_label_4.config(image='')
#	player1_label_5.config(image='')
#	player1_label_6.config(image='')

#	player2_label_1.config(image='')
#	player2_label_2.config(image='')
#	player2_label_3.config(image='')
#	player2_label_4.config(image='')
#	player2_label_5.config(image='')
#	player2_label_6.config(image='')

	# Define Our Deck
	suits = ["B", "C", "G", "S"]
	values = range(1, 13)

	global deck, trump, trump_cards
	for suit in suits:
		for value in values:
			deck.append(f'{suit}{value}')
	random.shuffle(deck)
	trump = deck[-1]
	trump_symbol = trump[0]
	print(f"trump_symbol= {trump_symbol}")
	
	if trump_symbol == 'B':
		trump_cards = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13"]
	if trump_symbol =='C':
		trump_cards = ["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13"]
	if trump_symbol == 'G':
		trump_cards = ["G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","G12","G13"]
	if trump_symbol == 'S':
		trump_cards = ["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13"]
	print(f"trump cards = {trump_cards}")

	# Calling Global variables
	global player1, trump_image
	global player1_image1, player1_image2, player1_image3, player1_image4, player1_image5, player1_image6
	global player2_image1, player2_image2, player2_image3, player2_image4, player2_image5, player2_image6
	global player1_button1, player1_button2, player1_button3, player1_button4, player1_button5, player1_button6
	global player2_button1, player2_button2, player2_button3, player2_button4, player2_button5, player2_button6

	trump_image = resize_cards(f'Brisca cards/{trump}.png')
	trump_label_1.config(image=trump_image)

	# Remove Card From Deck
	player1_card = deck.pop(0)
	# Append Card To player1 List
	player1.append(player1_card)
	# Output Card To Screen
	player1_image1 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button1.config(image=player1_image1,width=90,height=145,command=lambda: player1_play(player1_button1,player1_image1))
	
	# Remove Card From Deck
	player1_card = deck.pop(0)
	# Append Card To player1 List
	player1.append(player1_card)
	player1_image2 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button2.config(image=player1_image2,width=90,height=145,command=lambda: player1_play(player1_button2,player1_image2))
	
	# Remove Card From Deck
	player1_card = deck.pop(0)
	# Append Card To player1 List
	player1.append(player1_card)
	player1_image3 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button3.config(image=player1_image3,width=90,height=145,command=lambda: player1_play(player1_button3,player1_image3))
	
	# Remove Card From Deck
	player1_card = deck.pop(0)
	# Append Card To player1 List
	player1.append(player1_card)
	player1_image4 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button4.config(image=player1_image4,width=90,height=145,command=lambda: player1_play(player1_button4,player1_image4))
	
	# Remove Card From Deck
	player1_card = deck.pop(0)
	# Append Card To player1 List
	player1.append(player1_card)
	player1_image5 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button5.config(image=player1_image5,width=90,height=145,command=lambda: player1_play(player1_button5,player1_image5))

	# Remove Card From Deck
	player1_card = deck.pop(0)
	# Append Card To player1 List
	player1.append(player1_card)
	player1_image6 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button6.config(image=player1_image6,width=90,height=145,command=lambda: player1_play(player1_button6,player1_image6))

	# Remove Card From Deck
	player2_card = deck.pop(0)
	# Append Card To player1 List
	player2.append(player2_card)
	# Output Card To Screen
	player2_image1 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button1.config(image=player2_image1,width=90,height=145,command=lambda: player2_play(player2_button1,player2_image1))
	
	# Remove Card From Deck
	player2_card = deck.pop(0)
	# Append Card To player1 List
	player2.append(player2_card)
	player2_image2 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button2.config(image=player2_image2,width=90,height=145,command=lambda: player2_play(player2_button2,player2_image2))
	
	# Remove Card From Deck
	player2_card = deck.pop(0)
	#deck.remove(player2_card)
	# Append Card To player1 List
	player2.append(player2_card)
	player2_image3 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button3.config(image=player2_image3,width=90,height=145,command=lambda: player2_play(player2_button3,player2_image3))
	
	# Remove Card From Deck
	player2_card = deck.pop(0)
	# Append Card To player1 List
	player2.append(player2_card)
	player2_image4 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button4.config(image=player2_image4,width=90,height=145,command=lambda: player2_play(player2_button4,player2_image4))
	
	# Remove Card From Deck
	player2_card = deck.pop(0)
	# Append Card To player1 List
	player2.append(player2_card)
	player2_image5 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button5.config(image=player2_image5,width=90,height=145,command=lambda: player2_play(player2_button5,player2_image5))

	# Remove Card From Deck
	player2_card = deck.pop(0)
	# Append Card To player1 List
	player2.append(player2_card)
	player2_image6 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button6.config(image=player2_image6,width=90,height=145,command=lambda: player2_play(player2_button6,player2_image6))

	# Put number of remaining cards in title bar
	root.title(f'TheCrafterJGV.com - {len(deck)} Cards Left - Player1 Points = {scores[0]} - Player2 Points = {scores[1]} ')


# Deal Out Cards
def deal_cards():
	global deck, player1, player2
	global player1_image1, player1_image2, player1_image3, player1_image4, player1_image5, player1_image6
	global player2_image1, player2_image2, player2_image3, player2_image4, player2_image5, player2_image6
	global player1_button1, player1_button2, player1_button3, player1_button4, player1_button5, player1_button6
	global player2_button1, player2_button2, player2_button3, player2_button4, player2_button5, player2_button6

	player1.clear()
	player2.clear()

	if len(deck) > 0:
		# Get the player1 Cards
		# Remove Card From Deck
		player1_card = deck.pop(0)
		# Append Card To player1 List
		player1.append(player1_card)
		player1_image1 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button1.config(image=player1_image1,command=lambda: player1_play(player1_button1,player1_image1),state=NORMAL)
		
		# Remove Card From Deck
		player1_card = deck.pop(0)
		# Append Card To player1 List
		player1.append(player1_card)
		player1_image2 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button2.config(image=player1_image2,command=lambda: player1_play(player1_button2,player1_image2),state=NORMAL)
		
		# Remove Card From Deck
		player1_card = deck.pop(0)
		# Append Card To player1 List
		player1.append(player1_card)
		player1_image3 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button3.config(image=player1_image3,command=lambda: player1_play(player1_button3,player1_image3),state=NORMAL)
		
		# Remove Card From Deck
		player1_card = deck.pop(0)
		# Append Card To player1 List
		player1.append(player1_card)
		player1_image4 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button4.config(image=player1_image4,command=lambda: player1_play(player1_button4,player1_image4),state=NORMAL)
		
		# Remove Card From Deck
		player1_card = deck.pop(0)
		# Append Card To player1 List
		player1.append(player1_card)
		player1_image5 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button5.config(image=player1_image5,command=lambda: player1_play(player1_button5,player1_image5),state=NORMAL)

		# Remove Card From Deck
		player1_card = deck.pop(0)
		# Append Card To player1 List
		player1.append(player1_card)
		player1_image6 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button6.config(image=player1_image6,command=lambda: player1_play(player1_button6,player1_image6),state=NORMAL)
		
		# Get the player2 Cards
		# Remove Card From Deck
		player2_card = deck.pop(0)
		# Append Card To player1 List
		player2.append(player2_card)
		player2_image1 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button1.config(image=player2_image1,command=lambda: player2_play(player2_button1,player2_image1),state=NORMAL)
		
		# Remove Card From Deck
		player2_card = deck.pop(0)
		# Append Card To player1 List
		player2.append(player2_card)
		player2_image2 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button2.config(image=player2_image2,command=lambda: player2_play(player2_button2,player2_image2),state=NORMAL)
		
		# Remove Card From Deck
		player2_card = deck.pop(0)
		# Append Card To player1 List
		player2.append(player2_card)
		player2_image3 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button3.config(image=player2_image3,command=lambda: player2_play(player2_button3,player2_image3),state=NORMAL)
		
		# Remove Card From Deck
		player2_card = deck.pop(0)
		# Append Card To player1 List
		player2.append(player2_card)
		player2_image4 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button4.config(image=player2_image4,command=lambda: player2_play(player2_button4,player2_image4),state=NORMAL)
		
		# Remove Card From Deck
		player2_card = deck.pop(0)
		# Append Card To player1 List
		player2.append(player2_card)
		player2_image5 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button5.config(image=player2_image5,command=lambda: player2_play(player2_button5,player2_image5),state=NORMAL)
		
		# Remove Card From Deck
		player2_card = deck.pop(0)
		# Append Card To player1 List
		player2.append(player2_card)
		player2_image6 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button6.config(image=player2_image6,command=lambda: player2_play(player2_button6,player2_image6),state=NORMAL)
		

		# Put number of remaining cards in title bar
		root.title(f'TheCrafterJGV.com - {len(deck)} Cards Left - Player1 Points = {scores[0]} - Player2 Points = {scores[1]} ')

	#except:
	else:
		root.title(f'TheCrafterJGV - No Cards In Deck - Player1 Points = {scores[0]} - Player2 Points = {scores[1]}')

def end_hand():
	global played_cards, player1_played, player2_played, scores, played_label_1
	print("test")
	print(played_cards)
	winner = hand_winner(played_cards)
	round_score = sum(card_value(card) for card in played_cards)
	scores[winner-1] += round_score
	print(f"Player {winner} wins the round and earns {round_score} points!")
	played_cards = []
	player1_played = 0
	player2_played = 0
	root.title(f'TheCrafterJGV.com - {len(deck)} Cards Left - Player1 Points = {scores[0]} - Player2 Points = {scores[1]} ')
	
played_cards = []
played_label_1 = Label(root,pady=10,padx=10)
played_label_2 = Label(root,pady=10,padx=10)
empty_card = resize_cards(f'Brisca cards/cover.png')

def player1_play(card_button, card_image):
	global played_cards, winner_index, player1_played, first_play, player2_played, player1, played_label_1
	global player1_button1, player1_button2, player1_button3, player1_button4, player1_button5, player1_button6
	global empty_card
	print(f"player 1 = {player1}")
	if first_play == 0 or winner_index ==1 or (winner_index == 2 and player2_played == 1):
		played_label_1.config(image=card_image)
		played_label_1.grid(row=1,column=6,pady=10,padx=10)
		if card_button==player1_button1:
			played_cards.insert(0,player1[0])
			player1_button1.config(image=empty_card,width=90,height=145,state=DISABLED)
		if card_button==player1_button2:
			played_cards.insert(0,player1[1])
			player1_button2.config(image=empty_card,width=90,height=145,state=DISABLED)
		if card_button==player1_button3:
			played_cards.insert(0,player1[2])
			player1_button3.config(image=empty_card,width=90,height=145,state=DISABLED)
		if card_button==player1_button4:
			played_cards.insert(0,player1[3])
			player1_button4.config(image=empty_card,width=90,height=145,state=DISABLED)
		if card_button==player1_button5:
			played_cards.insert(0,player1[4])
			player1_button5.config(image=empty_card,width=90,height=145,state=DISABLED)
		if card_button==player1_button6:
			played_cards.insert(0,player1[5])
			player1_button6.config(image=empty_card,width=90,height=145,state=DISABLED)
		player1_played = 1
		first_play = 1
		if first_play == 1 and winner_index == 2:
			end_hand()

def player2_play(card_button,card_image):
	global played_cards, winner_index, player2_played, first_play, player2, played_label_2, player1_played
	global player2_button1, player2_button2, player2_button3, player2_button4, player2_button5, player2_button6
	global empty_card, test
	print(f"player 2 = {player2}")
	
	if (winner_index == 0 or (winner_index == 1 and player1_played == 1) or (winner_index == 2 and player2_played == 0 )) and first_play == 1:
		played_label_2.config(image=card_image)
		played_label_2.grid(row=1,column=7,pady=10,padx=10)
		if card_button==player2_button1:
			played_cards.insert(1,player2[0])
			player2_button1.config(image=empty_card,width=90,height=145,state=DISABLED)
		if card_button==player2_button2:
			played_cards.insert(1,player2[1])
			player2_button2.config(image=empty_card,width=90,height=145,state=DISABLED)
		if card_button==player2_button3:
			played_cards.insert(1,player2[2])
			player2_button3.config(image=empty_card,width=90,height=145,state=DISABLED)
		if card_button==player2_button4:
			played_cards.insert(1,player2[3])
			player2_button4.config(image=empty_card,width=90,height=145,state=DISABLED)
		if card_button==player2_button5:
			played_cards.insert(1,player2[4])
			player2_button5.config(image=empty_card,width=90,height=145,state=DISABLED)
		if card_button==player2_button6:
			played_cards.insert(1,player2[5])
			player2_button6.config(image=empty_card,width=90,height=145,state=DISABLED)
		player2_played = 1
		if (first_play == 1 and winner_index == 0) or winner_index == 1:
			end_hand()

def card_value(card):
    rank = card
    values = {"B1": 11, "B3": 10, "B12": 4, "B11": 3, "B10": 2,"C1": 11, "C3": 10, "C12": 4, "C11": 3, "C10": 2,
			  "G1": 11, "G3": 10, "G12": 4, "G11": 3, "G10": 2,"S1": 11, "S3": 10, "S12": 4, "S11": 3, "S10": 2}
    return values.get(rank, 0)

def hand_winner(hand):
	global trump, trump_cards, winner_index
	player1_card = hand[0]
	player2_card = hand[1]
	for i in range(1, len(hand)):
		if player1_card in trump_cards and player2_card not in trump_cards:
			print("ïnside if1")
			winner_index = 1
			return winner_index
		if player1_card not in trump_cards and player2_card in trump_cards:
			print("ïnside if2")
			winner_index = 2
			return winner_index
		if player1_card in trump_cards and player2_card in trump_cards:
			print("ïnside if3")
			print(f"player1_value{card_value(player1_card)}")
			print(f"player2_value{card_value(player2_card)}")
			if card_value(player1_card) > card_value(player2_card):
				winner_index = 1
				return winner_index
			if card_value(player1_card) < card_value(player2_card):
				winner_index = 2
				return winner_index
			if player1_card[1] > player2_card[1]:
				winner_index = 1
				return winner_index
			if player1_card[1] < player2_card[1]:
				winner_index = 2
				return winner_index
		if player1_card not in trump_cards and player2_card not in trump_cards:
			print("ïnside if4")
			print(f"player1_value{card_value(player1_card)}")
			print(f"player2_value{card_value(player2_card)}")
			print(f"winner index= {winner_index}")
			if (player1_card[0] != player2_card[0]) and (winner_index == 1 or winner_index == 0):
				winner_index = 1
				return winner_index
			if (player1_card[0] != player2_card[0]) and winner_index == 2:
				winner_index = 2
				return winner_index
			if (player1_card[0] == player2_card[0]) and (card_value(player1_card) < card_value(player2_card)):
				winner_index = 2
				return winner_index
			if (player1_card[0] == player2_card[0]) and (card_value(player1_card) > card_value(player2_card)):
				winner_index = 1
				return winner_index
	return winner_index
	

my_frame = Frame(root, bg="green")

trump_label_1 = Label(root, text='')
trump_label_1.grid(row=1, column=0, pady=10, padx=10)

# Put player1 cards as buttons
player1_button1.grid(row=0,column=0,pady=10,padx=10)
player1_button2.grid(row=0,column=1,pady=10,padx=10)
player1_button3.grid(row=0,column=2,pady=10,padx=10)
player1_button4.grid(row=0,column=3,pady=10,padx=10)
player1_button5.grid(row=0,column=4,pady=10,padx=10)
player1_button6.grid(row=0,column=5,pady=10,padx=10)
Player1_label = Label(root, text="Player 1")
Player1_label.grid(row=0, column=6, pady=10, padx = 10)

# Put Player cards as buttons
player2_button1.grid(row=2,column=0,pady=10,padx=10)
player2_button2.grid(row=2, column=1, pady=10, padx=10)
player2_button3.grid(row=2, column=2, pady=10, padx=10)
player2_button4.grid(row=2, column=3, pady=10, padx=10)
player2_button5.grid(row=2, column=4, pady=10, padx=10)
player2_button6.grid(row=2, column=5, pady=10, padx=10)
Player2_label = Label(root, text="Player 2")
Player2_label.grid(row=2, column=6, pady=10, padx = 10)

# Create a couple buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.grid(row=1, column=2, pady=10)

card_button = Button(root, text="Next Cards", font=("Helvetica", 14), command=deal_cards)
card_button.grid(row=1,column=3)

# Shuffle Deck On Start
shuffle()

root.mainloop()

