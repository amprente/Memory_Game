import tkinter as tk
import random

CARD_WIDTH = 50
CARD_HEIGHT = 100
NUM_CARDS = 16

class MemoryGame:
    """
    MemoryGame class

    This class represents the memory game. 
    It contains the logic for handling the game state, such as keeping track of which cards have been exposed and which cards have been matched. 
    It also contains methods for drawing the cards on the screen and responding to user input.
    """

    def __init__(self, master):
        """
        Initialize the MemoryGame

        Args:
            master (tk.Tk): The main window of the application
        """
        self.master = master
        self.master.title("Memory Game")

        self.canvas = tk.Canvas(master, width=NUM_CARDS * CARD_WIDTH, height=CARD_HEIGHT)
        self.canvas.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        self.deck = list(range(NUM_CARDS // 2)) * 2
        random.shuffle(self.deck)

        self.exposed = [False] * NUM_CARDS

        self.state = 0
        self.card1 = None
        self.card2 = None
        self.counter = 0
        self.score_label = tk.Label(master, text="Turns: 0", font=("Helvetica", 16))
        self.score_label.pack()

        self.draw_board()

        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        """
        Draw the memory game board

        This method draws the board on the screen, using a rectangle for each card and a text label for the card value. 
        The exposed cards are drawn in white, while the unexposed cards are drawn in tan.
        """
        for i, card in enumerate(self.deck):
            if self.exposed[i]:
                self.canvas.create_rectangle(i * CARD_WIDTH, 0, (i + 1) * CARD_WIDTH, CARD_HEIGHT, fill="White")
                self.canvas.create_text((i + 0.5) * CARD_WIDTH, CARD_HEIGHT / 2, text=str(card), fill="Black", font=("Helvetica", 16))
            else:
                self.canvas.create_rectangle(i * CARD_WIDTH, 0, (i + 1) * CARD_WIDTH, CARD_HEIGHT, fill="Tan")

    def on_click(self, event):
        """
        Handle a click on the memory game board

        This method is called when the user clicks on the memory game board. 
        It checks to see if the clicked card is exposed, and if not, it marks it as exposed and sets the state to "card1". 
        If the clicked card is already exposed, and the state is "card1", it marks the clicked card as "card2" and sets the state to "card2". 
        If the state is "card2", it checks to see if the two cards match. 
        If they do, they are uncovered and the state is reset to "card1". If they don't match, the cards are covered and the state is reset to "card1".
        """
        index = event.x // CARD_WIDTH
        if not self.exposed[index]:
            if self.state == 0:
                self.exposed[index] = True
                self.card1 = index
                self.state = 1
            elif self.state == 1:
                self.exposed[index] = True
                self.card2 = index
                self.state = 2
                self.counter += 1
                self.score_label.config(text="Turns: " + str(self.counter))
                self.master.after(1000, self.check_match)
            else:
                self.exposed[index] = True
                if self.deck[self.card1]!= self.deck[self.card2]:
                    self.exposed[self.card1] = False
                    self.exposed[self.card2] = False
                self.card1 = index
                self.state = 1
            self.canvas.delete("all")
            self.draw_board()

    def check_match(self):
        """
        Check if the two selected cards match

        This method is called after each click, and it checks to see if the two selected cards match. 
        If they do, they are uncovered and the state is reset to "card1". I
        f they don't match, the cards are covered and the state is reset to "card1".
        """
        if self.deck[self.card1]!= self.deck[self.card2]:
            self.exposed[self.card1] = False
            self.exposed[self.card2] = False
        self.state = 0
        self.card1 = None
        self.card2 = None
        self.canvas.delete("all")
        self.draw_board()

    def reset_game(self):
        """
        Reset the memory game

        This method resets the memory game by shuffling the deck of cards, resetting the exposed cards list, setting the state and card variables to None, and updating the score label.
        """
        self.deck = list(range(NUM_CARDS // 2)) * 2
        random.shuffle(self.deck)

        self.exposed = [False] * NUM_CARDS

        self.state = 0
        self.card1 = None
        self.card2 = None
        self.counter = 0
        self.score_label.config(text="Turns: 0")

        self.canvas.delete("all")
        self.draw_board()

def main():
    """
    Main function

    This function is the entry point of the memory game. 
    It creates the main window, creates an instance of the MemoryGame class, and starts the main loop of the application.
    """
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
