import os
import csv
import pygame
import time
from mapper import *
from itertools import cycle


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
<<<<<<< HEAD
        self.image = pygame.Surface((40, 40))
        self.image.fill((244, 32, 105))
        self.rect = self.image.get_rect()
        self.rect.center = 250,250
        self.xval = 5
        self.yval = 5
=======
        self.image = pygame.Surface((30, 30))
        self.image.fill((0,120,255))
        self.rect = self.image.get_rect()
        self.rect.center = 300,250
        self.val = 5
>>>>>>> experimental

    def update(self, win):
        pass


class Block(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill((189, 0, 255))
        self.rect = rect


class Map(object):
    def __init__(self, grid, start, final):
        self.grid = grid
        self.start = start
        self.final = final
        self.border = self.get_border()

    def get_border(self):
<<<<<<< HEAD
        border_points = [pygame.Rect(col[1], col[2], 40, 40) for row in self.grid for col in row if col[0] == (245, 205, 222)]

        return border_points


class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill((245,205,222))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, win):
        print(self.rect)

=======
        return [pygame.Rect(col[1], col[2], 40, 40) for row in self.grid for col in row if col[0] == (245, 205, 222)]
>>>>>>> experimental


def main():
    win = pygame.display.set_mode((800, 600))
    w, h = win.get_size()
    pygame.display.set_caption('First Game')

    clock = pygame.time.Clock()
    map_list = load_maps()
    maps = iter([Map(*read_grid(level)) for level in map_list])
    current_map = next(maps)

    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    blocks = pygame.sprite.Group()
    for rect in current_map.border:
        blocks.add(Block(rect))

<<<<<<< HEAD
    blocks = [Block((col[1], col[2])) for row in grid for col in row if col[0] == (245, 205, 222)]
    level_border = pygame.sprite.Group()
    for block in blocks:
        level_border.add(block)
    x, y = start
=======
    x, y = current_map.start
>>>>>>> experimental

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key = None
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if not player.rect.left <= 0:
                player.rect.x -= player.val

            if not player.rect.collidelist(current_map.border) == -1:
                player.rect.x += player.val


        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if not player.rect.right >= w:
                player.rect.x += player.val

            if not player.rect.collidelist(current_map.border) == -1:
                player.rect.x -= player.val

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if not player.rect.top <= 0:
                player.rect.y -= player.val

            if not player.rect.collidelist(current_map.border) == -1:
                player.rect.y += player.val

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if not player.rect.bottom >= h:
                player.rect.y += player.val

            if not player.rect.collidelist(current_map.border) == -1:
                player.rect.y -= player.val

        if (player.rect.x, player.rect.y) == current_map.final:
            if current_map == 'level_4.csv':
                running = False
                print('FIN')
            else:
                current_map = next(maps)
<<<<<<< HEAD
                grid, start, finish = read_grid(current_map)
                start_state = start
                final_state = finish
                x, y = start

        # pygame.time.delay(50)
        if player.rect.collidelist(level_1.border) == -1:
            pass

        level_border.update(win)
        all_sprites.update(win)
        win.fill((180,212,85))
        level_border.draw(win)
=======
                start_state = current_map.start
                final_state = current_map.final
                x, y = current_map.start
        print(player.rect)
        if not player.rect.collidelist(current_map.border) == -1:
            print('yeet')

        # all_sprites.update(win)
        win.fill((245, 205, 222))
        blocks.draw(win)
>>>>>>> experimental
        all_sprites.draw(win)
        pygame.display.flip()


if __name__ == "__main__":
    time_start = time.perf_counter()
    pygame.init()
    main()
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')
    pygame.quit()
