import os
import csv
import string
import pygame


def load_maps():
    maps = []
    for file in os.listdir('maps/'):
        maps.append(file)
    return maps


def no_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct


def read_grid(filename='level_1.csv'):
    new_grid = []
    row = []
    start = (0, 0)
    finish = (800, 600)
    with open('maps/'+filename, 'r') as csvfile:
        r = csv.reader(csvfile)
        for i in range(0, 15):
            if row:
                new_grid.append(row)
                row = []
            field = next(r)
            for j in field:
                values = no_punct(j).split()
                new_row = [(int(values[0]), int(values[1]), int(values[2])), int(values[3]), int(values[4])]
                if (int(values[0]), int(values[1]), int(values[2])) == (235, 225, 200):
                    start = (int(values[3]), int(values[4]))
                if (int(values[0]), int(values[1]), int(values[2])) == (200, 255, 200):
                    finish = (int(values[3]), int(values[4]))
                row.append(new_row)
    new_grid.append(row)
    return new_grid, start, finish


def save_grid(value):
    filename = value + '.csv'
    current_maps = load_maps()
    if filename not in current_maps:
        current_maps.append(filename)

        with open('maps/'+filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(grid)
        print('Saved map')

    print(current_maps)


def draw_grid(win, width, height, map):
    for row in map:
        for col in row:
            pygame.draw.rect(win, col[0], (col[1], col[2], width, height))
    pygame.display.update()
    return


def paint(win, width, height, pos, button, map, colour):
    selected_square = pos
    for row in map:
        for col in row:
            if pygame.Rect(col[1], col[2], width, height).collidepoint(pygame.mouse.get_pos()):
                if button == 1:
                    col[0] = colour
                if button == 3:
                    col[0] = (251,247,213)
                if button == '32':
                    col[0] = (235,225,200)
                if button == 'f':
                    col[0] = (200,255,200)
                pygame.draw.rect(win, col[0], (col[1], col[2], width, height))
                pygame.display.update()


def colour_picker(value):
    global colour
    colours = {'Border Tile': (245, 205, 222), 'Floor Tile': (251, 247, 213)}

    if value == 1:
        colour = (245, 205, 222)
    if value == 2:
        colour = (251, 247, 213)
    if value == 3:
        colour = (235,225,200)
    if value == 4:
        colour = (200,255,200)


def main():
    global colour, grid, start, finish, selected_map, file_saved
    maps = load_maps()
    colour = (245,205,222)
    width = 40
    height = 40
    velocity = 40

    colours = {'Border Tile': (245,205,222), 'Floor Tile': (251,247,213)}

    win = pygame.display.set_mode((800,600))

    pygame.display.set_caption('Map Builder')
    selected_map = 'level_1.csv'
    grid, start, finish = read_grid(selected_map)
    win.fill((0, 0, 0))
    draw_grid(win, width, height, grid)
    selected = (0,0)

    running = True
    drawing = False
    load_file = False

    x, y = start
    while running:
        if load_file:
            grid = read_grid()[0]
            load_file = False
        print(selected_map)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                paint(win, width, height, pygame.mouse.get_pos(), event.button, grid, colour)
                pressed = True
                while pressed:
                    for e in pygame.event.get():
                        if e.type != pygame.MOUSEBUTTONUP:
                            paint(win, width, height, pygame.mouse.get_pos(), button, grid, colour)
                        if e.type == pygame.MOUSEBUTTONUP:
                            pressed = False

        draw_grid(win, width, height, grid)
        pygame.display.update()

        pygame.time.delay(100)


if __name__ == "__main__":
    # os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)
    pygame.init()
    main()
