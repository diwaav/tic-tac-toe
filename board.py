# author: Diwa Ashwini Vittala
# date: 12-09-2020
# file: board.py a Python program used in the tic-tac-toe game

class Board:
    def __init__(self):
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2) #THIS IS A LIST
        self.cells = ("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3")
        # the winner's sign O or X
        self.winner = " "
        
    def get_size(self):
        # optional, return the board size (an instance size)
        return self.size

    def get_winner(self):
        # return the winner's sign O or X (an instance winner)
        return self.winner

    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        index = self.cells.index(cell)
        self.board[index] = sign

    def isempty(self, cell):
        # return True if the cell is empty (not marked with X or O)
        index = self.cells.index(cell)
        #for value in t:
        #index = t.index(" ~ ")
        if self.board[index] == " ":
            return True
        else:
            return False

    def isdone(self):
        done = False
        poss = ["A1", "B1", "C1", "A2", "A3"] #possible ways to check
        for cell in poss:
            i = self.cells.index(cell)
            sign = self.board[i]
            if sign == " ":
                continue
            if i == 0:
                if (sign == self.board[0] and sign == self.board[1] and sign == self.board[2])\
                   or (sign == self.board[0] and sign == self.board[3] and sign == self.board[6])\
                   or (sign == self.board[0] and sign == self.board[4] and sign == self.board[8]):
                    done = True
                    self.winner = self.board[i]
                    break
            elif i==1:
                if (sign == self.board[1] and sign == self.board[0] and sign == self.board[2])\
                   or (sign == self.board[1] and sign == self.board[4] and sign == self.board[7]):
                    done = True
                    self.winner = self.board[i]
                    break
            elif i==2:
                if (sign == self.board[2] and sign == self.board[0] and sign == self.board[1])\
                   or (sign == self.board[2] and sign == self.board[5] and sign == self.board[8])\
                   or (sign == self.board[2] and sign == self.board[4] and sign == self.board[6]):
                    done = True
                    self.winner = self.board[i]
                    break
            elif i==3:
                if sign == self.board[3] and sign == self.board[4] and sign == self.board[5]:
                    done = True
                    self.winner = self.board[i]
                    break
            elif i==6:
                if sign == self.board[6] and sign == self.board[7] and sign == self.board[8]:
                    done = True
                    self.winner = self.board[i]
                    break
            
            if not done:
                done = True
                for sign in self.board:
                    if sign == " ":
                        done = False
                        break
        return done

    def show(self):
        print("\n")
        print("   A   B   C")
        print(" +---+---+---+")
        print("1| {} | {} | {} |".format(self.board[0], self.board[1], self.board[2]))
        print(" +---+---+---+")
        print("2| {} | {} | {} |".format(self.board[3], self.board[4], self.board[5]))
        print(" +---+---+---+")
        print("3| {} | {} | {} |".format(self.board[6], self.board[7], self.board[8]))
        print(" +---+---+---+")




            
