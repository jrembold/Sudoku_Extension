import numpy as np
import random


class SuDoku:
    def __init__(self, size: int, div: tuple = (3, 3), difficulty: str = "medium"):
        self.size = size
        # I set these scaling numbers by estimating the difficulties myself, so...
        if difficulty == "medium":
            self.difficulty = int((self.size / 1.45) ** 2)
        elif difficulty == "hard":
            self.difficulty = int((self.size / 1.25) ** 2)
        else:
            self.difficulty = int((self.size / 2) ** 2)
        print(self.difficulty)
        self.divs = div  # (rows,col)
        if div[0] * div[1] != size:
            raise ValueError("Can not split puzzle into requested sections")
        self.seed = self.generate_seed()
        self.puzzle = None
        self.working = None
        self.solution = None
        self.attempted_solutions = []

        self.generate_puzzle(self.difficulty)

    def __repr__(self):
        return self.display(self.puzzle)

    def display(self, puzzle_array):
        """
        Display the sudoku puzzle nicely
        """
        numcol_lines = self.size // self.divs[1] - 1
        string = ""
        for jnd, row in enumerate(puzzle_array):
            if jnd % self.divs[0] == 0 and jnd != 0:
                string += "-" * (self.size * 3 + numcol_lines) + "\n"
            for ind, col in enumerate(row):
                if ind % self.divs[1] == 0 and ind != 0:
                    string += "|"
                string += f"{col:^3d}"
            string += "\n"
        return string

    def get_puzzle(self):
        return self.puzzle

    def get_solution(self):
        return self.solution

    def display_puzzle(self):
        print(self.display(self.puzzle))

    def display_solution(self):
        print(self.display(self.solution))

    def guess_in_row(self, guess: int, coordinate: tuple):
        """
        Checks to see if any identical values to guess exist in row

        Inputs:
            guess (int): the number attempting to be placed
            coordinate (tuple): the location to place the guess
        Outputs:
            (bool): is another number equal to guess already in row
        """
        return guess in self.working[coordinate[0], :]

    def guess_in_column(self, guess: int, coordinate: tuple):
        """
        Checks to see if any identical values to guess exist in column

        Inputs:
            guess (int): the number attempting to be placed
            coordinate (tuple): the location to place the guess
        Outputs:
            (bool): is another number equal to guess already in column
        """
        return guess in self.working[:, coordinate[1]]

    def guess_in_section(self, guess: int, coordinate: tuple):
        """
        Checks to see if any identical values to guess exist in
        current 3x3 square.

        Inputs:
            guess (int): the number attempting to be placed
            coordinate (tuple): the location to place the guess
        Outputs:
            (bool): is another number equal to guess already in section
        """
        r, c = coordinate
        section_row = r // self.divs[0]
        section_col = c // self.divs[1]
        ssr, ssc = section_row * self.divs[0], section_col * self.divs[1]
        section = self.working[ssr : ssr + self.divs[0], ssc : ssc + self.divs[1]]
        return guess in section.ravel()

    def find_viable_number(self, coordinate: tuple, start=1):
        """
        Starting at some initial value (defaults to 1) increments upwards,
        checking to see if that number would be a viable candidate for the
        indicated location.

        Input:
            coordinate (tuple): the (row, column) of the desired location to fill
            start (int): where the counting should begin
        Output:
            (bool): True if successful and a number is found, false if one is not found
        """
        for i in range(start, self.size + 1):
            # print(f"Checking {i}:")
            if not self.guess_in_row(i, coordinate):
                # print("Not in the row!")
                if not self.guess_in_column(i, coordinate):
                    # print("Not in the column!")
                    if not self.guess_in_section(i, coordinate):
                        # print("Not in the section!")
                        self.attempted_solutions.append((coordinate, i))
                        self.working[coordinate] = i
                        return True
        self.working[coordinate] = 0
        return False

    def find_next_empty(self):
        """
        Finds the next empty cell (filled with a placeholder 0)

        Outputs:
            (tuple) if a point is found, otherwise None
        """
        for r in range(self.size):
            for c in range(self.size):
                if self.working[r, c] == 0:
                    return (r, c)
        return None

    def solve(self):
        """
        Iterative method to compute the full grid. Works far better
        than the original recursive method.
        """
        self.working = self.puzzle.copy()
        pt = self.find_next_empty()
        start = 1
        try:
            while pt:
                success = self.find_viable_number(pt, start)
                if success:
                    pt = self.find_next_empty()
                    start = 1
                else:
                    pt, start = self.attempted_solutions.pop(-1)
            return self.working.copy()
        except IndexError:
            print("Puzzle could not be solved")
            return None

    def generate_seed(self):
        """
        Method to generate puzzle
        """
        board = np.zeros((self.size, self.size), dtype=int)
        # row = random.randint(0, self.size - 1)
        # cols = random.randint(0, self.size - 1)
        # val = random.randint(1, self.size)
        # board[row, cols] = val

        vals = [i for i in range(1, self.size + 1)]
        rows = [i for i in range(self.size)]
        cols = [i for i in range(self.size)]
        random.shuffle(vals)
        random.shuffle(rows)
        random.shuffle(cols)
        for i in range(len(vals)):
            board[rows[i], cols[i]] = vals[i]

        return board

    def generate_puzzle(self, difficulty: int):
        orig_solution = None
        while orig_solution is None:
            self.seed = self.generate_seed()
            self.puzzle = self.seed.copy()
            orig_solution = self.solve()
        self.puzzle = orig_solution.copy()
        count = 0
        attempts = 0
        while count < difficulty and attempts <= self.size ** 2:
            optx, opty = np.where(self.puzzle != 0)
            i = random.randint(0, len(optx) - 1)
            row, col = optx[i], opty[i]
            # row = random.randint(0, self.size - 1)
            # col = random.randint(0, self.size - 1)
            attempts += 1
            temp = self.puzzle[row, col]
            self.puzzle[row, col] = 0
            try:
                new_solution = self.solve()
            except IndexError:
                print(f"Error at ({row},{col}), filling back in {temp}")
                self.puzzle[row, col] = temp
            if (new_solution == orig_solution).all():
                count += 1
            else:
                self.puzzle[row, col] = temp
        self.solution = orig_solution


if __name__ == "__main__":
    P = SuDoku(6, (2, 3))
    P.display_puzzle()
    P.display_solution()
    print(P.difficulty)
