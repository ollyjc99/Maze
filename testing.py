import csv
import pygame
import time
from mapper import *
from win32api import GetSystemMetrics


class Cube(object):
    def __init__(self, pos, colour=(255,255,255)):
        self.edge = 40
        self.pos = pos
        self.colour = colour

    def draw(self):
        print(self.pos, self.colour)


def main():
    win_width, win_height = 800, 600
    screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)
    win_x = screen_width / 2 - win_width / 2
    win_y = screen_height / 2 - win_height / 2
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (win_x, win_y)
    os.environ['SLD_VIDEO_CENTERED'] = '0'

    edge = 40
    win = pygame.display.set_mode((win_width, win_height))

    boundary = Cube((0,0))
    boundary.draw()

if __name__ == "__main__":
    time_start = time.perf_counter()
    pygame.init()
    main()
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')
