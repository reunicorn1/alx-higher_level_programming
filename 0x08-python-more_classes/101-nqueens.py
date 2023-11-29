#!/usr/bin/python3

"""This module provides the class 'nqueenBoard'

The N queens puzzle is the challange of placing N non attacking
on an N=N chessboard.
"""

import sys


class nqueenBoard:
    """This class  provides the object board with N queens setted
    in default positions.

    This class provides methods to check if queens are safe relatively
    to each other, and also to set the pieces according to their non
    attack positions and print them.

    Attributes:
       size (int): the size of the N*N board.
       queens (list): a list of lists corresponding to queens available.

    The __init__ method sets the attributes of the board.

    Args:
       N: the size of the board, which also determines the number of
       queens.

    """
    def __init__(self, N):
        if not N.isdigit():
            print("N must be a number")
            sys.exit(1)
        if int(N) < 4:
            print("N must be at least 4")
            sys.exit(1)
        self.__size = int(N)
        self.queen = [[_, -1] for _ in range(self.__size)]

    def is_safe(self, index):
        """This method checks if a queen in a certain index is in a
        safe position compared to the queens on its left.

        index (int): the index of the queen in the list self.queen.
        """
        down = up = current = self.queen[index]
        for i in range(index - 1, -1, -1):
            if self.queen[i][1] == current[1]:
                return False
            up = [up[0] - 1, up[1] - 1]
            down = [down[0] - 1, down[1] + 1]
            if self.queen[i] == up or self.queen[i] == down:
                return False
        return True

    def nqueen_setter(self, index):
        """This function adjusts the coordinates of all queens available
        to be in N non-attacking positions.

        Arguments:
           index(int): the index of the queen to be moved.

        Returns:
           the list of the sorted queens
        """
        if index < self.__size:
            for i in range(self.queen[index][1] + 1, self.__size):
                self.queen[index][1] += 1
                if self.is_safe(index):
                    return (self.nqueen_setter(index + 1))
            if index > 0:
                self.queen[index][1] = -1
                return (self.nqueen_setter(index - 1))
            else:
                return None
        else:
            return self.queen

    def defaut(self):
        """This function returns the queens to the default positions
        before being placed in the board.
        """
        for i in range(self.__size):
            self.queen[i][1] = -1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        sys.exit(1)
    board = nqueenBoard(sys.argv[1])
    alist = board.nqueen_setter(0)
    while (alist):
        print(alist)
        save_row = board.queen[0][1]
        board.defaut()
        board.queen[0][1] = save_row
        alist = board.nqueen_setter(0)
