"""
Brisca card game done in python by Jeshua Gonzalez Valentin 
Card assests(images) used are from https://nacho-martin.com/images/posts/naipes.png
"""


import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk

#Funtion to count # of calls for the specified function
#Source https://www.quora.com/How-do-I-count-the-number-of-times-a-function-is-called-in-Python
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)

#initializin windows
root = tk.Tk()
root.title("TheCrafter6JGV.com - Card Deck")
root.iconbitmap("images/brisca.ico")
root.geometry("1000x600")
root.configure(background="green")

#global variables
deck = []
player1 = []
player2 = []
trump = []
trump_cards = []
played_cards = []
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
player1_label = Label(root)
player2_label = Label(root)
trump_label = Label(root)
winner_label = Label(root)
played_label1 = Label(root)
played_label2 = Label(root)
winner_index = 0
player1_played = 0
player2_played = 0
first_play = 0


# Resize Cards images Function
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

# Shuffle Cards Function
def shuffle():
	# Define Our Deck
	suits = ["B", "C", "G", "S"]
	values = range(1, 13)

	#calling Global Cards
	global deck, trump, trump_cards
    #creating cards deck
	for suit in suits:
		for value in values:
			deck.append(f'{suit}{value}')
    #shuffling deck
	random.shuffle(deck)
    #Last card of deck indicates the Trump cards
	trump = deck[-1]
	trump_symbol = trump[0]
	
	#identifying all the trump card of the game
	if trump_symbol == 'B':
		trump_cards = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13"]
	if trump_symbol =='C':
		trump_cards = ["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13"]
	if trump_symbol == 'G':
		trump_cards = ["G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","G12","G13"]
	if trump_symbol == 'S':
		trump_cards = ["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13"]

	# Calling Global variables
	global player1, trump_image, player1_label, player2_label, shuffle_button,next_hand_button, winner_label,trump_label
	global player1_image1, player1_image2, player1_image3, player1_image4, player1_image5, player1_image6
	global player2_image1, player2_image2, player2_image3, player2_image4, player2_image5, player2_image6
	global player1_button1, player1_button2, player1_button3, player1_button4, player1_button5, player1_button6
	global player2_button1, player2_button2, player2_button3, player2_button4, player2_button5, player2_button6

	#Display Trump Card in Grid
	trump_image = resize_cards(f'Brisca cards/{trump}.png')
	trump_label.config(image=trump_image)
	trump_label.grid(row=1, column=0, pady=10, padx=10)

	#Remove Card From Deck
	player1_card = deck.pop(0)
	#Append Card To player1 List
	player1.append(player1_card)
	#Display Card in Grid
	player1_image1 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button1.config(image=player1_image1,width=90,height=145,command=lambda: player1_play(player1_button1,player1_image1),state=NORMAL)
	
	#Repeat for next card
	player1_card = deck.pop(0)
	player1.append(player1_card)
	player1_image2 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button2.config(image=player1_image2,width=90,height=145,command=lambda: player1_play(player1_button2,player1_image2),state=NORMAL)
	
	#Repeat for next card
	player1_card = deck.pop(0)
	player1.append(player1_card)
	player1_image3 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button3.config(image=player1_image3,width=90,height=145,command=lambda: player1_play(player1_button3,player1_image3),state=NORMAL)
	
	#Repeat for next card
	player1_card = deck.pop(0)
	player1.append(player1_card)
	player1_image4 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button4.config(image=player1_image4,width=90,height=145,command=lambda: player1_play(player1_button4,player1_image4),state=NORMAL)
	
	#Repeat for next card
	player1_card = deck.pop(0)
	player1.append(player1_card)
	player1_image5 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button5.config(image=player1_image5,width=90,height=145,command=lambda: player1_play(player1_button5,player1_image5),state=NORMAL)

	#Repeat for next card
	player1_card = deck.pop(0)
	player1.append(player1_card)
	player1_image6 = resize_cards(f'Brisca cards/{player1_card}.png')
	player1_button6.config(image=player1_image6,width=90,height=145,command=lambda: player1_play(player1_button6,player1_image6),state=NORMAL)

	#Repeat for Player 2 cards
	player2_card = deck.pop(0)
	player2.append(player2_card)
	player2_image1 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button1.config(image=player2_image1,width=90,height=145,command=lambda: player2_play(player2_button1,player2_image1),state=NORMAL)
	
	#Repeat for next card
	player2_card = deck.pop(0)
	player2.append(player2_card)
	player2_image2 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button2.config(image=player2_image2,width=90,height=145,command=lambda: player2_play(player2_button2,player2_image2),state=NORMAL)
	
	#Repeat for next card
	player2_card = deck.pop(0)
	player2.append(player2_card)
	player2_image3 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button3.config(image=player2_image3,width=90,height=145,command=lambda: player2_play(player2_button3,player2_image3),state=NORMAL)
	
	#Repeat for next card
	player2_card = deck.pop(0)
	player2.append(player2_card)
	player2_image4 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button4.config(image=player2_image4,width=90,height=145,command=lambda: player2_play(player2_button4,player2_image4),state=NORMAL)
	
	#Repeat for next card
	player2_card = deck.pop(0)
	player2.append(player2_card)
	player2_image5 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button5.config(image=player2_image5,width=90,height=145,command=lambda: player2_play(player2_button5,player2_image5),state=NORMAL)

	#Repeat for next card
	player2_card = deck.pop(0)
	player2.append(player2_card)
	player2_image6 = resize_cards(f'Brisca cards/{player2_card}.png')
	player2_button6.config(image=player2_image6,width=90,height=145,command=lambda: player2_play(player2_button6,player2_image6),state=NORMAL)

	#Write number of remaining cards in title bar
	root.title(f'TheCrafterJGV.com - {len(deck)} Cards Left - Player1 Points = {scores[0]} - Player2 Points = {scores[1]} ')
	
	#Display Player 1 Row
	player1_label.grid(row=0,column=6,pady=10,padx = 10)
	player1_label.config(text="Player 1")

	#Display Player 2 Row
	player2_label.grid(row=2,column=6,pady=10,padx = 10)
	player2_label.config(text="Player 2")

	#Hide unused buttons for first hand and Player 2 Cards
	shuffle_button.grid_forget()
	next_hand_button.grid(row=1,column=3,pady=10)
	next_hand_button.grid_forget()
	winner_label.grid_forget()
	display_player1()
	hide_player2()
	
