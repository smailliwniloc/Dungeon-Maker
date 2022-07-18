import constants
import paths
import pygame as pg
import gui.text
import gui.image


class Entry:
    def __init__(self,
                 initial_text, text_size, text_color, text_font, text_padx, text_pady,
                 x, y, size=(-1,-1)):
        rest_path = paths.uiMenuPath + "input-normal.png"
        hover_path = paths.uiMenuPath + "input-normal-hover.png"
        focued_path = paths.uiMenuPath + "input-normal-focused.png"
        hover_focued = paths.uiMenuPath + "input-normal-hover-focused.png"
        self.rest_image = gui.Image(rest_path, x, y)
        self.hover_image = gui.Image(hover_path, x, y)
        self.rest_focused_image = gui.Image(focued_path, x, y)
        self.hover_focused_image = gui.Image(hover_focued, x, y)

        if(size != (-1, -1)):
            self.rest_image.resize(size)
            self.hover_image.resize(size)
            self.rest_focused_image.resize(size)
            self.hover_focused_image.resize(size)

        self.rect = self.rest_image.rect
        self.rect.x = x
        self.rect.y = y
        self.text_padx = text_padx
        self.text_pady = text_pady
        self.active = False
        self.text = gui.Text(initial_text, text_size, text_color, text_font,
                                    self.rect.x+self.text_padx, self.rect.y+self.text_pady)

        self.initial_text = initial_text

    def get_text(self):
        return self.text.text

    def mouse_over(self):
        posx, posy = pg.mouse.get_pos()
        if self.rect.collidepoint((posx - constants.DISPLAY_SIZE[0]/2, posy)):
            return True
        return False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            posx, posy = event.pos
            if self.rect.collidepoint(posx - constants.DISPLAY_SIZE[0]/2, posy):
                # Toggle the active variable.
                if(not self.active):
                    self.text.change_text("")
                self.active = True
                print(self.active)
            else:
                if len(self.text.text) == 0:
                    self.active = False
                    self.text.change_text(self.initial_text)
        if event.type == pg.KEYDOWN and self.active:
            if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                self.history.append(self.text)
                self.text.change_text("")
            elif event.key == pg.K_BACKSPACE:
                self.text.change_text(self.text.text[:-1])
            else:
                self.text.change_text(self.text.text + event.unicode)

    def draw(self, display):
        if self.mouse_over() and self.active:
            self.hover_focused_image.draw(display)
        elif self.active:
            self.rest_focused_image.draw(display)
        elif self.mouse_over():
            self.hover_image.draw(display)
        else:
            self.rest_image.draw(display)
        self.text.draw(display)
