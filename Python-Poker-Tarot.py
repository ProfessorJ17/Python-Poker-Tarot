import random

# Define the ranks and suits for both normal and tarot cards
normal_ranks = [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
normal_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

tarot_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Page', 'Knight', 'Queen', 'King']
tarot_suits = ['Wands', 'Pentacles', 'Cups', 'Swords']

# Combine normal and tarot cards to create a deck
deck = [(rank, suit) for rank in normal_ranks for suit in normal_suits] + [(rank, suit) for rank in tarot_ranks for suit in tarot_suits]

# Shuffle the deck
random.shuffle(deck)

# Initialize player and dealer coins
player_coins = 1000
dealer_coins = 1000

def deal_hands(deck):
    # Deal two private cards to each player
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    return player_hand, dealer_hand

def deal_community_cards(deck, num_cards):
    # Deal community cards
    community_cards = [deck.pop() for _ in range(num_cards)]

    return community_cards

def betting_round(player_coins, dealer_coins, pot):
    # Player's turn to bet
    player_bet = int(input(f"Player 1, your current coins: {player_coins}. Enter your bet: "))
    player_coins -= player_bet
    pot += player_bet

    # Dealer matches the bet
    dealer_bet = min(dealer_coins, player_bet)
    dealer_coins -= dealer_bet
    pot += dealer_bet

    return player_coins, dealer_coins, pot

def evaluate_hand(hand, community_cards):
    # Combine player's hand with community cards
    all_cards = hand + community_cards

    # Implement hand evaluation logic (you can replace this with a more sophisticated algorithm)
    # For simplicity, we'll just return the cards as the hand ranking
    return all_cards

def display_cards(player_hand, dealer_hand, community_cards, reveal_dealer=False):
    print("\nPlayer's Hand:", player_hand)
    if reveal_dealer:
        print("Dealer's Hand:", dealer_hand)
    else:
        print("Dealer's Hand:", [dealer_hand[0], 'Face Down'])
    print("Community Cards:", community_cards)

def main():
    global player_coins, dealer_coins
    pot = 0

    # Initial deal
    player_hand, dealer_hand = deal_hands(deck)

    # Show player's hand before the first bet
    display_cards(player_hand, dealer_hand, [])

    # First betting round
    player_coins, dealer_coins, pot = betting_round(player_coins, dealer_coins, pot)
    
    # Show hands and community cards
    display_cards(player_hand, dealer_hand, [])

    # Show 3 cards in the middle
    community_cards = deal_community_cards(deck, 3)
    display_cards(player_hand, dealer_hand, community_cards)

    # Second betting round
    player_coins, dealer_coins, pot = betting_round(player_coins, dealer_coins, pot)

    # Show 1 more card in the middle
    community_cards += deal_community_cards(deck, 1)
    display_cards(player_hand, dealer_hand, community_cards)

    # Third betting round
    player_coins, dealer_coins, pot = betting_round(player_coins, dealer_coins, pot)

    # Show the final card in the middle
    community_cards += deal_community_cards(deck, 1)
    display_cards(player_hand, dealer_hand, community_cards)

    # Final betting round
    player_coins, dealer_coins, pot = betting_round(player_coins, dealer_coins, pot)

    # Reveal dealer's second card
    display_cards(player_hand, dealer_hand, community_cards, reveal_dealer=True)

    # Evaluate hands
    player_ranking = evaluate_hand(player_hand, community_cards)
    dealer_ranking = evaluate_hand(dealer_hand, community_cards)

    print("\nPlayer Ranking:", player_ranking)
    print("Dealer Ranking:", dealer_ranking)

    # Determine the winner based on hand rankings
    # (You need to implement a proper hand evaluation function for this part)

    # For simplicity, let's compare the rankings
    if player_ranking > dealer_ranking:
        print("\nPlayer 1 wins!")
        print("Player 1 Highest Hand:", max(player_ranking))
        print("Dealer Highest Hand:", max(dealer_ranking))
        player_coins += pot
    elif player_ranking < dealer_ranking:
        print("\nDealer wins!")
        print("Player 1 Highest Hand:", max(player_ranking))
        print("Dealer Highest Hand:", max(dealer_ranking))
        dealer_coins += pot
    else:
        print("\nIt's a tie! The pot is split.")
        print("Player 1 Highest Hand:", max(player_ranking))
        print("Dealer Highest Hand:", max(dealer_ranking))

    print(f"\nPlayer 1 coins: {player_coins}")
    print(f"Dealer coins: {dealer_coins}")

    # Check if someone has run out of coins
    if player_coins <= 0:
        print("\nPlayer 1 is out of coins. Dealer wins!")
    elif dealer_coins <= 0:
        print("\nDealer is out of coins. Player 1 wins!")

if __name__ == "__main__":
    main()
