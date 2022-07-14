# Dungeon-Maker
Randomly generates dungeon with enemies, terrain, and loot with online access for several players to interact


Packages needed:
    - pyinstaller
    - PySimpleGUI (redacted)
    - pyGame
    - random

Use pyinstaller (___).py to make python file an executable .exe

Use virtual environment if in VSCode (select interpreter and manually go to .venv/Scripts/python.exe if needed)

Currently at 1:27:35 at https://www.youtube.com/watch?v=McoDjOCb2Zo&t=1246s -- I have not changed server or client

Consider using dirty_rects to only update changed frames with display.update(dirty_rects) instead of updating the whole screen with display.update()

Look at https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame for multi-line text

Use groups and sprites for buttons/other reusable components

Inspiration from https://github.com/Ben-Ryder/Conqueror-of-Empires
