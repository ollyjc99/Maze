import pygame
from threading import Thread
import time


def key_down(key, pressed):
    print(key)
    print(pressed)
    while pressed:
        pygame.time.wait(1000)
        print('loop')
        for event in pygame.event.get():
            print(event.type)
            if event.type == 3:
                print("key-up")
                pressed = False
            if event.type == 4:
                print("mouse")
                pressed = False
            if event.type != pygame.KEYUP:
                pass

def main():
    x = 0
    y = 0
    win = pygame.display.set_mode((800,600))
    velocity = 40

    running = True

    while running:
        # print('Running')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == 2:
                key_pressed = event.key
                Thread(target=key_down, args=(key_pressed,True)).start()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print("Left key")
            x -= velocity
            if x < 0:
                x = 0

        if keys[pygame.K_RIGHT]:
            print("Right key")
            x += velocity

        if keys[pygame.K_UP]:
            print("Up key")
            y -= velocity

        if keys[pygame.K_DOWN]:
            print("Down key")
            y += velocity

        if keys[pygame.K_SPACE]:
            running = False

        pygame.time.wait(100)


if __name__ == '__main__':
    pygame.init()
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)} second(s)')
