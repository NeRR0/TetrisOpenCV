import numpy as np



class TetrisFigure:
    def __init__(self):
        self.counter = 0


    def create_figure(self, img):
        self.counter += 1
        value = 1
        if value == 1:
            square = self._create_square()

        return self._insert_figure(image=img, figure=square)



    def _create_square(self):
        return np.ones((40, 40, 3), dtype=np.uint8) * 255


    def _insert_figure(self, image, figure):
        x_offset = 40
        y_offset = 40 * self.counter
        image[y_offset:y_offset + figure.shape[0], x_offset:x_offset + figure.shape[1]] = figure
        return image


