import numpy as np


class Board:
    def __init__(self, width, heigth):
        self._width = width
        self._heigth = heigth
        self._background = None
        self._game_counter = 0

    def create(self):
        self._background = np.zeros((self._width, self._heigth, 3), dtype=np.uint8)
        return self._background

    # def update_board(self, old_board):
    #     new_board =
    #     return new_board

    # def counter(self):
    #     self._game_counter +=1
    #     if self._game_counter == 250:
    #         return True
    #     else:
    #         return False