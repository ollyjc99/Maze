import csv
import pygame
from mapper import *
from multiprocessing import Process

def main():
    global grid
    filename = 'map.csv'
    win = pygame.display.set_mode((800,600))
    pygame.display.set_caption('First Game')
    win.fill((0, 0, 0))
    x = 0
    y = 0
    width = 40
    height = 40
    velocity = 40
    grid = [[[(255,255,255), x, y] for x in range(0, win.get_size()[0], width)] for y in range(0, win.get_size()[1], height)]
    draw_grid(win, x, y, width, height, grid)
    selected = (0,0)
    running = True
    drawing = False

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.KEYDOWN:
            #     print(event.key)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            print("Left key")
            x -= velocity
            if x < 0:
                x = 0

        if keys[pygame.K_RIGHT]:
            print("Right key")
            x += velocity
            if x > win.get_size()[0] - width:
                x = win.get_size()[0] - width

        if keys[pygame.K_UP]:
            print("Up key")
            y -= velocity
            if y <= 0:
                y = 0

        if keys[pygame.K_DOWN]:
            print("Down key")
            y += velocity
            if y >= win.get_size()[1] - height:
                y = win.get_size()[1] - height

        draw_grid(win, x, y, width, height, grid)
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
        pygame.display.update()
        pygame.time.delay(100)
    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    main()