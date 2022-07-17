import pygame as pg


class Cursor:
    def __init__(self, imageref):
        pg.mouse.set_visible(False)
        self.image = pg.image.load(imageref).convert_alpha()
        
    def draw(self, surface):
        surface.blit(self.image, pg.mouse.get_pos())
