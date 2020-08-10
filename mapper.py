import os
import csv
import string
import pygame


def load_maps():
    maps = []
    for file in os.listdir('maps/'):
        maps.append(file)
    return maps


def change_map(maps, selected_map):
    found = False
    for map in maps:
        if map == selected_map:
            found = True

    if found:
        return selected_map, True
    else:
        return selected_map, False


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


def save_grid(value, grid):
    filename = value + '.csv'
    current_maps = load_maps()
    if filename not in current_maps:
        current_maps.append(filename)

    with open('maps/'+filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(grid)
    print('Saved map')
    return current_maps


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
                if button == 6:
                    col[0] = (235,225,200)
                if button == 7:
                    col[0] = (200,255,200)
                pygame.draw.rect(win, col[0], (col[1], col[2], width, height))
                pygame.display.update()


def main():
    # global grid, start, finish
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
    load_map = False

    x, y = start
    while running:
        if load_map:
            grid = read_grid(selected_map)[0]
            load_map = False
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_map, load_map = change_map(maps, 'level_1.csv')
                if event.key == pygame.K_2:
                    selected_map, load_map = change_map(maps, 'level_2.csv')
                if event.key == pygame.K_3:
                    selected_map, load_map = change_map(maps, 'level_3.csv')
                if event.key == pygame.K_4:
                    selected_map, load_map = change_map(maps, 'level_4.csv')

                if event.key == pygame.K_s:
                    maps = save_grid(input('Enter filename: '), grid)

                if event.key == pygame.K_r:
                    grid = [[[(251,247,213), x, y] for x in range(0, 800, 40)] for y in range(0, 600, 40)]

        draw_grid(win, width, height, grid)
        pygame.display.update()

        pygame.time.delay(100)


if __name__ == "__main__":
    # os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)
    pygame.init()
    main()
