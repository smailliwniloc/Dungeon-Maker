import constants
import paths

import pygame as pg
from project.chat_panel import ChatPanel
import project.menus as menus
import project.test2 as game
# import project.game.controller as game


class ApplicationController:
    """ runs the whole application, changing section running based on state """
    def __init__(self):
        pg.init()

        # Icon Setup
        icon = pg.image.load(paths.uiMenuPath + "foo.png")
        icon.set_colorkey((0, 0, 0))
        pg.display.set_icon(icon)  # before set_mode as suggested in pygame docs

        # Display Setup
        self.display = pg.display.set_mode(constants.DISPLAY_SIZE)
        pg.display.set_caption(constants.DISPLAY_NAME)

        # General Setup
        self.state = "menu"
        self.game_reference = None

    def run(self):
        while self.state != "quit":
            if self.state == "menu":
                self.run_menu()

            elif self.state == "load_game":
                self.run_loadgame()

            elif self.state == "new_game":
                self.run_newgame()

            elif self.state == "leaderboard":
                self.run_leaderboard()

            elif self.state == "game":
                self.run_game()

            else:
                raise Exception("Invalid Game State: %s" % self.state)

        self.quit()

    def run_menu(self):
        menu = menus.Menu(self.display)  # takes control while section running, control returns here after.
        self.state = menu.get_state()

    def run_loadgame(self):
        chat = ChatPanel((constants.DISPLAY_SIZE[0]/2, constants.DISPLAY_SIZE[1]), self.display)
        self.state = chat.get_state()
        # load_game = menus.LoadGame(self.display)
        # self.state = load_game.get_state()
        # self.game_reference = load_game.get_game()

    def run_newgame(self):
        game.main()

    def run_leaderboard(self):
        print("in run_leaderboard")
        # leaderboard = menus.Leaderboard(self.display)
        # self.state = leaderboard.get_state()

    def run_game(self):
        print("in run_game")
        # if self.game_reference is None:
        #     raise Exception("No Game Selected")

        # running_game = game.Controller(self.display, self.game_reference)
        # self.state = running_game.play()  # takes control, returns when game is complete.
        # self.game_reference = None

    def quit(self):
        pg.quit()
        quit()
        
