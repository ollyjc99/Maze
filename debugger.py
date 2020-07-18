import pygame
import time
import string
import csv
from mapper import *
import os
'''
Things to debug
1) Searching efficiency
2) Working on maps

'''


def command_handler(command):
    if command == '1':
        maps = []
        for file in os.listdir('maps/'):
            maps.append(file)
        print(maps)
        time.sleep(1000)


def main():
    running = True
    while running:
        os.system('cls')
        print('Debugging Console')
        print('==================')
        print('1) View maps')
        command = input('> ')
        command_handler(command)


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)} second(s)')