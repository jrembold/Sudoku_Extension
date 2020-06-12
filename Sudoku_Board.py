"""
Sudoku Board
"""
import arcade
import Cameron
import time
from datetime import date
from BoardGeneration import SuDoku

# Call today's date and convert to a string
todaydt = date.today()
today = todaydt.strftime("%d-%m-%Y")


# Set how many rows and columns we will have
SIZE = 9
ROW_COUNT = SIZE
COLUMN_COUNT = SIZE

# Divisions
DIV_ROW = 3
DIV_COL = 3

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 100
HEIGHT = 100

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 6

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Suduko Board 6x6"

# Instructions that print ot the terminal
print("Welcome to Arcade Sudoku!")
print("Instructions:")
print("- Press the number on your keyboard that you would like to enter.")
print("- Click the box in which you would like to enter the number.")
print("-------------------------------------------------")
print("| To generate a hint      | Press the 'h' key   |")
print("-------------------------------------------------")
print("| To save game to         |                     |")
print("| continue later          | Press the 's' key   |")
print("-------------------------------------------------")
print("| To check your solution  |                     |")
print("| after completing board  | Press the 'c' key   |")
print("-------------------------------------------------")
print("| To close game           | Press the 'Esc' key |")
print("-------------------------------------------------")

name = input("Name: ")
game = input("New game or continue saved game? Input 'N' for new game and 'S' for : ")
if game == "N":
    new = True
    difficulty = input(
        "To select difficulty level, input 'easy', 'medium', or 'hard': "
    )
elif game == "S":
    new = False
    file = input("Type in the exact name of the file (including .txt): ")


