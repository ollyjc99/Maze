import os
import csv
import pygame
import time
from mapper import *
from itertools import cycle


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 120, 255))
        self.rect = self.image.get_rect()
        self.rect.center = 300,250
        self.val = 5

    def update(self, win, border):
        w, h = win.get_size()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if not self.rect.left <= 0:
                self.rect.x -= self.val

            if not self.rect.collidelist(border) == -1:
                self.rect.x += self.val

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if not self.rect.right >= w:
                self.rect.x += self.val

            if not self.rect.collidelist(border) == -1:
                self.rect.x -= self.val

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if not self.rect.top <= 0:
                self.rect.y -= self.val

            if not self.rect.collidelist(border) == -1:
                self.rect.y += self.val

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if not self.rect.bottom >= h:
                self.rect.y += self.val

            if not self.rect.collidelist(border) == -1:
                self.rect.y -= self.val


class Block(pygame.sprite.Sprite):
    def __init__(self, rect, colour=(189, 0, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(colour)
        self.rect = rect


class Map(object):
    def __init__(self, name, grid, start, final):
        self.name = name
        self.grid = grid
        self.start = self.get_start(start)
        self.final = self.get_accept(final)
        self.border = self.get_border()

    def get_border(self):
        return [pygame.Rect(col[1], col[2], 40, 40) for row in self.grid for col in row if col[0] == (245, 205, 222)]

    def get_start(self, start):
        return pygame.Rect(*start, 40, 40)

    def get_accept(self, final):
        return pygame.Rect(*final, 40, 40)


def main():
    win = pygame.display.set_mode((800, 600))
    w, h = win.get_size()
    pygame.display.set_caption('First Game')

    clock = pygame.time.Clock()

    map_list = load_maps()
    maps = iter([Map(*read_grid(level)) for level in map_list])
    current_map = next(maps)

    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    blocks = pygame.sprite.Group()
    for rect in current_map.border:
        blocks.add(Block(rect))

    final = Block(current_map.final, (1, 255, 31))

    blocks.add(final)

    player.rect.topleft = current_map.start.topleft

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if player.rect.colliderect(final.rect):
            if current_map.name == 'level_4.csv':
                running = False
                print('FIN')
            else:
                current_map = next(maps)
                blocks.empty()
                final.rect.topleft = current_map.final.topleft
                blocks.add(final)
                for rect in current_map.border:
                    blocks.add(Block(rect))
                player.rect.topleft = current_map.start.topleft

        win.fill((253, 253, 150))
        blocks.draw(win)
        all_sprites.update(win, current_map.border)
        all_sprites.draw(win)
        pygame.display.flip()


if __name__ == "__main__":
    time_start = time.perf_counter()
    pygame.init()
    main()
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')
    pygame.quit()
