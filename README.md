"""
Memory Game

This is a simple memory game that uses Python and the Tkinter library. 
The game consists of a deck of cards, which are flipped over one at a time. 
The player tries to remember the location of two matching cards, and when they click on a card, the game checks to see if it matches the previously selected card. 
If the cards match, they are uncovered and remain visible for the next turn. 
If the cards do not match, they are covered again and the player has another chance to find a match. 
The game ends when all cards have been matched or when the player runs out of turns.

How to Play:
1. Start the game by clicking the "Reset" button.
2. The cards will be hidden and the score will be set to 0.
3. Click on a card to flip it over. If this is the first card you've clicked, it will be marked as "card1". If it's a different card, it will be marked as "card2".
4. If you click on a card that matches the previously selected card, the cards will be uncovered and remain visible for the next turn. 
   If they don't match, the cards will be covered and you'll have another chance to find a match.
5. After each turn, the score will increase by 1.
6. Continue flipping over cards and trying to find matches until all cards are matched or you run out of turns.
7. When you're done, click the "Reset" button to start a new game.

Note: The game uses a shuffled deck of cards, so each time you play, the cards will be in a different order.

"""
