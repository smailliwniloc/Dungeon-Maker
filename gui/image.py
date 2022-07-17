import pygame as pg


class Image:
    def __init__(self, image_ref, x, y):
        self.image = pg.image.load(image_ref).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)

    def resize(self, size):
        self.image = pg.transform.scale(self.image, size)