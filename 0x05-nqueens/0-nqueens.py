#!/usr/bin/python3
"""
A program that solves the N queens puzzle.

The N queens puzzle is the challenge of placing N chess queens on an N x N
chessboard such that no two queens attack each other on the board. This means
that no two queens can be placed on the same row, column, or diagonal on the
chessboard.
"""
import sys


class NQueens:
    """
    A class representing a particular board dimension.

    Attributes:
        N (int) :
            The dimension of the chess board, which also corresponds to
            the number of queens that must be placed on the board.

        solutions (list) :
            A list of every possible solution for a board with the given
            dimension.

    Methods:
        def __init__(self, N):
            Initializes a new board with the given attribute.

        def solve(self, queens=[], dif=[], sum=[]):
            Determines all the possible solutions to the board.

        def format_solutions(self):
            Re-writes the list of solutions according to a given format.

        def get_solutions(self):
            Prints out the list of solutions.
    """

    def __init__(self, N):
        """
        Initializes a new board with the given attribute.

        Args:
            N (int) :
                The dimension of the chess board, which also corresponds to
                the number of queens that must be placed on the board.

            solutions (list) :
                A list of every possible solution for a board with the given
                dimension. After instantiation, this list is empty until the
                solve method is called.
        """
        self.N = N
        self.solutions = []

    def solve(self, queens=[], dif=[], sum=[]):
        """
        Determines all the possible solutions to the board.

        The method employs the back-tracking algorithm technique.

        Args:
            queens (list) :
                The current queen placements on the board. It is empty at the
                start but increases in length as the algorithm continues. Once
                its length becomes equal to the size of the board N, a
                complete solution has been found and it is appended to the
                general list of solutions.

            dif (list) :

            sum (list) :
        """
        row = len(queens)
        if row == self.N:
            self.solutions.append(queens)
            return
        for col in range(self.N):
            if (col not in queens and
               row - col not in dif and row + col not in sum):
                a = queens + [col]
                b = dif + [row - col]
                c = sum + [row + col]
                self.solve(a, b, c)

    def format_solutions(self):
        """
        Re-writes the list of solutions according to a given format.

        For each solution, the solution is printed acording to the format
        : [board_row, queen_position], for each queen placement.
        After the formatting operation, the solutions-attribute is updated.
        """
        final_list = []
        for solution in self.solutions:
            tmp = []
            for i in range(len(solution)):
                tmp.append([i, solution[i]])
            final_list.append(tmp)

        self.solutions = final_list

    def get_solutions(self):
        """
        Prints out the list of solutions.

        One solution per line.
        """
        for solution in self.solutions:
            print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    else:
        board = NQueens(N)
        board.solve()
        board.format_solutions()
        board.get_solutions()
