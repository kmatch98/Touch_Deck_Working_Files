# SPDX-FileCopyrightText: 2021 Tim C, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""

"""
import time
import board
import displayio
import terminalio
from adafruit_display_text import label, bitmap_label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
import adafruit_touchscreen
from touch_deck_layers import touch_deck_config, KEY
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_button import Button

from adafruit_displayio_layout.widgets.icon_widget import IconWidget

COOLDOWN_TIME = 0.25
LAST_PRESS_TIME = -1

current_layer = 0

# use built in display (PyPortal, PyGamer, PyBadge, CLUE, etc.)
# see guide for  up external displays (TFT / OLED breakouts, RGB matrices, etc.)
# https://learn.adafruit.com/circuitpython-display-support-using-displayio/display-and-display-bus
display = board.DISPLAY

# Make the display context
main_group = displayio.Group(max_size=10)
display.show(main_group)

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

ts = adafruit_touchscreen.Touchscreen(
    board.TOUCH_XL,
    board.TOUCH_XR,
    board.TOUCH_YD,
    board.TOUCH_YU,
    calibration=((5200, 59000), (5800, 57000)),
    size=(display.width, display.height),
)

layout = GridLayout(
    x=0,
    y=20,
    width=300,
    height=210,
    grid_size=(4, 3),
    cell_padding=6,
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

layer_label = bitmap_label.Label(terminalio.FONT)
layer_label.anchor_point = (0.5, 0.0)
layer_label.anchored_position = (display.width // 2, 4)
main_group.append(layer_label)

next_layer_btn = Button(
    x=layout.x + layout._width - 12,
    y=display.height - 70,
    width=50,
    height=70,
    style=Button.RECT,
    fill_color=0x00ff99,
    label="",
    label_font=terminalio.FONT,
    label_color=0x000000,
)

main_group.append(next_layer_btn)

home_layer_btn = Button(
    x=layout.x + layout._width - 12,
    y=0,
    width=50,
    height=70,
    style=Button.RECT,
    fill_color=0xFF9900,
    label="",
    label_font=terminalio.FONT,
    label_color=0x000000,
)

main_group.append(home_layer_btn)


def load_layer(layer_index):
    # remove everything from self
    global _icons
    _icons = []
    layout._cell_content_list = []

    while len(layout) > 0:
        layout.pop()

    layer_label.text = touch_deck_config["layers"][layer_index]["name"]
    for i, shortcut in enumerate(touch_deck_config["layers"][layer_index]["shortcuts"]):
        _new_icon = IconWidget(shortcut["label"], shortcut["icon"])
        _icons.append(_new_icon)
        layout.add_content(_new_icon, grid_position=(i % 4, i // 4), cell_size=(1, 1))


load_layer(current_layer)
main_group.append(layout)
while True:
    p = ts.touch_point
    if p:
        _now = time.monotonic()
        if _now - LAST_PRESS_TIME > COOLDOWN_TIME:
            if next_layer_btn.contains(p):
                current_layer += 1
                if current_layer >= len(touch_deck_config["layers"]):
                    current_layer = 0

                load_layer(current_layer)
                LAST_PRESS_TIME = time.monotonic()
            if home_layer_btn.contains(p):
                current_layer = 0
                load_layer(current_layer)
                LAST_PRESS_TIME = time.monotonic()

            for index, icon_shortcut in enumerate(_icons):
                if icon_shortcut.contains(p):
                    if index not in _pressed_icons:
                        print("pressed {}".format(index))
                        print(touch_deck_config["layers"][current_layer]["shortcuts"][index]["actions"][1])
                        if touch_deck_config["layers"][current_layer]["shortcuts"][index]["actions"][0] == KEY:
                            kbd.press(*touch_deck_config["layers"][current_layer]["shortcuts"][index]["actions"][1])
                            kbd.release_all()
                        else:
                            cc.send(touch_deck_config["layers"][current_layer]["shortcuts"][index]["actions"][1])
                        LAST_PRESS_TIME = time.monotonic()
                        _pressed_icons.append(index)
                elif index in _pressed_icons:
                    _pressed_icons.remove(index)