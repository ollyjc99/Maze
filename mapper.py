import os
import csv
import string
import pygame
from tkinter import *
import threading


class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def quit(self):
        self.root.quit()

    def callback(self, value):
        global e, new_window
        if value <= 4:
            colour_picker(value)
        else:
            new_window = Toplevel(self.root)
            new_window.geometry("150x150+1385+450")
            Label(new_window, text="Enter map name").pack(ipady=5)
            e = Entry(new_window)
            e.pack()
            b = Button(new_window, text="Save", command=self.get_val)
            b.pack(ipady=3)

    def get_val(self):
        save_grid(e.get())

    def run(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.root.geometry("25x215+1400+450")

        rb1 = Button(self.root, text="Border Tile", background="light blue", command=lambda:self.callback(1))
        rb2 = Button(self.root, text="Floor Tile", background="light blue", command=lambda:self.callback(2))
        rb3 = Button(self.root, text="Start Tile", background="light blue", command=lambda: self.callback(3))
        rb4 = Button(self.root, text="End Tile", background="light blue", command=lambda: self.callback(4))
        rb5 = Button(self.root, text="Save", background="green", command=lambda: self.callback(5))
        rb6 = Button(self.root, text="Quit", background="red", foreground='white', command=self.root.destroy)

        rb1.pack(fill=X, ipady=5)
        rb2.pack(fill=X, ipady=5)
        rb3.pack(fill=X, ipady=5)
        rb4.pack(fill=X, ipady=5)
        rb5.pack(fill=X, ipady=5)
        rb6.pack(fill=X, ipady=5)

        self.root.mainloop()


def no_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct


def read_grid():
    new_grid = []
    row = []
    start = (0, 0)
    finish = (800, 600)
    with open('map.csv', 'r') as csvfile:
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
    print('Saved', filename)
    # with open(filename, 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerows(grid)
    # print('Saved map')


def draw_grid(win, width, height, grid):
    for row in grid:
        for col in row:
            pygame.draw.rect(win, col[0], (col[1], col[2], width, height))
    pygame.display.update()
    return


def paint(win, width, height, pos, button, grid, colour):
    selected_square = pos
    for row in grid:
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
    global colour
    colour = (245,205,222)
    width = 40
    height = 40
    velocity = 40

    colours = {'Border Tile': (245,205,222), 'Floor Tile': (251,247,213)}

    win = pygame.display.set_mode((800,600))
    app = App()

    pygame.display.set_caption('Map Builder')
    grid, start, finish = read_grid()
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
                paint(win, width, height, pygame.mouse.get_pos(), event.button, grid, colour)
                pressed = True
                while pressed:
                    for e in pygame.event.get():
                        if e.type != pygame.MOUSEBUTTONUP:
                            paint(win, width, height, pygame.mouse.get_pos(), button, grid, colour)
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
    x = 560
    y = 240
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)
    pygame.init()
    main()
