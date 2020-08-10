import csv
import pygame
import time
from mapper import *
from itertools import cycle


class Sprite(object):
    def __init__(self, win, width, height, colour):
        self.win = win
        self.x = 50
        self.y = 50
        self.width = width
        self.height = height
        self.colour = colour
        self.velocity = 40
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))

    def move(self, dirn, val):
        if dirn == 'left' or dirn == 'right':
            self.x += val
        if dirn == 'up' or dirn == 'down':
            self.y += val

        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))
        self.draw()

    def draw(self):
        pygame.draw.rect(self.win, self.colour, self.rect)


class Map(object):
    def __init__(self, grid, start, finish):
        self.grid = grid
        self.start = start
        self.finish = finish
        self.border = self.get_border()

    def get_border(self):
        border_points = [pygame.Rect(col[1], col[2], 40, 40) for row in self.grid for col in row if col[0] == (245, 205, 222)]

        return border_points


class Block(object):
    def __init__(self, win, width, height, prop):
        self.win = win
        self.width = width
        self.height = height
        self.prop = prop

    def get_texture(self):
        return None

    def draw(self, pos):
        pygame.draw.rect(self.win, (self.x, self.y, self.width, self.height))


def main():
    width = 40
    height = 40
    velocity = 5
    window_width = 800
    window_height = 600
    win = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('First Game')
    win.fill((245,205,222))
    clock = pygame.time.Clock()
    maps = iter(load_maps())
    current_map = next(maps)
    grid, start, finish = read_grid(current_map)
    start_state = start
    final_state = finish

    player = Sprite(win, 30, 30, (0,120,255))
    level_1 = Map(grid, start, finish)
    print(level_1.border)
    draw_grid(win, width, height, grid)
    x, y = start

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # draw_grid(win, width, height, grid)
        # player.draw()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if player.rect.collidelist(level_1.border) == -1:
                draw_grid(win, width, height, grid)
                player.move('left', -velocity)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            draw_grid(win, width, height, grid)
            player.move('right', velocity)

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            draw_grid(win, width, height, grid)
            player.move('up', -velocity)

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            draw_grid(win, width, height, grid)
            player.move('down', velocity)

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

        # pygame.time.delay(50)
        pygame.display.update()



if __name__ == "__main__":
    time_start = time.perf_counter()
    pygame.init()
    main()
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')
    pygame.quit()
