import pygame


def draw_grid(win, x, y, width, height, grid):

    for row in grid:
        for col in row:
            pygame.draw.rect(win, col[0], (col[1], col[2], width, height))

    pygame.display.update()


def paint(win, width, height, pos, button):
    selected_square = pos
    for row in grid:
        for col in row:
            if col[1] <= pos[0] <= col[1] + width:
                if col[2] <= pos[1] <= col[2] + height:
                    if button == 1:
                        col[0] = (0,0,0)
                    if button == 3:
                        col[0] = (255,255,255)
                    pygame.draw.rect(win, col[0], (col[1], col[2], width, height))
                    pygame.display.update()


def main():
    global grid
    win = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Map Builder')
    win.fill((0, 0, 0))
    x = 0
    y = 0
    width = 40
    height = 40
    velocity = 40
    grid = [[[(255,255,255), x, y] for x in range(0, win.get_size()[0], width)] for y in range(0, win.get_size()[1], height)]
    draw_grid(win, x, y, width, height)
    selected = (0,0)
    running = True
    drawing = False

    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEMOTION:
            #     hover(win, width, height, pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                paint(win, width, height, pygame.mouse.get_pos(), event.button)
                pressed = True
                while pressed:
                    for e in pygame.event.get():
                        if e.type != pygame.MOUSEBUTTONUP:
                            paint(win, width, height, pygame.mouse.get_pos(), button)
                        elif e.type == pygame.MOUSEBUTTONUP:
                            pressed = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print(grid)

        draw_grid(win, x, y, width, height)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()