if new == False:
    s = open(file, "r")
    all = s.readlines()
    answer = all[0].strip("\n")
    progress = all[1].strip("\n")


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        ## INIT FUNCTION ##
        super().__init__(width, height, title)

        ## APPENDING THE SPRTIES ##
        self.shape_list = None
        self.num_key = 0

        self.win = arcade.load_texture("Numbers/won.png")
        self.lost = arcade.load_texture("Numbers/lost.png")

        # Define variables to check for completeness and accuracy
        self.done = False
        self.correct = False
        self.incorrect = False

        self.current_selected = None

        # If continuing saved game, convert strings from saved game file to lists and set equal to self.grid and self.fixed_answer
        if new == False:
            self.fixed_answer = Cameron.str_to_list(answer)
            self.grid = Cameron.str_to_list(progress)
        # If starting new game, generate unique board and save solution to text file
        elif new == True:
            self.board = SuDoku(SIZE, (DIV_ROW, DIV_COL), difficulty)
            self.answer = self.board.get_solution()
            self.grid = self.board.get_puzzle()
            self.fixed_answer = self.answer

        ## GENERATES BACKGROUND ##
        arcade.set_background_color(arcade.color.BLACK)
        self.recreate_grid()

    # Changing the color of the squares and placing them
    def recreate_grid(self):
        """
        This takes a list of numbers for each row/column
        and populates a SpriteList based on what is in each row/column

        """

        self.print_numlist = arcade.SpriteList()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                sprite = arcade.Sprite(
                    f"Numbers/{self.grid[row][column]}.png", scale=0.2
                )
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                sprite.center_x = x
                sprite.center_y = y
                self.print_numlist.append(sprite)
        # Check to see if all squares have been filled in
        if 0 not in self.grid:
            # if Cameron.Check_for_Completion(self.grid) == True:
            self.done = True

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        self.print_numlist.draw()

        ## Row/Column/Section Indicators
        if self.current_selected:
            x = self.current_selected[1] * (WIDTH + MARGIN) + MARGIN / 2
            y = self.current_selected[0] * (HEIGHT + MARGIN) + MARGIN / 2
            # Row
            arcade.draw_lrtb_rectangle_filled(
                0, SCREEN_WIDTH, y + HEIGHT + MARGIN, y, (200, 0, 0, 20)
            )
            # Column
            arcade.draw_lrtb_rectangle_filled(
                x, x + WIDTH + MARGIN, SCREEN_HEIGHT, 0, (0, 200, 0, 20)
            )
            # Section
            sec_row = self.current_selected[0] // DIV_ROW
            sec_col = self.current_selected[1] // DIV_COL
            start_x = sec_col * (WIDTH + MARGIN) * DIV_COL
            start_y = sec_row * (HEIGHT + MARGIN) * DIV_ROW
            end_x = start_x + (WIDTH + MARGIN) * DIV_COL
            end_y = start_y + (HEIGHT + MARGIN) * DIV_ROW
            arcade.draw_lrtb_rectangle_filled(
                start_x, end_x, end_y, start_y, (0, 0, 200, 20)
            )

        ## LINES SEPARATING THE GRID ##
        # Horizontal
        for i in range(SIZE // DIV_ROW + 1):
            yloc = (i / DIV_COL) * SCREEN_HEIGHT
            arcade.draw_line(0, yloc, SCREEN_WIDTH, yloc, arcade.color.SILVER, 7)

        # Vertical
        for i in range(SIZE // DIV_COL + 1):
            xloc = (i / DIV_ROW) * SCREEN_WIDTH
            arcade.draw_line(xloc, 0, xloc, SCREEN_HEIGHT, arcade.color.SILVER, 7)

        # Final screen telling user if they won or lost
        if self.correct == True:
            arcade.draw_lrwh_rectangle_textured(
                0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.win
            )

        elif self.incorrect == True:
            arcade.draw_lrwh_rectangle_textured(
                0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.lost
            )

    def on_update(self, dt):
        """
        Continually check if done and if so run the checker and
        display the final message.
        """
        if self.done:
            if (self.grid == self.answer).all():
                self.correct = True
            else:
                self.incorrect = True

    def on_key_press(self, key, mod):
        """
        The user will press a number on their keyboard
        that number will be used to generate a new sprite
        """
        ## Hint Generator
        if key == arcade.key.H:
            self.grid = Cameron.Hint_Generator(self.grid, self.fixed_answer)
            self.recreate_grid()

        # Close window
        elif key == arcade.key.ESCAPE:
            arcade.close_window()

        # Check accuracy after filling in all the squares
        elif key == arcade.key.C:
            if (self.grid == self.answer).all():
                # if Cameron.Check_Accuracy(self.fixed_answer, self.grid) == True:
                print("You won!")
                self.correct = True
            else:
                print("Incorrect :(")
                self.incorrect = True

        # Save progress to a text file
        elif key == arcade.key.S:
            s = open(name + "_" + today + ".txt", "w")
            s.write(str(self.fixed_answer) + "\n")
            s.write(str(self.grid))
            s.close()

        ## NUMBERS TO PRESS TO GENERATE BOARD ##
        elif key in range(arcade.key.KEY_1, arcade.key.KEY_9 + 1):
            if self.current_selected:
                self.grid[self.current_selected] = key % arcade.key.KEY_1 + 1

        elif key == arcade.key.BACKSPACE:
            if self.current_selected:
                self.grid[self.current_selected] = 0
        self.recreate_grid()
        # elif key == arcade.key.KEY_1:
        # self.num_key = 1
        # return self.num_key

        # elif key == arcade.key.KEY_2:
        # self.num_key = 2
        # return self.num_key

        # elif key == arcade.key.KEY_3:
        # self.num_key = 3
        # return self.num_key

        # elif key == arcade.key.KEY_4:
        # self.num_key = 4
        # return self.num_key

        # elif key == arcade.key.KEY_5:
        # self.num_key = 5
        # return self.num_key

        # elif key == arcade.key.KEY_6:
        # self.num_key = 6
        # return self.num_key

        # elif key == arcade.key.KEY_7:
        #    self.num_key = 7
        #    return self.num_key

    #
    # elif key == arcade.key.KEY_8:
    #    self.num_key = 8
    #    return self.num_key
    #
    # elif key == arcade.key.KEY_9:
    #    self.num_key = 9
    #    return self.num_key

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        The user will press a number on their keyboard
        then that number will be placed on the board. 
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        #     print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        # AKA: make sure you are clicking w/in the grid - TH
        if row < ROW_COUNT and column < COLUMN_COUNT:
            # Flip the location between 1 and 0.
            # this will reset value for the recreate grid
            # and change the color  - TH
            # if self.grid[row][column] == 0:
            # self.grid[row][column] = self.num_key
            # else:
            # self.grid[row][column] = 0
            self.current_selected = (row, column)

        self.recreate_grid()


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()

