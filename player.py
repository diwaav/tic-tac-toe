# author: Diwa Ashwini Vittala
# date: 12-09-2020
# file: player.py a Python program used in the tic-tac-toe game

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
            return self.sign
      def get_name(self):
            # return an instance name
            return self.name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # you can do the conversion here in the player.py or in the board.py
            # this implementation is up to you

            correct = False
            while correct==False:
                cell = input(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: \n").upper()
                if cell in ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]:
                    if board.isempty(cell):
                        board.set(cell, self.sign)
                        correct = True
                    else:
                        print("You did not choose correctly.")
                else:
                    print("You did not choose correctly.")
