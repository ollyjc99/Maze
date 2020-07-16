import pygame
import time
import string
import csv
import os
from tkinter import *
from mapper import *
import threading


class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def quit(self):
        self.root.quit()

    def callback(self,v):
        print(v)

    def run(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.quit)

        rb1 = Button(self.root, text="Border Tile", background="light blue", command=lambda:self.callback(1)).pack(fill=X, ipady=5)
        rb2 = Button(self.root, text="Floor Tile", background="light blue", command=lambda:self.callback(1)).pack(fill=X, ipady=5)
        rb3 = Button(self.root, text="Start Tile", background="light blue", command=lambda: self.callback(1)).pack(fill=X, ipady=5)
        rb4 = Button(self.root, text="End Tile", background="light blue", command=lambda: self.callback(1)).pack(fill=X, ipady=5)
        rb5 = Button(self.root, text="Quit", background="red", foreground='white', command=self.root.destroy).pack(fill=X, ipady=5)

        self.root.mainloop()


def main():
    colour_picker = (245,205,222)
    app = App()


if __name__ == '__main__':
    main()
