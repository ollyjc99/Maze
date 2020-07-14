import csv
import string
import pygame


class Map(object):
    def __init__(self, grid):
        self.saved_map = self.read_map(grid)

    def read_map(self, grid):
        new_grid = []
        row = []
        with open('map.csv', 'r') as csvfile:
            r = csv.reader(csvfile)
            for i in range(0, 15):
                if row:
                    new_grid.append(row)
                    row = []
                field = next(r)
                for i in field:
                    values = no_punct(i).split()
                    new_row = [(int(values[0]), int(values[1]), int(values[2])), int(values[3]), int(values[4])]
                    row.append(new_row)

        new_grid.append(row)
        return new_grid


def no_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct


def read_grid():
    new_grid = []
    row = []
    start = (0,0)
    finish = (800,600)
    with open('map.csv', 'r') as csvfile:
        r = csv.reader(csvfile)
        for i in range(0, 15):
            if row:
                new_grid.append(row)
                row = []
            field = next(r)
            for j in field:
                values = no_punct(j).split()
                new_row = [(int(values[0]),int(values[1]),int(values[2])), int(values[3]), int(values[4])]

                if (int(values[0]),int(values[1]),int(values[2])) == (235,225,200):
                    start = (int(values[3]), int(values[4]))

                if (int(values[0]),int(values[1]),int(values[2])) == (200,255,200):
                    finish = (int(values[3]), int(values[4]))
                row.append(new_row)
    new_grid.append(row)
    return new_grid, start, finish


def draw_grid(win, width, height, grid):
    for row in grid:
        for col in row:
            pygame.draw.rect(win, col[0], (col[1], col[2], width, height))
    pygame.display.update()
    return


def paint(win, width, height, pos, button, grid):
    selected_square = pos
    for row in grid:
        for col in row:
            if pygame.Rect(col[1], col[2], width, height).collidepoint(pygame.mouse.get_pos()):
                if button == 1:
                    col[0] = (245,205,222)
                if button == 3:
                    col[0] = (251,247,213)
                if button == '32':
                    col[0] = (235,225,200)
                if button == 'f':
                    col[0] = (200,255,200)
                pygame.draw.rect(win, col[0], (col[1], col[2], width, height))
                pygame.display.update()


def main():
    width = 40
    height = 40
    velocity = 40
    win = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Map Builder')
    grid, start = read_grid()
    win.fill((0, 0, 0))
    draw_grid(win, width, height, grid)
    selected = (0,0)
    running = True
    drawing = False

    x, y = start
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
                    paint(win, width, height, pygame.mouse.get_pos(), '32', grid)
                if event.key == pygame.K_f:
                    paint(win, width, height, pygame.mouse.get_pos(), 'f', grid)

                if event.key == pygame.K_s:
                    filename = 'map.csv'
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(grid)
                    print('Saved map')

                if event.key == pygame.K_r:
                    grid = [[[(251,247,213), x, y] for x in range(0, win.get_size()[0], width)] for y in
                            range(0, win.get_size()[1], height)]
                    print('Reset map')

        draw_grid(win, width, height, grid)
        pygame.display.update()

        pygame.time.delay(100)


if __name__ == "__main__":
    pygame.init()
    main()
