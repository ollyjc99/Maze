import csv
import pygame
import time
from mapper import *


def main():
    window_width = 800
    window_height = 600
    win = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('First Game')

    # Text-box
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('You won!', True, (226,190,241))
    text_rect = text.get_rect()
    text_rect.center = (window_width // 2, window_height // 2)

    win.fill((245,205,222))
    width = 40
    height = 40
    velocity = 40
    grid, start, finish = read_grid()
    draw_grid(win, width, height, grid)
    x, y = start
    pygame.draw.rect(win, (204,225,242), (x, y, width, height))
    start_state = start
    final_state = finish
    running = True

    while running:
        time_start = time.perf_counter()
        if (x,y) == final_state:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pos = (round(x-width/2),round(y+height/2))
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, width).collidepoint(pos):
                        if col[0] != (245,205,222):
                            x -= velocity
                            if x < 0:
                                x = 0
                            break
                        elif col[0] == (245,205,222):
                            pass

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pos = (x+width*1.5, y+height/2)
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, width).collidepoint(pos):
                        if col[0] != (245,205,222):
                            x += velocity
                            if x > win.get_size()[0] - width:
                                x = win.get_size()[0] - width
                            break
                        elif col[0] == (245,205,222):
                            pass

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pos = (x+width/2, y-height/2)
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, width).collidepoint(pos):
                        if col[0] != (245,205,222):
                            y -= velocity
                            if y <= 0:
                                y = 0
                            break
                        elif col[0] == (245,205,222):
                            pass

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pos = (x+width/2, y+height*1.5)
            for row in grid:
                for col in row:
                    if pygame.Rect(col[1], col[2], width, height).collidepoint(pos):
                        if col[0] != (245,205,222):
                            y += velocity
                            if y >= win.get_size()[1] - height:
                                y = win.get_size()[1] - height
                            break
                        elif col[0] == (245,205,222):
                            pass

        draw_grid(win, width, height, grid)
        pygame.draw.rect(win, (204,225,242), (x, y, width, height))
        pygame.display.update()
        time_finish = time.perf_counter()
        print(f'Finished in {round(time_finish - time_start, 3)} second(s)')
        pygame.time.delay(100)


if __name__ == "__main__":
    pygame.init()
    main()
