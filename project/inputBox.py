import pygame as pg
import project.aesthetics as ae
from project.aesthetics import blit_text


pg.init()
screen = pg.display.set_mode((640, 480))


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.minWidth = w
        self.minHeight = h
        self.color = ae.COLOR_INACTIVE
        self.startingText = text
        self.text = text
        self.txt_surface = ae.FONT.render(text, True, self.color)
        self.active = False
        self.history = []

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                if(not self.active):
                    self.text = ''
                self.active = True
            else:
                if len(self.text) == 0: self.active = False
                if len(self.text) == 0: self.text = self.startingText 
            # Change the current color of the input box.
            self.color = ae.COLOR_ACTIVE if self.active else ae.COLOR_INACTIVE
        if event.type == pg.KEYDOWN and self.active:
            if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                self.history.append(self.text)
                self.text = ''
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        # Re-render the text.
        self.txt_surface = ae.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.minWidth, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        # screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        lines, width = ae.get_change(screen, self.text, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        self.rect.w = max(self.minWidth, width)
        self.rect.h = lines*self.minHeight
        self.rect.y -= (lines-1)*self.minHeight
        ae.blit_text(screen, self.text, (self.rect.x+5, self.rect.y+5), color=ae.COLOR_ACTIVE)
        pg.draw.rect(screen, self.color, self.rect, 2)
        

    def resize(self, width, height, history_width):
        self.rect = pg.Rect((1 + 1/70)*width - history_width, (69/70)*height - ae.FONT.get_height(), (33/35)*history_width, 1.1*ae.FONT.get_height())

    def printHistory(self, screen):
        vert = self.rect.y - 5
        for s in self.history[::-1]:
            text_surface = ae.FONT.render(s, True, (0,0,0))
            # screen.blit(text_surface, (self.rect.x+5, vert-text_surface.get_height()))
            ae.blit_text(screen, s, (self.rect.x+5, vert-text_surface.get_height()))
            vert -= text_surface.get_height()

    def clearHistory(self):
        self.history = []

def main():
    clock = pg.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
