import csv
import pygame
import time
from mapper import *
from itertools import cycle


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill((244, 32, 105))
        self.rect = self.image.get_rect()
        self.rect.center = 250,250
        self.xval = 5
        self.yval = 5

    def update(self, win):
        w, h = win.get_size()
        self.rect.x += self.xval
        self.rect.y += self.yval

        if self.rect.right > w:
            self.xval = -self.xval

        if self.rect.left < 0:
            self.xval = -self.xval

        if self.rect.top < 0:
            self.yval = -self.yval

        if self.rect.bottom > h:
            self.yval = -self.yval


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

    clock = pygame.time.Clock()
    maps = iter(load_maps())
    current_map = next(maps)
    grid, start, finish = read_grid(current_map)
    start_state = start
    final_state = finish

    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    level_1 = Map(grid, start, finish)
    print(level_1.border)
    # draw_grid(win, width, height, grid)

    x, y = start

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pass

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pass

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pass

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
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

        # pygame.time.delay(50)
        if player.rect.collidelist(level_1.border) == -1:
            pass

        all_sprites.update(win)
        win.fill((180,212,85))
        all_sprites.draw(win)
        pygame.display.flip()


if __name__ == "__main__":
    time_start = time.perf_counter()
    pygame.init()
    main()
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')
    pygame.quit()
