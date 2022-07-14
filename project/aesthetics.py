import pygame as pg

# Does this work?

BLACK  = (0, 0,0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE   = (0,0,255)

GREEN = (0,255,0)

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.SysFont('calibri', 20)


SCREEN_COLOR = (0,0,0)
HISTORY_COLOR = (255, 255, 255)
TEXTBOX_COLOR = (125, 125, 125)
SECONDARY_COLOR = pg.Color('saddlebrown')

def blit_text(surface, text, pos, font=FONT, color=BLACK):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def get_change(surface, text, pos, font = FONT):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    lines = 1
    width = 0
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, BLACK)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                width = max(x, width)
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
                lines += 1
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    return lines, width
