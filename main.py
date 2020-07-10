import pygame


def draw_grid(win):
    height = 40
    width = 40

    for row in grid:
        for col in row:
            pygame.draw.rect(win, col[0], (col[1], col[2], width, height))

    pygame.display.update()


def paint(win, width, height, pos):
    for row in grid:
        for col in row:
            if pos[0] >= col[1] and pos[0] <= col[1]+40:
                if pos[1] >= col[2] and pos[1] <= col[2] + 40:
                    col[0] = (0,0,0)
                    pygame.draw.rect(win, col[0], (col[1], col[2], width, height))
                    pygame.display.update()


def main():
    win = pygame.display.set_mode((800,600))
    pygame.display.set_caption('First Game')
    win.fill((0, 0, 0))
    x = 0
    y = 0
    width = 40
    height = 40
    velocity = 40
    draw_grid(win)
    running = True
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    while running:

        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                paint(win,width,height,pygame.mouse.get_pos())



        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= velocity
            if x < 0:
                x = 0
        if keys[pygame.K_RIGHT]:
            x += velocity
            if x > win.get_size()[0] - width:
                x = win.get_size()[0] - width
        if keys[pygame.K_UP]:
            y -= velocity
            if y <= 0:
                y = 0
        if keys[pygame.K_DOWN]:
            y += velocity
            if y >= win.get_size()[1] - height:
                y = win.get_size()[1] - height
        if keys[pygame.K_SPACE]:
            print(grid)
        draw_grid(win)
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    grid = [[[(255,255,255), x, y] for x in range(0, 800, 40)] for y in range(0, 600, 40)]
    main()