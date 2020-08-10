import csv
import pygame
import time
from mapper import *
from itertools import cycle


class Sprite(object):
    def __init__(self, win, width, height):
        self.win = win
        self.x = 0
        self.y = 0
        self.width = 40
        self.height = 40
        self.velocity = 40

    def move(self, key):
        print(key)


class Block(object):
    def __init__(self, win, width, height, property):
        self.win = win
        self.width = width
        self.height = height
        self.property = property


def main():
    width = 40
    height = 40
    velocity = 40
    window_width = 800
    window_height = 600
    win = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('First Game')
    win.fill((245,205,222))
    clock = pygame.time.Clock()
    maps = iter(load_maps())
    current_map = next(maps)
    grid, start, finish = read_grid(current_map)
    draw_grid(win, width, height, grid)
    start_state = start
    final_state = finish

    x, y = start
    pygame.draw.rect(win, (204,225,242), (x, y, width, height))

    running = True
    while running:
        # clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pos = (int(x-width/2),int(y+height/2))
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, width).collidepoint(pos):
                        if col[0] != (245,205,222):
                            x -= velocity
                            if x < 0:
                                x = 0
                            break
                        elif col[0] == (245,205,222):
                            pass

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pos = (int(x+width*1.5), int(y+height/2))
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, width).collidepoint(pos):
                        if col[0] != (245,205,222):
                            x += velocity
                            if x > win.get_size()[0] - width:
                                x = win.get_size()[0] - width
                            break
                        elif col[0] == (245,205,222):
                            pass

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pos = (int(x+width/2), int(y-height/2))
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, width).collidepoint(pos):
                        if col[0] != (245,205,222):
                            y -= velocity
                            if y <= 0:
                                y = 0
                            break
                        elif col[0] == (245,205,222):
                            pass

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pos = (int(x+width/2), int(y+height*1.5))
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, height).collidepoint(pos):
                        if col[0] != (245,205,222):
                            y += velocity
                            if y >= win.get_size()[1] - height:
                                y = win.get_size()[1] - height
                            break
                        elif col[0] == (245,205,222):
                            pass

        if (x,y) == final_state:
            if current_map == 'level_4.csv':
                running = False
                print('FIN')
            else:
                current_map = next(maps)
                grid, start, finish = read_grid(current_map)
                start_state = start
                final_state = finish
                x, y = start

        draw_grid(win, width, height, grid)
        pygame.draw.rect(win, (204,225,242), (x, y, width, height))
        pygame.display.update()

        pygame.time.delay(100)


if __name__ == "__main__":
    time_start = time.perf_counter()
    pygame.init()
    main()
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')
