import random

def create_deck():
    suits = ["oros", "copas", "espadas", "bastos"]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "sota", "caballo", "rey"]
    deck = [(suit, rank) for suit in suits for rank in ranks]
    return deck

def deal_cards(deck, num_players, cards_per_player):
    hands = [[] for _ in range(num_players)]
    for _ in range(cards_per_player):
        for i in range(num_players):
            hands[i].append(deck.pop(random.randint(0, len(deck) - 1)))
    return hands, deck

def card_value(card):
    rank = card[1]
    values = {"1": 11, "3": 10, "rey": 4, "caballo": 3, "sota": 2}
    return values.get(rank, 0)

def determine_winner(played_cards, trump):
    winning_card = played_cards[0]
    winner_index = 0
    for i in range(1, len(played_cards)):
        if played_cards[i][0] == trump and winning_card[0] != trump:
            winning_card = played_cards[i]
            winner_index = i
        elif played_cards[i][0] == winning_card[0]:
            if card_value(played_cards[i]) > card_value(winning_card):
                winning_card = played_cards[i]
                winner_index = i
    return winner_index

def play_game():
    deck = create_deck()
    random.shuffle(deck)
    trump = deck[-1][0]
    print("Trump suit:", trump)
    hands, deck = deal_cards(deck, 2, 5)
    scores = [0, 0]

    for round_num in range(5):
            print("\nRound", round_num + 1)
            played_cards = []
            for i in range(2):
                print(f"Player {i+1} hand: {hands[i]}")
                choice = int(input(f"Player {i+1}, choose a card (0-{len(hands[i])-1}): "))
                played_cards.append(hands[i].pop(choice))
            
            winner = determine_winner(played_cards, trump)
            round_score = sum(card_value(card) for card in played_cards)
            scores[winner] += round_score
            print(f"Player {winner+1} wins the round and earns {round_score} points!")
    print("\nFinal Scores:")
    print(f"Player 1: {scores[0]} points")
    print(f"Player 2: {scores[1]} points")
    if scores[0] > scores[1]:
        print("Player 1 wins the game!")
    elif scores[1] > scores[0]:
         print("Player 2 wins the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()