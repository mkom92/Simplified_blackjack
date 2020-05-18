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

while p1.balance > 0 and question != "N":

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

    print(c1.hand[0])

    p1_bet = gm.bet(p1)

    while round_go == "Round goes on":
        round_go = gm.Player_Round(p1, current_deck)


    # Here goes computers round IF player didn't bust

    if round_go == "Computer's turn":

        print("Here comes the Computer part one day")

    p1.end_round(round_go, p1_bet)

    if p1.balance == 0:
        print("The End!")
    else:
        question = "X"
        while question not in ["N","Y"]:
            question = input("Would you like to continue [Y/N]?\n>")

        if question == "N":
            print("The End!")

print(round_go)

print(f"Thank you for playing Blackjack! Your end balance: ${p1.balance}.")