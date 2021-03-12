# SPDX-FileCopyrightText: 2021 Tim C, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""

"""
import time
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
import adafruit_imageload
import adafruit_touchscreen

# use built in display (PyPortal, PyGamer, PyBadge, CLUE, etc.)
# see guide for  up external displays (TFT / OLED breakouts, RGB matrices, etc.)
# https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-and-display-bus
from adafruit_displayio_layout.widgets.control import Control
from adafruit_displayio_layout.widgets.widget import Widget
from displayio import Group

COOLDOWN_TIME = 0.25
LAST_PRESS_TIME = -1

current_layer = 0

display = board.DISPLAY

# Make the display context
main_group = displayio.Group(max_size=10)
display.show(main_group)

config_obj = {
    "layers":[
        {
            "name": "Layer 0",
            "shortcuts": [
                {
                    "label": "Play",
                    "icon": "images/test32_icon.bmp",
                    "actions": ["A"]
                },
                {
                    "label": "Pause",
                    "icon": "images/test32_icon.bmp",
                    "actions": ["A"]
                },
                {
                    "label": "FastForward",
                    "icon": "images/test32_icon.bmp",
                    "actions": ["A"]
                },
                {
                    "label": "Rewind",
                    "icon": "images/test32_icon.bmp",
                    "actions": ["A"]
                },
                {
                    "label": "Stop",
                    "icon": "images/test32_icon.bmp",
                    "actions": ["A"]
                }
            ]
        }
    ]
}
class IconWidget(Widget, Control):
    def __init__(self, label_text, icon, **kwargs):
        super().__init__(**kwargs)
        image, palette = adafruit_imageload.load(icon)
        tile_grid = displayio.TileGrid(image, pixel_shader=palette)
        self.append(tile_grid)
        _label = label.Label(
            terminalio.FONT, scale=1, text=label_text,
            anchor_point=(0.5, 0), anchored_position=(image.width // 2, image.height)
        )
        self.append(_label)
        self.touch_boundary = (self.x, self.y, image.width, image.height + _label.bounding_box[3])

    def contains(self, touch_point):  # overrides, then calls Control.contains(x,y)
        """
        """
        touch_x = (
                touch_point[0] - self.x
        )  # adjust touch position for the local position
        touch_y = touch_point[1] - self.y

        return super().contains((touch_x, touch_y, 0))

ts = adafruit_touchscreen.Touchscreen(
    board.TOUCH_XL,
    board.TOUCH_XR,
    board.TOUCH_YD,
    board.TOUCH_YU,
    calibration=((5200, 59000), (5800, 57000)),
    size=(display.width, display.height),
)


layout = GridLayout(
    x=10,
    y=10,
    width=300,
    height=220,
    grid_size=(4, 3),
    cell_padding=8,
    max_size=10,
)

_icons = []

_pressed_icons = []

"""
for i in range(12):
    _new_icon = IconWidget("Shortcut {}".format(i), "images/test32_icon.bmp")
    _icons.append(_new_icon)
    layout.add_content(_new_icon, grid_position=(i%4, i//4), cell_size=(1, 1))

"""

for i, shortcut in enumerate(config_obj["layers"][current_layer]["shortcuts"]):
    _new_icon = IconWidget(shortcut["label"], shortcut["icon"])
    _icons.append(_new_icon)
    layout.add_content(_new_icon, grid_position=(i%4, i//4), cell_size=(1, 1))

main_group.append(layout)
while True:
    p = ts.touch_point
    if p:
        _now = time.monotonic()
        if _now - LAST_PRESS_TIME > COOLDOWN_TIME:
            for index, icon_shortcut in enumerate(_icons):
                if icon_shortcut.contains(p):
                    if index not in _pressed_icons:
                        print("pressed {}".format(index))
                        LAST_PRESS_TIME = time.monotonic()
                        _pressed_icons.append(index)
                elif index in _pressed_icons:
                    _pressed_icons.remove(index)