# Deal Out Cards
def next_hand():
	global deck, player1, player2, shuffle_button, next_hand_button, winner_index, winner_label, first_play
	global player1_image1, player1_image2, player1_image3, player1_image4, player1_image5, player1_image6
	global player2_image1, player2_image2, player2_image3, player2_image4, player2_image5, player2_image6
	global player1_button1, player1_button2, player1_button3, player1_button4, player1_button5, player1_button6
	global player2_button1, player2_button2, player2_button3, player2_button4, player2_button5, player2_button6
	global player1_played, player2_played, scores

	#Reset Players Card List
	player1.clear()
	player2.clear()

	#Check if deck is not empty
	if len(deck) > 0:
		# Get the player Cards as before
		player1_card = deck.pop(0)
		player1.append(player1_card)
		player1_image1 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button1.config(image=player1_image1,command=lambda: player1_play(player1_button1,player1_image1),state=NORMAL)
		
		#Repeat for next card
		player1_card = deck.pop(0)
		player1.append(player1_card)
		player1_image2 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button2.config(image=player1_image2,command=lambda: player1_play(player1_button2,player1_image2),state=NORMAL)
		
		#Repeat for next card
		player1_card = deck.pop(0)
		player1.append(player1_card)
		player1_image3 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button3.config(image=player1_image3,command=lambda: player1_play(player1_button3,player1_image3),state=NORMAL)
		
		#Repeat for next card
		player1_card = deck.pop(0)
		player1.append(player1_card)
		player1_image4 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button4.config(image=player1_image4,command=lambda: player1_play(player1_button4,player1_image4),state=NORMAL)
		
		#Repeat for next card
		player1_card = deck.pop(0)
		player1.append(player1_card)
		player1_image5 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button5.config(image=player1_image5,command=lambda: player1_play(player1_button5,player1_image5),state=NORMAL)

		#Repeat for next card
		player1_card = deck.pop(0)
		player1.append(player1_card)
		player1_image6 = resize_cards(f'Brisca cards/{player1_card}.png')
		player1_button6.config(image=player1_image6,command=lambda: player1_play(player1_button6,player1_image6),state=NORMAL)
		
		#Repeat for player2 Cards 
		player2_card = deck.pop(0)
		player2.append(player2_card)
		player2_image1 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button1.config(image=player2_image1,command=lambda: player2_play(player2_button1,player2_image1),state=NORMAL)
		
		#Repeat for next card
		player2_card = deck.pop(0)
		player2.append(player2_card)
		player2_image2 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button2.config(image=player2_image2,command=lambda: player2_play(player2_button2,player2_image2),state=NORMAL)
		
		#Repeat for next card
		player2_card = deck.pop(0)
		player2.append(player2_card)
		player2_image3 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button3.config(image=player2_image3,command=lambda: player2_play(player2_button3,player2_image3),state=NORMAL)
		
		#Repeat for next card
		player2_card = deck.pop(0)
		player2.append(player2_card)
		player2_image4 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button4.config(image=player2_image4,command=lambda: player2_play(player2_button4,player2_image4),state=NORMAL)
		
		#Repeat for next card
		player2_card = deck.pop(0)
		player2.append(player2_card)
		player2_image5 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button5.config(image=player2_image5,command=lambda: player2_play(player2_button5,player2_image5),state=NORMAL)
		
		#Repeat for next card
		player2_card = deck.pop(0)
		player2.append(player2_card)
		player2_image6 = resize_cards(f'Brisca cards/{player2_card}.png')
		player2_button6.config(image=player2_image6,command=lambda: player2_play(player2_button6,player2_image6),state=NORMAL)
		

		#Refresh number of remaining cards in title bar
		root.title(f'TheCrafterJGV.com - {len(deck)} Cards Left - Player1 Points = {scores[0]} - Player2 Points = {scores[1]} ')

		#hide "Next Hand" Button after giving cards to players
		next_hand_button.grid_forget()

		#reset call counts for end_hand()
		end_hand.call_count = 0

	#if deck is empty then end game
	else:
		root.title(f'TheCrafterJGV - No Cards In Deck - Player1 Points = {scores[0]} - Player2 Points = {scores[1]}')
		#re-display shuffle button for new game
		shuffle_button.grid(row=1, column=2, pady=10)
		#hide "Next Hand" button
		next_hand_button.grid_forget()
		#Display Winner
		winner_label.config(text=f'Player {winner_index} Wins!')
		winner_label.grid(row=1,column=5,pady=10)
		#reset internal flags and score
		first_play = 0
		winner_index = 0
		player1_played = 0
		player2_played = 0
		scores = [0,0]

