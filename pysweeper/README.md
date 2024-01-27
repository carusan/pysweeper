PySweeper 
Creator: Andrea C.

A small-scale recreation of the classic Microsoft game "Minesweeper" I 
made for a university course using the Tkinter Python library.

The whole game is self-contained in one .py
file; however, the logic could very well be separated from the GUI in a
future revision. There are also a number of non-optimal design choices
in the code, but nothing game-breaking. The aim of the game is to press 
all the safe tiles on the board while avoiding all the mine tiles which 
are randomly placed alongside safe tiles in an "m by n" grid; the 
minefield.

The user wins the game if exactly all the safe tiles are successfully
pressed and exactly all the mine tiles are successfully avoided. The
program makes sure to inform the player if they win or lose in the form
of text and colour changes, the minefield also stops being interactable
at the end of a game round.

To help the user in their quest, every time a safe tile is pressed, the
tile is disabled and displays the number of bomb tiles (not their exact
locations) present in the 8 tiles surrounding the pressed safe tile. If
a player mistakenly presses on a mine tile the game ends.

The options in this program are elementary. In addition to interacting
with the minefield, the user has the option to change the difficulty of
the game from a drop-down menu, reset the current size of minefield and
quit the program. The difficulty changing function also acts as a reset
button of sorts if the same difficulty is chosen; however, it is more
convenient to reset the current game with a click of the reset button.

The three difficulties are the following, which are based on original
Minesweeper difficulty options:

- easy:   "9 by 9" tile minefield with a total mine count of 10.
- medium: "16 by 16" tile minefield with a mine count of 40.
- hard:   "30 by 16" tile minefield with a mine count of 99.

This program was made to be simpler than the original game, as such, the
minefield is pre-rendered and the player runs the risk of pressing a 
mine tile as their first tile, thus ending the game with a score of 0.
The mine tiles are also not opened automatically, the player must
manually click on every safe tile to finish the game.