import csv
import string
import pygame


def no_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct


def read_grid():
    new_grid = []
    row = []
    with open('map.csv', 'r') as csvfile:
        r = csv.reader(csvfile)
        for i in range(0, 15):
            if row != []:
                new_grid.append(row)
                row = []
            field = next(r)
            for i in field:
                values = no_punct(i).split()
                new_row = [(int(values[0]),int(values[1]),int(values[2])), int(values[3]), int(values[4])]
                row.append(new_row)

    new_grid.append(row)
    return new_grid


def draw_grid(win, x, y, width, height, grid):
    for row in grid:
        for col in row:
            pygame.draw.rect(win, col[0], (col[1], col[2], width, height))
    pygame.display.update()


def paint(win, width, height, pos, button, grid):
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
    x = 0
    y = 0
    width = 40
    height = 40
    velocity = 40
    win = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Map Builder')
    grid = read_grid()
    win.fill((0, 0, 0))
    draw_grid(win, x, y, width, height, grid)
    selected = (0,0)
    running = True
    drawing = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                paint(win, width, height, pygame.mouse.get_pos(), event.button, grid)
                pressed = True
                while pressed:
                    for e in pygame.event.get():
                        if e.type != pygame.MOUSEBUTTONUP:
                            paint(win, width, height, pygame.mouse.get_pos(), button, grid)
                        if e.type == pygame.MOUSEBUTTONUP:
                            pressed = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    filename = 'map.csv'
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(grid)
                    print('Saved map')

                if event.key == pygame.K_r:
                    grid = [[[(255,255,255), x, y] for x in range(0, win.get_size()[0], width)] for y in
                            range(0, win.get_size()[1], height)]
                    # for i in range(0, win.get_size[0], width):
                    #     for x in range(0, win.get_size[1], width):
                    #         print(i, x)
                    print('Reset map')

        draw_grid(win, x, y, width, height, grid)
        pygame.display.update()

        pygame.time.delay(100)


if __name__ == "__main__":
    pygame.init()
    main()