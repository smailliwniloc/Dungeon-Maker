import paths

DISPLAY_NAME = "Dungeon Maker"
DISPLAY_SIZE = (700, 500)

COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "yellow": (255, 220, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "indigo": (75, 0, 130),
    "magenta": (255, 0, 255),
    "panel": (255, 0, 0)
}

FONTS = {"main": paths.fontPath + "SourceSansPro-Light.ttf",
         "main-bold": paths.fontPath + "SourceSansPro-Semibold.ttf",
         "main-italic": paths.fontPath + "SourceSansPro-LightIt.ttf",
         "main-bold-italic": paths.fontPath + "SourceSansPro-SemiboldIt.ttf",
         "sizes":
             {"large": 20,
              "medium": 15,
              "small": 12},
         "color": COLORS["blue"]}