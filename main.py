import csv
import pygame
from mapper import *
from multiprocessing import Process


def collision_detect(win, width, pos, velocity, grid, key=None):
    x = pos[0]+(1/2*width)
    y = pos[1]+(1/2*width)

    for row in grid:
        for col in row:
            if col[1] <= x <= col[1] + width:
                if col[2] <= y+width <= col[2] + width:
                    print('y')
                    if col[0] != (0,0,0):
                        print('Whitespace')
                        return False
                    if col[0] == (0,0,0):
                        print('Collision')
                        return True

            if col[1] <= x+width <= col[1] + width:
                if col[2] <= y <= col[2] + width:
                    if col[0] != (0,0,0):
                        print('Whitespace')
                        return False
                    elif col[0] == (0,0,0):
                        print('Collision')
                        return True


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
        pos = (y*1/2,x*1/2)
        collision = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            collision_detect(win, width, (x, y), velocity, grid)
            x -= velocity
            if x < 0:
                x = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            collision_detect(win, width, (x, y), velocity, grid)
            x += velocity
            if x > win.get_size()[0] - width:
                x = win.get_size()[0] - width

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            collision_detect(win, width, (x, y), velocity, grid)
            y -= velocity
            if y <= 0:
                y = 0

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += velocity
            if y >= win.get_size()[1] - height:
                y = win.get_size()[1] - height

        collision_detect(win, width, (x, y), velocity, grid)
        draw_grid(win, x, y, width, height, grid)
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
        pygame.display.update()
        pygame.time.delay(100)
    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    main()