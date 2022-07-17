import pygame as pg
import sys
from pygame.locals import *
from project.aesthetics import *


# Data Definition
class helloWorld:
    '''Create a resizable hello world window'''
    def __init__(self):
        pg.init()
        self.width = 300
        self.height = 300
        DISPLAYSURF = pg.display.set_mode((self.width,self.height), RESIZABLE)
        DISPLAYSURF.fill(WHITE)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == VIDEORESIZE:
                    self.CreateWindow(event.w,event.h)
            pg.display.update()

    def CreateWindow(self,width,height):
        '''Updates the window width and height '''
        pg.display.set_caption("Press ESC to quit")
        DISPLAYSURF = pg.display.set_mode((width,height),RESIZABLE)
        DISPLAYSURF.fill(WHITE)


if __name__ == '__main__':
    helloWorld().run()
