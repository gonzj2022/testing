from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.title("Codemy.com - Card Deck")
root.iconbitmap("images/brisca.ico")
root.geometry("900x500")
root.configure(background="green")

# Resize Cards
def resize_cards(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	our_card_resize_image = our_card_img.resize((150, 218))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Shuffle The Cards
def shuffle():
	# Clear all the old cards from previous games
	dealer_label_1.config(image='')
	dealer_label_2.config(image='')
	dealer_label_3.config(image='')
	dealer_label_4.config(image='')
	dealer_label_5.config(image='')

	player_label_1.config(image='')
	player_label_2.config(image='')
	player_label_3.config(image='')
	player_label_4.config(image='')
	player_label_5.config(image='')

	# Define Our Deck
	suits = ["B", "C", "G", "S"]
	values = range(1, 13)
	# 11 = Jack, 12=Queen, 13=King, 14 = Ace

	global deck
	deck =[]

	for suit in suits:
		for value in values:
			deck.append(f'{suit}{value}')

	# Create our players
	global dealer, player
	dealer = []
	player = []

	# Grab a random Card For Dealer
	dealer_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(dealer_card)
	# Append Card To Dealer List
	dealer.append(dealer_card)
	# Output Card To Screen
	global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5
	dealer_image1 = resize_cards(f'Brisca cards/{dealer_card}.png')
	dealer_label_1.config(image=dealer_image1)
	dealer_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(dealer_card)
	# Append Card To Dealer List
	dealer.append(dealer_card)
	dealer_image2 = resize_cards(f'Brisca cards/{dealer_card}.png')
	dealer_label_2.config(image=dealer_image2)
	dealer_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(dealer_card)
	# Append Card To Dealer List
	dealer.append(dealer_card)
	dealer_image3 = resize_cards(f'Brisca cards/{dealer_card}.png')
	dealer_label_3.config(image=dealer_image3)
	dealer_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(dealer_card)
	# Append Card To Dealer List
	dealer.append(dealer_card)
	dealer_image4 = resize_cards(f'Brisca cards/{dealer_card}.png')
	dealer_label_4.config(image=dealer_image4)
	dealer_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(dealer_card)
	# Append Card To Dealer List
	dealer.append(dealer_card)
	dealer_image5 = resize_cards(f'Brisca cards/{dealer_card}.png')
	dealer_label_5.config(image=dealer_image5)

	# Grab a random Card For Player
	player_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(player_card)
	# Append Card To Dealer List
	player.append(player_card)
	# Output Card To Screen
	global player_image1, player_image2, player_image3, player_image4, player_image5
	player_image1 = resize_cards(f'Brisca cards/{player_card}.png')
	player_label_1.config(image=player_image1)
	player_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(player_card)
	# Append Card To Dealer List
	player.append(player_card)
	player_image2 = resize_cards(f'Brisca cards/{player_card}.png')
	player_label_2.config(image=player_image2)
	player_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(player_card)
	# Append Card To Dealer List
	player.append(player_card)
	player_image3 = resize_cards(f'Brisca cards/{player_card}.png')
	player_label_3.config(image=player_image3)
	player_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(player_card)
	# Append Card To Dealer List
	player.append(player_card)
	player_image4 = resize_cards(f'Brisca cards/{player_card}.png')
	player_label_4.config(image=player_image4)
	player_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(player_card)
	# Append Card To Dealer List
	player.append(player_card)
	player_image5 = resize_cards(f'Brisca cards/{player_card}.png')
	player_label_5.config(image=player_image5)

	#player_label.config(text=card)

	# Put number of remaining cards in title bar
	root.title(f'Codemy.com - {len(deck)} Cards Left')


# Deal Out Cards
def deal_cards():
	try:
		# Get the deler Card
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		dealer.append(card)
		# Output Card To Screen
		global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5
		dealer_image1 = resize_cards(f'Brisca cards/{card}.png')
		dealer_label_1.config(image=dealer_image1)
		# Get the deler Card
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		dealer.append(card)
		dealer_image2 = resize_cards(f'Brisca cards/{card}.png')
		dealer_label_2.config(image=dealer_image2)
		# Get the deler Card
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		dealer.append(card)
		dealer_image3 = resize_cards(f'Brisca cards/{card}.png')
		dealer_label_3.config(image=dealer_image3)
		# Get the deler Card
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		dealer.append(card)
		dealer_image4 = resize_cards(f'Brisca cards/{card}.png')
		dealer_label_4.config(image=dealer_image4)
		# Get the deler Card
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		dealer.append(card)
		dealer_image5 = resize_cards(f'Brisca cards/{card}.png')
		dealer_label_5.config(image=dealer_image5)
		#dealer_label.config(text=card)

		# Get the player Card
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		player.append(card)
		# Output Card To Screen
		global player_image1, player_image2, player_image3, player_image4, player_image5
		player_image1 = resize_cards(f'Brisca cards/{card}.png')
		player_label_1.config(image=player_image1)
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		player.append(card)
		player_image2 = resize_cards(f'Brisca cards/{card}.png')
		player_label_2.config(image=player_image2)
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		player.append(card)
		player_image3 = resize_cards(f'Brisca cards/{card}.png')
		player_label_3.config(image=player_image3)
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		player.append(card)
		player_image4 = resize_cards(f'Brisca cards/{card}.png')
		player_label_4.config(image=player_image4)
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		player.append(card)
		player_image5 = resize_cards(f'Brisca cards/{card}.png')
		player_label_5.config(image=player_image5)
		#player_label.config(text=card)


		# Put number of remaining cards in title bar
		root.title(f'Codemy.com - {len(deck)} Cards Left')

	except:
		root.title(f'Codemy.com - No Cards In Deck')




my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack(ipadx=20, pady=10)

# Put Dealer cards in frames
dealer_label_1 = Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

# Put Player cards in frames
player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='')
player_label_2.grid(row=1, column=1, pady=20, padx=20)

player_label_3 = Label(player_frame, text='')
player_label_3.grid(row=1, column=2, pady=20, padx=20)

player_label_4 = Label(player_frame, text='')
player_label_4.grid(row=1, column=3, pady=20, padx=20)

player_label_5 = Label(player_frame, text='')
player_label_5.grid(row=1, column=4, pady=20, padx=20)


# Create a couple buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command=deal_cards)
card_button.pack(pady=20)



# Shuffle Deck On Start
shuffle()


root.mainloop()

