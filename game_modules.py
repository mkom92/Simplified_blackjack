from random import shuffle

class Deck:

    def __init__(self):
        self.whole_deck = []

        signs = ['♥', '♦', '♣', '♠']
        specials = ['A', 'J', 'Q', 'K']

        for i in signs:
            for j in range(2, 11):
                self.whole_deck.append(i + str(j))
            for k in specials:
                self.whole_deck.append(i + k)

        shuffle(self.whole_deck)

        self.selected_cards = self.whole_deck[:32]

    def played_card(self, card):
        self.selected_cards.remove(card)


# Class Player - describing the human player
# Class will include persons Name, Account Balance and available cards in the Hand

class Player:

    def __init__(self):
        self.name = input("Tell me your name, Player:\n>")
        self.hand = []

        hand_p = Hand(self.hand)

        self.hand_value = hand_p.hand_val

        test = 0
        while True:
            try:
                self.balance = int(input("What's your initial balance?\n>"))
                reassurance = input("Are you sure? [Y/N]\n>")
                if reassurance == "Y" and isinstance(self.balance, int):
                    print("Great!")
                    break
                else:
                    continue
            except:
                print("Give me an actual balance, please")

    def end_round(self, result, value):

        if result == "Player won!":
            self.balance += 2*int(value)
            print(f"You won! Your current balance: {self.balance}")
        else:
            self.balance -= value
            print(f"You lost! Your current balance: {self.balance}")

        self.hand = []

    def draw_card(self, deck):
        card = deck.selected_cards[0]

        print(f"You've picked {card}")

        self.hand.append(card)
        deck.played_card(card)

    def player_hand(self):
        hand_p = Hand(self.hand)

        self.hand_value = hand_p.hand_val
        print(self.hand_value)

# Computer doesn't need a balance

class Computer:

    def __init__(self):

        self.hand = []

        hand_c = Hand(self.hand)

        self.hand_value = hand_c.hand_val

    def end_round(self):

        self.hand = []

    def draw_card(self, deck):
        card = deck.selected_cards[0]

        self.hand.append(card)
        deck.played_card(card)

    def computer_hand(self, player):

        hand_c = Hand(self.hand)

        self.hand_value = hand_c.hand_val
        print(self.hand_value)

# Card - includes a code and value of a card

class Card:

    def __init__(self, card):
        self.card = card

        if card[1:] in ['J', 'Q', 'K']:
            self.value = 10
        elif card[1:] == 'A':
            val_q = 0
            while val_q not in ['1', '11']:
                val_q = input(f"Which value should {self.card} take: 1 or 11?\n>")
            self.value = int(val_q)
        else:
            self.value = int(card[1:])

class Hand:

    def __init__(self, hand):

        self.hand_val = 0

        for i in hand:

            c = Card(i)
            self.hand_val += c.value

    def comp_hand(self, c_hand, p_val):

        hand_l = []
        for i in hand_c:

            if i[1:] == "A":
                hand_l.append("x")
            else:
                hand_l.append(i)

def bet(player):

    test = 0
    while test == 0:
        response = "test"
        try:
            response = int(input("How much do you want to bet?\n>"))
            if response > 0 and response <= player.balance:
                test = 1
            else:
                print("Try again")
                continue
        except:
            print("Try again.")

    return response


def PlayerMove(player):

    move = "x"

    while move not in ["Hit","Stay"]:
        move = input("What's your next move: Hit or Stay?\n>")

    return move


def Player_Round(player,deck):

    p_move = PlayerMove(player)

    if p_move == "Hit":
        player.draw_card(deck)
        print(player.hand)
        player.player_hand()

        p_value = player.hand_value

        if p_value > 21:
            round_result = "Bust!"
        elif p_value == 21:
            round_result = "Player won!"
        else:
            round_result = "Round goes on"

    else:
        print(player.hand)
        p_value = player.hand_value
        print(p_value)

        if p_value == 21:
            round_result = "Player won!"
        else:
            round_result = "Computer's turn"

    return round_result
