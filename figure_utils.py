import numpy as np



class TetrisFigure:
    def __init__(self):
        self.counter = 0
        self.x_coord = 40 # TODO make it random or center 
        self.y_coord = 40

    def create_figure(self, img):
        self.counter += 1
        value = 1
        if value == 1:
            square = self._create_square()

        return self._insert_figure(image=img, figure=square)



    def _create_square(self):
        return np.ones((40, 40, 3), dtype=np.uint8) * 255


    def _insert_figure(self, image, figure):
        image = self._delete_old_coord(image, figure)
        self.x_coord = 40 # TODO make it random or center
        self.y_coord = 40 * self.counter
        image[self.y_coord:self.y_coord + figure.shape[0], self.x_coord:self.x_coord + figure.shape[1]] = figure
        return image

    def _delete_old_coord(self, image, black_figure):
        white_figure = black_figure * 0
        image[self.y_coord:self.y_coord + white_figure.shape[0], self.x_coord:self.x_coord + white_figure.shape[1]] = white_figure
        return image

