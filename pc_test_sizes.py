# SPDX-FileCopyrightText: 2020 Tim C, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
This version runs on the PC for testing interface in a window
mocked to the same size as the Featherwing.
"""
import displayio
import pygame
import terminalio
from adafruit_display_text import label
import time
import displayio
import terminalio
from adafruit_display_text import label, bitmap_label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from touch_deck_layers import touch_deck_config, KEY
from adafruit_button import Button
from adafruit_displayio_layout.widgets.icon_widget import IconWidget
from blinka_displayio_pygamedisplay import PyGameDisplay


# Make the display context. Change size if you want
display = tft_featherwing.display


COOLDOWN_TIME = 0.25
LAST_PRESS_TIME = -1

current_layer = 0

# Make the display context
main_group = displayio.Group(max_size=10)
display.show(main_group)


layout = GridLayout(
    x=20,
    y=40,
    width=420,
    height=290,
    grid_size=(4, 3),
    cell_padding=6,
    max_size=20,
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
    x=display.width - 50,
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
    x=display.width - 50,
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
while display.running:
    ev = pygame.event.get(eventtype=pygame.MOUSEBUTTONUP)
    # proceed events
    for event in ev:
        p = pygame.mouse.get_pos()

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
                                print(*touch_deck_config["layers"][current_layer]["shortcuts"][index]["actions"][1])

                            else:
                                print(touch_deck_config["layers"][current_layer]["shortcuts"][index]["actions"][1])
                            LAST_PRESS_TIME = time.monotonic()
                            _pressed_icons.append(index)
                    elif index in _pressed_icons:
                        _pressed_icons.remove(index)



