import cv2
import numpy as np
from figure_utils import TetrisFigure



def add_text(img, color):
    return cv2.putText(img, 'FPS: {}'.format(game_loop_counter), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2,
                cv2.LINE_AA)



background = np.zeros((800, 500, 3), dtype=np.uint8)
# square = np.ones((25, 25, 3), dtype=np.uint8)* 255

game_loop_counter = 0





# x_offset=y_offset=50
# background[y_offset:y_offset + square.shape[0], x_offset:x_offset + square.shape[1]] = square


tetris_figure = TetrisFigure()
while True:
    add_text(img=background, color=(255, 0 ,0))



    background = tetris_figure.create_figure(background)
    print(id(background))


    cv2.imshow("TETRIS", background)
    cv2.waitKey(1000)
    add_text(img=background, color=(0, 0, 0))
    game_loop_counter += 1