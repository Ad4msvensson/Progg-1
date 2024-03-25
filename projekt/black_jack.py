import random

card_values = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 11}
deck ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)

def deal_card(deck):
    return deck.pop()

def calculate_total(hand):
    total = sum(card_values[card] for card in hand)
    for card in hand:
        if card == 'A' and total > 21:
            total -= 10
    return total

def player_turn(deck, player_hand):
    while true:
        player_choice = input("Hit and Stand? ").lower()
        if player_choice == 'Hit':
            player_hand.append(deal_card(deck))
            total = calculate_total(player_hand)
            print("Your hand:", player_hand, "Total:", total)
            if total > 21:
                print("Bust! Du förlorar.")
                return False
            elif  player_choice == 'Stand':
                return True

def dealer_turn(deck, dealer_hand):
    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    return dealer_hand




