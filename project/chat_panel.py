import pygame as pg

import constants
import paths

import gui

class ChatEditor:
    def __init__(self):
        try:
            with open(paths.dataPath + "chat.txt", "r") as file:  # file formatted as: name1,message1+name2,message2+...
                self.data = []
                chat_data = file.read().split("+")
                # del chat_data[-1]  # always a + at end, removes empty player added to end.
                for messagePair in chat_data:
                    # print(messagePair)
                    message = messagePair.split(",")
                    self.data.append(message)
        except FileNotFoundError:
            self.data = []
            # data is [[name1, message1], [name2, message2], ...]

    def new_message(self, name, message):
        self.data.append([name, message])
        self.save()

    def save(self):
        with open(paths.dataPath + "chat", "w") as file:
            for messagePair in self.data:
                file.write(messagePair[0] + "," + messagePair[1] + "+")  # file formatted as: name1,message1+name2,message2+...

class ChatSlot:
    def __init__(self, name, message, x, y, w, h):
        # self.panel = gui.Panel([x, y, w, h], 100, constants.COLORS["panel"])
        # self.name = name
        # self.message = message

        self.name_text = gui.Text(
            name,
            constants.FONTS["sizes"]["medium"], constants.FONTS["color"], constants.FONTS["main"],
            x, y)

        self.nameWidth, self.textHeight = self.name_text.get_rect()[2:]

        self.message_text = gui.Text(
            ": {}".format(message),
            constants.FONTS["sizes"]["medium"], constants.FONTS["color"], constants.FONTS["main"],
            x + self.nameWidth, y)

    def draw(self, display):
        # self.panel.draw(display)
        self.name_text.draw(display)
        self.message_text.draw(display)

class ChatPanel:
    def __init__(self, size, screen):
        self.state = "load_game"
        self.screen = screen
        self.display = pg.Surface(size)
        self.display.fill(constants.COLORS["white"])

        self.entry = gui.Entry("Type Here", constants.FONTS["sizes"]["medium"], constants.FONTS["color"],
                                constants.FONTS["main"], 5, 5, 5, size[1]/2)

        self.chat_reader = ChatEditor()
        self.slots = []
        x, y = [10, self.display.get_height() - 40]
        padding = 20
        for player in self.chat_reader.data:
            self.slots.append(ChatSlot(player[0], player[1], x, y, 50, 20))
            y -= padding

        self.run()

    def run(self):
        while self.state == "load_game":
            self.handle_events()
            self.draw()

    def get_state(self):
        return self.state

    def handle_events(self):
        for event in pg.event.get():
            # print(event)
            if event.type == pg.QUIT:
                self.state = "quit"
                pg.quit()

            elif event.type == pg.MOUSEBUTTONDOWN:
                print("mouse clicked")
                # if self.back.check_clicked():
                #     self.state = "menu"

            self.entry.handle_event(event)

    def draw(self):
        for slot in self.slots:
            slot.draw(self.display)

        self.entry.draw(self.display)

        self.screen.blit(self.display, (self.screen.get_width()/2, 0))

        pg.display.update()