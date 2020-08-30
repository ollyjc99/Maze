import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 120, 255))
        self.rect = self.image.get_rect()
        self.rect.center = 300,250
        self.val = 5

    def update(self, win, border):
        w, h = win.get_size()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if not self.rect.left <= 0:
                self.rect.x -= self.val

            if not self.rect.collidelist(border) == -1:
                self.rect.x += self.val

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if not self.rect.right >= w:
                self.rect.x += self.val

            if not self.rect.collidelist(border) == -1:
                self.rect.x -= self.val

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if not self.rect.top <= 0:
                self.rect.y -= self.val

            if not self.rect.collidelist(border) == -1:
                self.rect.y += self.val

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if not self.rect.bottom >= h:
                self.rect.y += self.val

            if not self.rect.collidelist(border) == -1:
                self.rect.y -= self.val


class Block(pygame.sprite.Sprite):
    def __init__(self, rect, colour=(177, 156, 217)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(colour)
        self.rect = rect


class Map(object):
    def __init__(self, name, grid, start, final):
        self.name = name
        self.grid = grid
        self.start = self.get_start(start)
        self.final = self.get_accept(final)
        self.border = self.get_border()

    def get_border(self):
        return [pygame.Rect(col[1], col[2], 40, 40) for row in self.grid for col in row if col[0] == (245, 205, 222)]

    def get_start(self, start):
        return pygame.Rect(*start, 40, 40)

    def get_accept(self, final):
        return pygame.Rect(*final, 40, 40)
