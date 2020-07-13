import csv
import pygame
import time
from mapper import *
from multiprocessing import Process


def collision_detect(win, width, pos, velocity, grid):
    x = pos[0]+(1/2*width)
    y = pos[1]+(1/2*width)
    for row in grid:
        for col in row:
            if pygame.Rect(col[1],col[2], width, width).collidepoint(x,y):
                pass

            # Right Collision
            if pygame.Rect(col[1], col[2], width, width).collidepoint(x+width, y):
                if col[0] != (0,0,0):
                    pass
                elif col[0] == (0,0,0):
                    print('Right collision')

            # Left Collision
            if pygame.Rect(col[1], col[2], width, width).collidepoint(x-width, y):
                if col[0] != (0,0,0):
                    pass
                elif col[0] == (0,0,0):
                    print('Left collision')

            # Up Collision
            if pygame.Rect(col[1], col[2], width, width).collidepoint(x, y-width):
                if col[0] != (0,0,0):
                    pass
                elif col[0] == (0,0,0):
                    return True

            # Down Collision
            if pygame.Rect(col[1], col[2], width, width).collidepoint(x, y+width):
                if col[0] != (0,0,0):
                    pass
                elif col[0] == (0,0,0):
                    print('Down collision')



def main():
    window_width = 800
    window_height = 600
    win = pygame.display.set_mode((window_width,window_height))
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
        start = time.perf_counter()
        collision = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, width).collidepoint(x-width, y):
                        if col[0] != (0, 0, 0):
                            x -= velocity
                            if x < 0:
                                x = 0
                            break
                        elif col[0] == (0, 0, 0):
                            pass

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, width).collidepoint(x + width, y):
                        if col[0] != (0, 0, 0):
                            x += velocity
                            if x > win.get_size()[0] - width:
                                x = win.get_size()[0] - width
                            break
                        elif col[0] == (0, 0, 0):
                            pass

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, width).collidepoint(x, y-width):
                        if col[0] != (0, 0, 0):
                            y -= velocity
                            if y <= 0:
                                y = 0
                            break
                        elif col[0] == (0, 0, 0):
                            pass

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, height).collidepoint((x*1/2)+width, (y*1/2)+height*2):
                        print(col)
                        print(x+(width*1/2))
                        print((y*1/2)+height)
                        if col[0] != (0, 0, 0):
                            y += velocity
                            if y >= win.get_size()[1] - height:
                                y = win.get_size()[1] - height
                            break
                        elif col[0] == (0, 0, 0):
                            pass

        collision_detect(win, width, (x, y), velocity, grid)
        draw_grid(win, x, y, width, height, grid)
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
        pygame.display.update()
        finish = time.perf_counter()
        print(f'Finished in {round(finish - start, 2)} second(s)')
        pygame.time.delay(100)

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    main()
