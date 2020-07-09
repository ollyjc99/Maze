import pygame

def draw_grid(win):
    height = 40
    width = 40
    grid = [[[1, x, y] for x in range(0, 800, 40)] for y in range(0, 600, 40)]
    red = 0
    green = 0
    blue = 0
    a = 3
    b = 2
    c = 1
    for row in grid:
        for col in row:
            pygame.time.delay(1)
            pygame.draw.rect(win, (red,green,blue), (col[1], col[2], width, height))

            red += a
            if red > 255:
                a = -3
                red += a
            elif red < 0:
                a = 3
                red+=a

            green += b
            if green > 255:
                b = -2
                green += b
            elif green < 0:
                b = 2
                green+=b

            blue += c
            if blue > 255:
                c = -1
                blue += c
            elif blue < 0:
                c = 1
                blue+=c
            pygame.display.update()




def main():
    win = pygame.display.set_mode((800,600))
    pygame.display.set_caption('First Game')

    x = 360
    y = 260
    width = 40
    height = 40
    velocity = 20

    running = True

    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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

        win.fill((0,0,0))
        draw_grid(win)


if __name__ == "__main__":
    pygame.init()
    main()