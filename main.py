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
        self.image.fill((0,120,255))
        self.rect = self.image.get_rect()
        self.rect.center = 300,250
        self.val = 5

    def update(self, win):
        pass


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

    start = Block(current_map.start, (240, 212, 217))
    final = Block(current_map.final, (1, 255, 31))

    blocks.add(start)
    blocks.add(final)

    player.rect.topleft = current_map.start.topleft

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

        if player.rect.colliderect(final.rect):
            if current_map.name == 'level_4.csv':
                running = False
                print('FIN')
            else:
                current_map = next(maps)
                blocks.empty()
                start.rect.topleft = current_map.start.topleft
                final.rect.topleft = current_map.final.topleft
                blocks.add(start)
                blocks.add(final)
                for rect in current_map.border:
                    blocks.add(Block(rect))
                player.rect.topleft = start.rect.topleft

        # all_sprites.update(win)
        win.fill((245, 205, 222))
        blocks.draw(win)
        all_sprites.draw(win)
        pygame.display.flip()


if __name__ == "__main__":
    time_start = time.perf_counter()
    pygame.init()
    main()
    time_finish = time.perf_counter()
    print(f'Finished in {round(time_finish - time_start, 3)} second(s)')
    pygame.quit()
