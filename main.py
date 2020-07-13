import csv
import pygame
from mapper import *
from multiprocessing import Process


def collision_detect(win, width, pos, velocity, grid):
    print(pos)


def main():
    win = pygame.display.set_mode((800,600))
    pygame.display.set_caption('First Game')
    win.fill((0, 0, 0))
    x = 0
    y = 0
    width = 40
    height = 40
    velocity = 40
    grid = read_grid()
    draw_grid(win, x, y, width, height, grid)
    running = True
    drawing = False

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            x -= velocity
            if x < 0:
                x = 0

        if keys[pygame.K_d]:
            x += velocity
            if x > win.get_size()[0] - width:
                x = win.get_size()[0] - width

        if keys[pygame.K_SPACE]:
            y -= velocity
            if y <= 0:
                y = 0

        if keys[pygame.K_DOWN]:
            y += velocity
            if y >= win.get_size()[1] - height:
                y = win.get_size()[1] - height

        draw_grid(win, x, y, width, height, grid)
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
        pygame.display.update()
        collision_detect(win, width, (x, y), velocity, grid)
        pygame.time.delay(100)
    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    main()