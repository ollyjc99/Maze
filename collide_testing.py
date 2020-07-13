import pygame
import time


def draw_grid(win, width, height, grid):
    for row in grid:
        for col in row:
            pygame.draw.rect(win, col[0], (col[1], col[2], width, height))
    pygame.display.update()


def main():
    x = 0
    y = 0
    width = 40
    height = 40
    velocity = 40
    win = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Map Builder')
    win.fill((0, 0, 0))
    grid = [[[(255, 255, 255), x, y] for x in range(0, win.get_size()[0], width)] for y in range(0, win.get_size()[1], height)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for row in grid:
                    for col in row:
                        if pygame.Rect(col[1],col[2],width,height).collidepoint(pygame.mouse.get_pos()):
                            print(col)

        draw_grid(win, width, height, grid)
        # pygame.draw.rect(win, (255,255,255),rect)
        pygame.display.update()

        pygame.time.delay(100)


if __name__ == '__main__':
    pygame.init()
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)} second(s)')