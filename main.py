import cv2
import numpy as np
from figure_utils import TetrisFigure
from board import Board
import threading
import time
import queue


que = queue.Queue()

def update_figure():
    while True:
        time.sleep(1)
        que.put(True)


def add_text(img, color, game_loop_counter):
    return cv2.putText(img, 'FPS: {}'.format(game_loop_counter), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2,
                cv2.LINE_AA)


def main():
    t1 = threading.Thread(target=update_figure)
    t1.start()

    board = Board(800, 500)
    background = board.create()
    game_loop_counter = 0

    tetris_figure = TetrisFigure()
    _ = tetris_figure.create_figure(background)
    while True:
        add_text(img=background, color=(255, 0 ,0), game_loop_counter=game_loop_counter)

        if not que.empty():
            flag = que.get(block=False)
            if flag:
                tetris_figure.update_figure(background)


        cv2.imshow("TETRIS", background)
        cv2.waitKey(1)
        add_text(img=background, color=(0, 0, 0), game_loop_counter=game_loop_counter)
        game_loop_counter += 1

if __name__ == '__main__':

    main()