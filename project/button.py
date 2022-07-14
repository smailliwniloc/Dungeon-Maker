import pygame as pg
import aesthetics as ae

pg.init()

class Button:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.text = text
        self.color = ae.SECONDARY_COLOR
        self.txt_surface = ae.FONT.render(text, True, self.color)

    def handle_event(self, event, box):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                box.history = []

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)
