import pygame as pg
import sys
# import server 
from project.inputBox import InputBox
import gui.button
import constants
import project.aesthetics as ae
# import pickle
pg.init()




def main():
    clock = pg.time.Clock()

    # Dimensions
    width = 500
    height = 500
    history_w_ratio = 0.4
    history_h_ratio = 14/15
    history_width = width*history_w_ratio
    history_height = height*history_h_ratio

    # Font
    base_font = pg.font.SysFont('calibri', 20)
    pg.key.set_repeat(200, 25)
    
    #Main screen
    screen = pg.display.set_mode((width, height), flags=pg.RESIZABLE)
    pg.display.set_caption("Test2")
    screen.fill(ae.SCREEN_COLOR)

    # History side-bar
    history = pg.Surface.subsurface(screen, (width - history_width, 0, history_width, history_height))
    history.fill(ae.HISTORY_COLOR)

    # create textbox rectangle
    input_rect = InputBox((1 + 1/70)*width - history_width, (69/70)*height - base_font.get_height(), (33/35)*history_width, 1.1*base_font.get_height(), text='Type Here')

    b = gui.TextButton((10, 40, 50, 20), 0, 100, "Clear", 
                        constants.FONTS["sizes"]["large"], constants.FONTS["color"], constants.FONTS["main"])
    b.set_function(input_rect.clearHistory)

    run = True

    while run:
        
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
            input_rect.handle_event(event)
            b.check_clicked()
            if event.type == pg.VIDEORESIZE:
                screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
                pg.display.set_caption("Test2")
                screen.fill(ae.SCREEN_COLOR)

                width = event.w
                height = event.h
                history_width = width*history_w_ratio
                history_height = height*history_h_ratio

                # History side-bar
                history = pg.Surface.subsurface(screen, (width - history_width, 0, history_width, history_height))
                history.fill(ae.HISTORY_COLOR)

        screen.fill(ae.SCREEN_COLOR)
        history.fill(ae.HISTORY_COLOR)

        input_rect.resize(width, height, history_width)

        # input_rect.update()
        input_rect.draw(screen)

        b.draw(screen)


        input_rect.printHistory(screen)


        pg.display.update()

        clock.tick(60)

main()
