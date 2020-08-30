import os
import csv
import pygame
import time
from mapper import *
from itertools import cycle
from assets import *


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
