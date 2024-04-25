import random
import itertools

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
suits = ['hearts', 'diamond', 'spades', 'clubs']

deck = list(itertools.product(deck, suits))

random.shuffle(deck)

def deal_card(deck):
    return deck.pop()

def calculate_total(hand):
    total = sum(card_values[card[0]] for card in hand)
    for card in hand:
        if card[0] == 'A' and total > 21:
            total -= 10
    return total

def player_turn(deck, player_hand):
    while True:
        player_choice = input("Hit or Stand? ").lower()
        if player_choice == 'hit':
            player_hand.append(deal_card(deck))
            total = calculate_total(player_hand)
            print("Din hand:", player_hand, "Total:", total)
            if total > 21:
                print("Bust! DU förlorar.")
                return False
        elif player_choice == 'stand':
            return True



  

def dealer_turn(deck, dealer_hand):
    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    return dealer_hand

def blackjack():
    while True: 
      player_hand = [deal_card(deck), deal_card(deck)]
      dealer_hand = [deal_card(deck), deal_card(deck)]

      print("Din hand:", player_hand, "Total:", calculate_total(player_hand))
      print("Dealer's hand:", [dealer_hand[0], '??'], "Total:", card_values[dealer_hand[0][0]])

      if player_turn(deck, player_hand):
          dealer_turn(deck, dealer_hand)

          player_total = calculate_total(player_hand)
          dealer_total = calculate_total(dealer_hand)

          print("Din hand:", player_hand, "Total:", player_total)
          print("Dealer's hand:", dealer_hand, "Total:", dealer_total)

          if player_total > 21:
              print("Du förlorar!")
          elif dealer_total > 21 or player_total > dealer_total:
              print("Du vinner!")
          elif player_total == dealer_total:
              print("Det är lika!")
          else:
              print("Du förlorar!")

          play_again = input("Vill du spela igen? (Ja/Nej): ").lower()
          if play_again != 'ja':
              break

blackjack()
