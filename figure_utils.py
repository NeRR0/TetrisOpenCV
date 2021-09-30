import numpy as np


class TetrisFigure():
    def __init__(self, board):
        self.x_coord = 40 # TODO make it random or center 
        self.y_coord = 40
        self.currently_figure = None
        self.board = board

    def create_figure(self):
        value = 1
        if value == 1:
            square = self._create_square()

        return self._insert_figure(figure=square)


    def _create_square(self):
        self._square_width = 40
        self._square_height = 40
        self.currently_figure = np.ones((self._square_width, self._square_height, 3), dtype=np.uint8) * 255
        return self.currently_figure


    def _insert_figure(self, figure):
        self.x_coord = 40 # TODO make it random or center
        self.y_coord = 40
        self.board[self.y_coord:self.y_coord + figure.shape[0], self.x_coord:self.x_coord + figure.shape[1]] = figure
        return self.board


    def update_figure(self):
        image = self._delete_old_coord(self.board, self.currently_figure)
        self.y_coord = self.y_coord + self._square_width
        image[self.y_coord:self.y_coord + self.currently_figure.shape[0], self.x_coord:self.x_coord + self.currently_figure.shape[1]] = self.currently_figure

    def move_figure(self, direction):
        move_value, down_value = 0, 0
        if direction == "right":
            move_value = 20
        elif direction == "left":
            move_value = - 20
        elif direction == "down":
            down_value = 40

        image = self._delete_old_coord(self.board, self.currently_figure)

        if direction =="left" and self.x_coord > 0 and not self.y_coord == 760:
            self.x_coord = self.x_coord + move_value
        if direction =="right" and self.x_coord < 460 and not self.y_coord == 760:
            self.x_coord = self.x_coord + move_value
        if self.y_coord < 760:
            self.y_coord = self.y_coord + down_value

        # block_flag = _floor_block()
        image[self.y_coord:self.y_coord + self.currently_figure.shape[0], self.x_coord:self.x_coord + self.currently_figure.shape[1]] = self.currently_figure




    def _delete_old_coord(self, image, black_figure):
        white_figure = black_figure * 0
        image[self.y_coord:self.y_coord + white_figure.shape[0], self.x_coord:self.x_coord + white_figure.shape[1]] = white_figure
        return image


    def _floor_block(self):
        print(self.y_coord + 40, self.board.shape[0])
        if self.y_coord + 40 == self.board.shape[0]:
            print("STUCK")
            return True
        elif (self.board[self.y_coord + 40][self.x_coord] == np.asarray([255, 255, 255])).any():
            return True
        elif (self.board[self.y_coord + 40][self.x_coord+20] == np.asarray([255, 255, 255])).any():
            return True
        else:
            return False

    def _block(self):
        pass