"""
Sudoku Board

Show how to use a two-dimensional list/array to back the display of a
grid on-screen.

Faster drawing of a board. 

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.array_backed_grid_buffered
"""
import arcade

# Set how many rows and columns we will have
ROW_COUNT = 6
COLUMN_COUNT = 6

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 6

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Suduko Board 6x6"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        super().__init__(width, height, title)

        self.shape_list = None
        self.num_key = 0

        self.num_list = []
        self.zero = arcade.Sprite('Numbers/0.png',  scale= 0.2)
        self.one = arcade.Sprite('Numbers/1.png', scale= 0.2)
        self.two = arcade.Sprite('Numbers/2.png', scale= 0.2)
        self.three = arcade.Sprite('Numbers/3.png',scale= 0.2)
        self.four = arcade.Sprite('Numbers/4.png',  scale= 0.2)
        self.five = arcade.Sprite('Numbers/5.png',  scale= 0.2)
        self.six = arcade.Sprite('Numbers/6.png',  scale= 0.2)
        #self.seven = arcade.Sprite('Numbers/7.png', scale= 0.2)
        #self.eight = arcade.Sprite('Numbers/8.png', scale= 0.2)
        #self.nine = arcade.Sprite('Numbers/9.png',  scale= 0.2)
        self.num_list.append(self.zero)
        self.num_list.append(self.one)
        self.num_list.append(self.two)
        self.num_list.append(self.three)
        self.num_list.append(self.four)
        self.num_list.append(self.five)
        self.num_list.append(self.six)
        #self.num_list.append(self.seven)
        #self.num_list.append(self.eight)
        #self.num_list.append(self.nine)
        self.print_numlist = arcade.SpriteList()


        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)
        self.recreate_grid()

    #Changing the color of the squares and placing them
    def recreate_grid(self):
        #self.shape_list = arcade.ShapeElementList()
        print(self.num_key)
        print(self.grid)
        print(len(self.print_numlist))
        self.print_numlist = arcade.SpriteList()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                sprite = arcade.Sprite(f'Numbers/{self.grid[row][column]}.png', scale = 0.2)
                
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                sprite.center_x = x
                sprite.center_y = y
                self.print_numlist.append(sprite)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        #self.shape_list.draw()
        self.print_numlist.draw()

    def on_key_press(self, key, mod):
        if key == arcade.key.ESCAPE:
            arcade.close_window()
        
        elif key == arcade.key.KEY_1:
            self.num_key = 1
            return self.num_key

        elif key == arcade.key.KEY_2:
            self.num_key = 2
            return self.num_key

        elif key == arcade.key.KEY_3:
            self.num_key = 3
            return self.num_key

        elif key == arcade.key.KEY_4:
            self.num_key = 4
            return self.num_key

        elif key == arcade.key.KEY_5:
            self.num_key = 5
            return self.num_key

        elif key == arcade.key.KEY_6:
            self.num_key = 6
            return self.num_key

        #elif key == arcade.key.KEY_7:
        #    self.num_key = 7
        #    return self.num_key
#
        #elif key == arcade.key.KEY_8:
        #    self.num_key = 8
        #    return self.num_key
        #
        #elif key == arcade.key.KEY_9:
        #    self.num_key = 9
        #    return self.num_key

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        # AKA: make sure you are clicking w/in the grid - TH
        if row < ROW_COUNT and column < COLUMN_COUNT:
            #print(f'Center-x of num_key', self.num_key.center_x, '. Center-y of num_key', self.num_key.center_y)
            #print(f'Name of pic', str(self.num_key))
            # Flip the location between 1 and 0.
            # this will reset value for the recreate grid
            # and change the color  - TH
            if self.grid[row][column] == 0:
                self.grid[row][column] = self.num_key
            else:
                self.grid[row][column] = 0

        self.recreate_grid() 



def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()