#Counts end_hand() calls
@CallCounter
def end_hand():
	global played_cards, player1_played, player2_played, scores, played_label1
	#calls hand_winner function
	winner = hand_winner(played_cards)
	#calls card_value function
	round_score = sum(card_value(card) for card in played_cards)
	#add points to winner scores[0] = Player 1, scores[1] = Player 2
	scores[winner-1] += round_score
	if winner == 1:
		#Replace Player1 Label with new text
		player1_label.config(text=f"Player1 earned {round_score} pts!")
		player1_label.grid(row=0,column=6,pady=10,padx = 10)
		#Hide Player2 Label
		player2_label.grid_forget()
		#Hide Player 2 cards
		hide_player2()
		#Show Player 1 cards
		display_player1()
	if winner == 2:
		#same logic as before for Player 2
		player2_label.config(text=f"Player2 earned {round_score} pts!")
		player2_label.grid(row=2,column=6,pady=10,padx = 10)
		player1_label.grid_forget()
		hide_player1()
		display_player2()
	#clear played cards
	played_cards.clear()
	#reset player play flag
	player1_played = 0
	player2_played = 0
	#update windows title with new score
	root.title(f'TheCrafterJGV.com - {len(deck)} Cards Left - Player1 Points = {scores[0]} - Player2 Points = {scores[1]} ')
	#update end_hand funcion calls
	end_hand_count = end_hand.call_count
	#if end_hand has been called 6 times, all cards have been played, then re-enable "Next Hand" button
	if end_hand_count == 6:
		next_hand_button.grid(row=1,column=3,pady=10)

