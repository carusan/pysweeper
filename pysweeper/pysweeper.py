"""
PySweeper
Creator: Andrea C.
"""


from tkinter import *
# The 'random' module is needed for the randomised tile generation.
import random


class Minesweeper:
    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title("PySweeper by carusan")
        self.__main_window["background"] = "light grey"
        self.__main_window["cursor"] = "dot"
        # The window is made un-resizable.
        self.__main_window.resizable(False, False)
        # Defining a blank "dummy image" to force tiles to be square.
        self.__i = PhotoImage()

        self.__option_frame = Frame(self.__main_window,
                                    relief="ridge",
                                    background="light grey",
                                    border=5,
                                    width=71,
                                    cursor="pencil")

        self.__difficulty = StringVar()
        self.__difficulty.set("medium")

        selected_difficulty = self.__difficulty

        # Creating the function in charge of changing the difficulty to
        # the difficulty selected by the user. This function also resets
        # the score counter. The <event> dummy parameter is only needed
        # to fulfill syntax requirements.
        def selected(event):
            self.create_minefield(selected_difficulty.get())
            self.__score = 0
            self.__score_counter["text"] = f"Score: {self.__score}"

        # The 'selected()' function is called at the press of one of
        # this drop-down menu's options.
        self.__set_difficulty = OptionMenu(self.__option_frame,
                                           selected_difficulty,
                                           "easy",
                                           "medium",
                                           "hard",
                                           command=selected)

        self.__set_difficulty["font"] = "System"
        self.__set_difficulty["background"] = "light grey"
        self.__set_difficulty["border"] = 1
        self.__set_difficulty["borderwidth"] = 3

        self.__set_difficulty.grid(row=2,
                                   column=1,
                                   columnspan=1,
                                   sticky=NSEW)

        # In order to be able to recreate a new minefield when the user
        # changes difficulty, the minefield creation is executed through
        # a method '.create_minefield()'.
        self.create_minefield(selected_difficulty.get())

        self.__score = 0
        self.__score_counter = Label(self.__option_frame,
                                     text=f"Score: {self.__score}",
                                     font="System",
                                     background="black",
                                     foreground="white",
                                     borderwidth=3,
                                     width=65,
                                     relief="sunken")

        self.__score_counter.grid(row=1,
                                  column=1,
                                  columnspan=3)

        self.__quit_button = Button(self.__option_frame,
                                    text="quit",
                                    font="System",
                                    background="light grey",
                                    borderwidth=3,
                                    command=self.quit)

        self.__quit_button.grid(row=2,
                                column=3,
                                sticky=NSEW)

        self.__refresh_button = Button(self.__option_frame,
                                       text="refresh",
                                       font="System",
                                       background="light grey",
                                       border=1,
                                       borderwidth=3,
                                       command=self.restart)

        self.__refresh_button.grid(row=2,
                                   column=2,
                                   columnspan=1,
                                   sticky=NSEW)

        self.__option_frame.pack(side=BOTTOM)

        self.__main_window.mainloop()

    def create_minefield(self, difficulty):
        """
        This method creates the minefield according to the chosen
        difficulty, the previous minefield, if it exists, is removed
        from existence to avoid overlapping minefield grids. The tiles
        used in the grid are all buttons whose positions are logged
        using a matrix (2-dimensional list). Another matrix is used to
        keep track of whether the given tile is a mine or a safe tile.

        :param difficulty: str, either "easy", "medium", or "hard"
                           depending on the level of challenge the user
                           wants in their game.
        """
        # Trying to destroy the previous minefield if it exists to avoid
        # minefields overlapping and causing, to put it in technical
        # terms, a mess.
        try:
            self.__minefield.destroy()
        except AttributeError:
            pass

        # The "pool" from which the tiles are selected are generated as
        # long lists containing both safe tiles and mine tiles. The
        # randomiser implemented later on will pick one of the list
        # entries at (pseudo) random and removes the selected tile from
        # the "pool".
        if difficulty == "easy":
            self.__minefield_width = 9
            self.__minefield_height = 9
            self.__max_score = 71
            self.__tile_pool = []
            for tile in range(71):
                self.__tile_pool.append("safe")
            for tile in range(10):
                self.__tile_pool.append("mine")

        elif difficulty == "medium":
            self.__minefield_width = 16
            self.__minefield_height = 16
            self.__max_score = 216
            self.__tile_pool = []
            for tile in range(216):
                self.__tile_pool.append("safe")
            for tile in range(40):
                self.__tile_pool.append("mine")

        elif difficulty == "hard":
            self.__minefield_width = 30
            self.__minefield_height = 16
            self.__tile_pool = []
            self.__max_score = 381
            for tile in range(381):
                self.__tile_pool.append("safe")
            for tile in range(99):
                self.__tile_pool.append("mine")

        # The minefield is created as a frame to aid in the indexing.
        self.__minefield = Frame(self.__main_window,
                                 relief="ridge",
                                 border=5,
                                 background="light grey",
                                 cursor="cross")

        width = self.__minefield_width
        height = self.__minefield_height
        tile_pool = self.__tile_pool

        self.__tiles = []
        self.__tile_type = []

        # Creating the matrices for logging the positions of the tiles.
        for row in range(height):
            self.__tiles.append([None] * width)
            self.__tile_type.append([None] * width)

        for row in range(height):
            for column in range(width):

                # The program takes tiles at random from the predefined
                # tile "pool" and places either the tiles, whether safe
                # tile or mine tile, into the grid. The tile is then
                # removed from the selection pool, so it can't be picked
                # again. This ensures an exact number of each type of
                # tile on the grid.
                if random.choice(tile_pool) == "mine":
                    def mine_press(x=row, y=column):
                        self.press_mine(x, y)

                    mine_tile = Button(self.__minefield,
                                       text=" ",
                                       font=("System", 15),
                                       image=self.__i,
                                       compound="center",
                                       background="light grey",
                                       height=23,
                                       width=23,
                                       borderwidth=3,
                                       command=mine_press)

                    self.__tiles[row][column] = mine_tile
                    mine_tile.grid(row=row, column=column)
                    self.__tile_type[row][column] = "mine"
                    tile_pool.remove("mine")
                else:
                    def safe_press(x=row, y=column):
                        self.press_safe(x, y)

                    safe_tile = Button(self.__minefield,
                                       text=" ",
                                       font=("System", 15),
                                       image=self.__i,
                                       compound="center",
                                       background="light grey",
                                       fg="yellow",
                                       height=23,
                                       width=23,
                                       borderwidth=3,
                                       command=safe_press)

                    self.__tiles[row][column] = safe_tile
                    safe_tile.grid(row=row, column=column)
                    self.__tile_type[row][column] = "safe"
                    tile_pool.remove("safe")

        self.__minefield.pack(side=TOP)

    def press_safe(self, x, y):
        """
        When a safe tile is clicked on, this function is called, which
        performs a check of the 8 tiles adjacent to the current one to
        see if there are any  mine tiles nearby, the number of mine
        tiles adjacent to the pressed tile is printed on the pressed
        tile and the pressed tile is disabled, the player can continue
        the game seamlessly. If the player presses the last safe tile,
        the game ends with a victory. The board is painted green and the
        score is displayed alongside a message confirming the victory.

        :param x: int, the x-coordinate of the pressed tile.
        :param y: int, the y-coordinate of the pressed tile.
        """
        # This code checks for mine tiles adjacent to the pressed tile
        # if the indexing is unsuccessful due to reaching an edge the
        # check is passed as there is not the possibility of  a mine
        # being in the wall.
        mine_counter = 0
        for x_check in [x - 1, x, x + 1]:
            for y_check in [y - 1, y, y + 1]:
                if x_check < 0 or y_check < 0:
                    pass
                else:
                    try:
                        if self.__tile_type[x_check][y_check] == "mine":
                            mine_counter += 1
                    except IndexError:
                        pass

        # The tile is replaced with a non-functional copy if itself
        # which displays the number of adjacent mine tiles.
        self.__tiles[x][y]["state"] = DISABLED
        self.__tiles[x][y]["text"] = f"{mine_counter}"
        self.__tiles[x][y]["relief"] = "sunken"
        self.__tiles[x][y]["background"] = "grey"

        self.__tiles[x][y].grid(row=x, column=y)

        if self.__tiles[x][y]["state"] == DISABLED:
            self.__score += 1
        self.__score_counter["text"] = f"Score: {self.__score}"

        width = self.__minefield_width
        height = self.__minefield_height

        # The following code checks whether all the safe tiles have been
        # disabled, if so, the game ends with a victory for the user and
        # the total score is given.
        if self.__score == self.__max_score:

            for row in range(height):
                for column in range(width):
                    self.__tiles[row][column]["state"] = DISABLED
                    self.__tiles[row][column]["background"] = "green"

            self.__score_counter["text"] = f"You WIN! Final score: " \
                                           f"{self.__score}"

    def press_mine(self, x, y):
        """
        When a mine tile is pressed, this function is called, which
        swiftly and mercilessly ends the game for the unsuspecting
        player. As the mine tile is pressed, all the board tiles are
        rendered un-clickable and all the mine tiles are displayed as
        red tiles on with an '×' on them for informational purposes and
        the playe's score is displayed alongside a message reminding the
        player of their failure to beat the game.

        :param x: int, the x-coordinate of the pressed tile.
        :param y: int, the y-coordinate of the pressed tile.
        """
        self.__tiles[x][y]["state"] = DISABLED
        self.__tiles[x][y]["text"] = "×"
        self.__tiles[x][y]["relief"] = "sunken"

        self.__tiles[x][y].grid(row=x, column=y)

        width = self.__minefield_width
        height = self.__minefield_height

        for row in range(height):
            for column in range(width):
                self.__tiles[row][column]["state"] = DISABLED
                if self.__tile_type[row][column] == "mine":
                    self.__tiles[row][column]["background"] = "red"
                    self.__tiles[row][column]["text"] = "\u00D7"

        self.__score_counter["text"] = f"You LOSE! Final score: " \
                                       f"{self.__score}"

    def restart(self):
        """
        Reloads the same game grid for a new game, this function should
        be called after each loss, victory or any time the player wishes
        to abandon the current game to start anew. The game score is
        also reset.
        """
        self.create_minefield(self.__difficulty.get())
        self.__score = 0
        self.__score_counter["text"] = f"Score: {self.__score}"

    def quit(self):
        """
        Quits the game by directly closing the game window.
        """
        self.__main_window.destroy()


def main():
    Minesweeper()


if __name__ == "__main__":
    main()
