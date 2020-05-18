# Main script to run the game

import game_modules as gm

print("BLACKJACK\n")

# Shuffle cards and get 32 cards to a new deck

current_deck = gm.Deck()
table = current_deck.selected_cards

# Get Player data

p1 = gm.Player()

# Create a computer player

c1 = gm.Computer()

print("\n")

# Test a player round

question = "Y"

while p1.balance > 0 and question != "N" and len(current_deck.selected_cards) > 0:

    round_go = "Round goes on"
    question = "Y"

    # Player draws 2 cards

    p1.draw_card(current_deck)
    p1.draw_card(current_deck)
    p1.player_hand()

    # Reveal the hand + hands' value

    print(f"Players' hand:\n{p1.hand}\n{p1.hand_value}\n")

    # Computer draws 2 cards

    c1.draw_card(current_deck)
    c1.draw_card(current_deck)

    # Reveal the first card

    print(f"Computers' hand: {c1.hand[0]}\n")

    p1_bet = gm.bet(p1)

    while round_go == "Round goes on":
        round_go = gm.Player_Round(p1, current_deck)

    print("Result: "+round_go)

    # Here goes computers round IF player didn't bust

    if round_go == "Computer's turn":

        round_go = "Round goes on"

        while round_go == "Round goes on":
            round_go = gm.Computer_Round(c1,p1,current_deck)

    p1.end_round(round_go, p1_bet)
    c1.end_round()

    if p1.balance == 0:
        print("The End!")
    else:
        question = "X"
        while question not in ["N","Y"]:
            question = input("Would you like to continue [Y/N]?\n>")

        if question == "N":
            print("The End!")

if len(current_deck.selected_cards) == 0:
    print("The deck if empty! Thank you for the game!")


print(f"Thank you for playing Blackjack! Your end balance: ${p1.balance}.")