#initialize and resize empty card
empty_card = resize_cards(f'Brisca cards/cover.png')

#Define Player1 Play function, this function is called by Player1 Buttons
def player1_play(card_button, card_image):
	global played_cards, winner_index, player1_played, first_play, player2_played, player1, played_label1, played_label2
	global player1_button1, player1_button2, player1_button3, player1_button4, player1_button5, player1_button6
	
	if first_play == 0 or winner_index ==1 or (winner_index == 2 and player2_played == 1):
		played_label1.config(image=card_image)
		played_label1.grid(row=1,column=6,pady=10,padx=10)

		if card_button==player1_button1:
			played_cards.insert(0,player1[0])
			#disable play card once played
			player1_button1.config(image=empty_card,state=DISABLED)
		if card_button==player1_button2:
			played_cards.insert(0,player1[1])
			player1_button2.config(image=empty_card,state=DISABLED)
		if card_button==player1_button3:
			played_cards.insert(0,player1[2])
			player1_button3.config(image=empty_card,state=DISABLED)
		if card_button==player1_button4:
			played_cards.insert(0,player1[3])
			player1_button4.config(image=empty_card,state=DISABLED)
		if card_button==player1_button5:
			played_cards.insert(0,player1[4])
			player1_button5.config(image=empty_card,state=DISABLED)
		if card_button==player1_button6:
			played_cards.insert(0,player1[5])
			player1_button6.config(image=empty_card,state=DISABLED)
		#set Player 1 played flag to one to prevent replaying (once pass flag)
		player1_played = 1
		#first_play is initialized as 0 to allow only the first player to play first, now the Player 2 can play
		first_play = 1
		#display player2 cards after player 1 play
		display_player2()
		#hide player1 cards after player 1 play
		hide_player1()
		#if Player 1 is the second to play because Player 2 won the previous hand, then call end_hand()
		if first_play == 1 and winner_index == 2:
			end_hand()

#Define Player2 Function, this fuction is called by Player2 buttons
def player2_play(card_button,card_image):
	global played_cards, winner_index, player2_played, first_play, player2, played_label2, player1_played
	global player2_button1, player2_button2, player2_button3, player2_button4, player2_button5, player2_button6
	global empty_card
	#Check If statements during first hand or Player1 won and Player1 already played or Player2 won and Player2 hasn't played
	if (winner_index == 0 or (winner_index == 1 and player1_played == 1) or (winner_index == 2 and player2_played == 0 )) and first_play == 1:
		played_label2.config(image=card_image)
		played_label2.grid(row=1,column=7,pady=10,padx=10)
		#same logic as in Player 1
		if card_button==player2_button1:
			played_cards.insert(1,player2[0])
			player2_button1.config(image=empty_card,state=DISABLED)
		if card_button==player2_button2:
			played_cards.insert(1,player2[1])
			player2_button2.config(image=empty_card,state=DISABLED)
		if card_button==player2_button3:
			played_cards.insert(1,player2[2])
			player2_button3.config(image=empty_card,state=DISABLED)
		if card_button==player2_button4:
			played_cards.insert(1,player2[3])
			player2_button4.config(image=empty_card,state=DISABLED)
		if card_button==player2_button5:
			played_cards.insert(1,player2[4])
			player2_button5.config(image=empty_card,state=DISABLED)
		if card_button==player2_button6:
			played_cards.insert(1,player2[5])
			player2_button6.config(image=empty_card,state=DISABLED)
		player2_played = 1
		display_player1()
		hide_player2()
		#If Player2 won the first hand or this is not the first hand and Player1 won then previous hand, so Player2 is the last to play
		if (first_play == 1 and winner_index == 0) or winner_index == 1:
			end_hand()

#Function to assign values to cards per Brisca rules
def card_value(card):
    rank = card
    values = {"B1": 11, "B3": 10, "B12": 4, "B11": 3, "B10": 2,"C1": 11, "C3": 10, "C12": 4, "C11": 3, "C10": 2,
			  "G1": 11, "G3": 10, "G12": 4, "G11": 3, "G10": 2,"S1": 11, "S3": 10, "S12": 4, "S11": 3, "S10": 2}
    return values.get(rank, 0)

