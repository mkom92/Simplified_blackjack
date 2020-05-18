'''

GENERAL OVERVIEW

Create a simplified text-based version of Blackjack
- Deck of 32 cards
- Jack, Queen and King have all value = 10
- Aces can be either 1 or 11, depends on the player preference
- Player places a bet, has a balance
- Bet cannot exceed the balance
- Computer starts with one card faced up and one faced down
- Player starts with both cards faced up
- Goal - get closer to a total value of 21 than the dealer (computer)
- 2 possible action for a player:
    - Hit - receive a card
    - Stay - stop receiving cards
- If a player hits and goes above 21, busts and loses the bet
- Once a player has finished, it's the computer's turn
    - if a player is under 21, dealer hits until it beats the player or busts (over 21)
    - computer beats the player if he hits and scores closer to 21 (while below 21) than player
- If a player wins, doubles the bet money which goes to his balance
- Inform a player if he won, lost, busted etc.

DECK INFORMATION

- 32 cards -> select random 32 cards from the deck of 52 (4x 13), beware of the symbols (max 4 of each kind)
- Jack, Queen and King have all value = 10
- Aces can be either 1 or 11, depends on the player preference

PLAYER

- Select a name
- Start with a pre-defined balance
- Has to bet every round
- If busts - loses bet money
- If wins - get double the bet money
- Can check his balance mid game

EXTRAS
- Try to display cards graphically, ex.:
 ___
|6  |
| ♥ |
|__6|
 ___
|6  |
| ♦ |
|__6|
 ___
|6  |
| ♣ |
|__6|
 ___
|6  |
| ♠ |
|__6|

- Place cards next to each other (unlike above)

'''