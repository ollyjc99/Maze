import pygame
import time
import string
import csv
import os
from mapper import *
class text:
    def __init__(self, font, text, textRect):
        self.font = font
        self.text = text
        self.textRect = textRect

def main():
    x = 800
    y = 600

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    win = pygame.display.set_mode((x, y))

    pygame.display.set_caption('Show Text')
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('GeeksForGeeks', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (x // 2, y // 3)

    while True:

        win.fill(white)

        win.blit(text, textRect)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                quit()

            pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
