import pygame


class Panel:
    def __init__(self, rect, transparency, color):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.transparency = transparency
        self.surface = self.make_surface()

    def reset_rect(self, rect):
        self.rect = pygame.Rect(rect)
        self.surface = self.make_surface()

    def reset_width(self, width):
        self.rect.width = width
        self.surface = self.make_surface()

    def make_surface(self):
        surface = pygame.Surface([self.rect[2], self.rect[3]])
        surface.set_alpha(self.transparency)
        return surface

    def draw(self, display):
        self.surface.fill(self.color)
        display.blit(self.surface, [self.rect[0], self.rect[1]])
