"""
Sudoku Board
"""
import arcade
import Cameron



# Set how many rows and columns we will have
ROW_COUNT = 6
COLUMN_COUNT = 6

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
print('Welcome to Arcade Sudoku!')
print('Instructions:')
print('- Press the number on your keyboard that you would like to enter.')
print('- Click the box in which you would like to enter the number.')
print('--------------------------------------------')
print("| To generate a hint | Press the 'h' key   |")
print("| To close the game  | Press the 'Esc' key |")
print('--------------------------------------------')
difficulty = input("To select difficulty level, input easy, medium, or hard: ")


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

        self.num_list = []
        self.zero = arcade.Sprite('Numbers/0.png')
        self.one = arcade.Sprite('Numbers/1.png') 
        self.two = arcade.Sprite('Numbers/2.png')
        self.three = arcade.Sprite('Numbers/3.png')
        self.four = arcade.Sprite('Numbers/4.png')
        self.five = arcade.Sprite('Numbers/5.png')
        self.six = arcade.Sprite('Numbers/6.png')
        #self.seven = arcade.Sprite('Numbers/7.png')
        #self.eight = arcade.Sprite('Numbers/8.png')
        #self.nine = arcade.Sprite('Numbers/9.png')
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

        ## ANSWER KEY ##
        self.answer = Cameron.Generate_unique_board()
        self.grid = Cameron.Partial_solution(self.answer, difficulty)
        self.fixed_answer = Cameron.read_text('answertext2.txt')
#        a = open('answertext2.txt','r')
#        for line in a:
#            self.fixed_answer = line
#        a.close()

        ## GENERATES BACKGROUND ##
        arcade.set_background_color(arcade.color.BLACK)
        self.recreate_grid()
    


    #Changing the color of the squares and placing them
    def recreate_grid(self):
        '''
        This takes a list of numbers for each row/column
        and populates a SpriteList based on what is in each row/column

        '''
        #self.shape_list = arcade.ShapeElementList()
    #    print("Key pressed: ",self.num_key) #key pressed
    #    print("Current: ",self.grid) #answer grid
    #    print("Answer: ",self.fixed_answer)



        self.print_numlist = arcade.SpriteList()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                sprite = arcade.Sprite(f'Numbers/{self.grid[row][column]}.png', scale = 0.2)
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                sprite.center_x = x
                sprite.center_y = y
                self.print_numlist.append(sprite)
     #   print(Cameron2.Check_for_Completion(self.grid))

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        

        self.print_numlist.draw()

        ## LINES SEPARATING THE GRID ##
        arcade.draw_line(0, (2/3)*SCREEN_HEIGHT, SCREEN_WIDTH,(2/3)*SCREEN_HEIGHT, arcade.color.SILVER, line_width=7)
        arcade.draw_line(0, (1/3)*SCREEN_HEIGHT, SCREEN_WIDTH,(1/3)*SCREEN_HEIGHT, arcade.color.SILVER, line_width=7)
        arcade.draw_line((1/2)*SCREEN_WIDTH, 0, (1/2)*SCREEN_WIDTH,SCREEN_HEIGHT, arcade.color.SILVER, line_width=7)

    def on_key_press(self, key, mod):
        '''
        The user will press a number on their keyboard
        that number will be used to generate a new sprite
        '''
        ## Hint Generator
        if key == arcade.key.H:
            self.grid = Cameron.Hint_Generator(self.grid, self.fixed_answer)
            self.recreate_grid()

        if key == arcade.key.ESCAPE:
            arcade.close_window()

        
        ## NUMBERS TO PRESS TO GENERATE BOARD ##
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
        The user will press a number on their keyboard
        then that number will be placed on the board. 
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