#Function to compare cards and determine winner per Brisca rules
def hand_winner(hand):
	global trump, trump_cards, winner_index, hand_counter
	player1_card = hand[0]
	player2_card = hand[1]
	hand_counter = 0
	for i in range(1, len(hand)):
		#If player1 card is a trump card and player2 is not, then player1 wins
		if player1_card in trump_cards and player2_card not in trump_cards:
			winner_index = 1
			return winner_index
		#If player2 card is not a trump card and player2 is, then player2 wins
		if player1_card not in trump_cards and player2_card in trump_cards:
			winner_index = 2
			return winner_index
		#if both cards are trump cards, then values
		if player1_card in trump_cards and player2_card in trump_cards:
			if card_value(player1_card) > card_value(player2_card):
				winner_index = 1
				return winner_index
			if card_value(player1_card) < card_value(player2_card):
				winner_index = 2
				return winner_index
			#if both card value is 0, then compare the card number
			if player1_card[1] > player2_card[1]:
				winner_index = 1
				return winner_index
			if player1_card[1] < player2_card[1]:
				winner_index = 2
				return winner_index
		#if both cards are not trump then...
		if player1_card not in trump_cards and player2_card not in trump_cards:
			#if the player2 plays another suit card than player1, then player1 wins
			if (player1_card[0] != player2_card[0]) and (winner_index == 1 or winner_index == 0):
				winner_index = 1
				return winner_index
			#if the player1 plays another suit card than player2, then player2 wins
			if (player1_card[0] != player2_card[0]) and winner_index == 2:
				winner_index = 2
				return winner_index
			#if both cards value is 0 and both cards are the same suit then...
			if (card_value(player1_card) == 0 and card_value(player2_card)==0) and (player1_card[0] == player2_card[0]):
				#the card with the highest number wins
				if (player1_card[1] < player2_card[1]):
					winner_index = 2
				if (player1_card[1] > player2_card[1]):
					winner_index = 1
				return winner_index
			#if both cards have the same suit, them the card with the higher value wins
			if (player1_card[0] == player2_card[0]) and (card_value(player1_card) < card_value(player2_card)):
				winner_index = 2
				return winner_index
			if (player1_card[0] == player2_card[0]) and (card_value(player1_card) > card_value(player2_card)):
				winner_index = 1
				return winner_index
	return winner_index

#adding green background to frame
my_frame = Frame(root, bg="green")

#Display player1 cards in grid
def display_player1():
	player1_button1.grid(row=0,column=0,pady=10,padx=10)
	player1_button2.grid(row=0,column=1,pady=10,padx=10)
	player1_button3.grid(row=0,column=2,pady=10,padx=10)
	player1_button4.grid(row=0,column=3,pady=10,padx=10)
	player1_button5.grid(row=0,column=4,pady=10,padx=10)
	player1_button6.grid(row=0,column=5,pady=10,padx=10)
	

#Hide player1 cards
def hide_player1():
	player1_button1.grid_forget()
	player1_button2.grid_forget()
	player1_button3.grid_forget()
	player1_button4.grid_forget()
	player1_button5.grid_forget()
	player1_button6.grid_forget()

#Display player2 cards in grid
def display_player2():
	player2_button1.grid(row=2,column=0,pady=10,padx=10)
	player2_button2.grid(row=2,column=1,pady=10,padx=10)
	player2_button3.grid(row=2,column=2,pady=10,padx=10)
	player2_button4.grid(row=2,column=3,pady=10,padx=10)
	player2_button5.grid(row=2,column=4,pady=10,padx=10)
	player2_button6.grid(row=2,column=5,pady=10,padx=10)

#Hide player2 cards
def hide_player2():
	player2_button1.grid_forget()
	player2_button2.grid_forget()
	player2_button3.grid_forget()
	player2_button4.grid_forget()
	player2_button5.grid_forget()
	player2_button6.grid_forget()

# Create a couple buttons
shuffle_button = Button(root, text="Shuffle Deck", command=shuffle)
#shuffle_button.grid(row=1, column=2, pady=10)

next_hand_button = Button(root, text="Next Hand", command=next_hand)
#next_hand_button.grid(row=1,column=3)

# Shuffle Deck On Start
shuffle()

root.mainloop()