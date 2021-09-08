import numpy as np

import board


class TetrisFigure:
    def __init__(self):
        # self.counter = 1
        self.x_coord = 40 # TODO make it random or center 
        self.y_coord = 40
        self.currently_figure = None

    def create_figure(self, img):
        value = 1
        if value == 1:
            square = self._create_square()

        return self._insert_figure(image=img, figure=square)


    def _create_square(self):
        self._square_width = 40
        self._square_height = 40
        self.currently_figure = np.ones((self._square_width, self._square_height, 3), dtype=np.uint8) * 255
        return self.currently_figure


    def _insert_figure(self, image, figure):
        self.x_coord = 40 # TODO make it random or center
        self.y_coord = 40
        image[self.y_coord:self.y_coord + figure.shape[0], self.x_coord:self.x_coord + figure.shape[1]] = figure
        return image


    def update_figure(self, image):
        image = self._delete_old_coord(image, self.currently_figure)
        self.y_coord = self.y_coord + self._square_width
        image[self.y_coord:self.y_coord + self.currently_figure.shape[0], self.x_coord:self.x_coord + self.currently_figure.shape[1]] = self.currently_figure



    def _delete_old_coord(self, image, black_figure):
        white_figure = black_figure * 0
        image[self.y_coord:self.y_coord + white_figure.shape[0], self.x_coord:self.x_coord + white_figure.shape[1]] = white_figure
        return image


    def _floor_block(self, board):
        print(self.y_coord + 40, board.shape[0])
        if self.y_coord + 40 == board.shape[0]:
            print("STUCK")
            return True
        elif (board[self.y_coord + 40][self.x_coord] == np.asarray([255, 255, 255])).any():
            return True
        else:
            return False
