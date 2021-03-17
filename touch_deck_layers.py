from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

MEDIA = 1
KEY = 2

touch_deck_config = {
    "layers":[
        {
            "name": "Youtube Controls",
            "shortcuts": [
                {
                    "label": "Play",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (KEY, [Keycode.K])
                },
                {
                    "label": "Pause",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (KEY, [Keycode.K])
                },
                {
                    "label": "FastForward",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (KEY, [Keycode.RIGHT_ARROW])
                },
                {
                    "label": "Rewind",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (KEY, [Keycode.LEFT_ARROW])
                },
                {
                    "label": "Next",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.N])
                },
                {
                    "label": "Vol -",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (MEDIA, ConsumerControlCode.VOLUME_DECREMENT)
                },
                {
                    "label": "Vol +",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (MEDIA, ConsumerControlCode.VOLUME_INCREMENT)
                },
                {
                    "label": "Test (T)",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (KEY, [Keycode.T])
                },
                {
                    "label": "Test (E)",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (KEY, [Keycode.E])
                },
                {
                    "label": "Test (S)",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (KEY, [Keycode.S])
                },
                {
                    "label": "Test (T)",
                    "icon": "touch_deck_icons/80px_test_icon.bmp",
                    "actions": (KEY, [Keycode.T])
                },
                {
                    "label": "Adafruit",
                    "icon": "touch_deck_icons/Adafruit_logo_48x48x32.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.SEMICOLON, Keycode.ZERO])
                }
            ]
        },
        {
            "name": "Test Second Layer",
            "shortcuts": [
                {
                    "label": "Test (T)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.T])
                },
                {
                    "label": "Test (E)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.E])
                },
                {
                    "label": "Test (S)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.S])
                },
                {
                    "label": "Test (T)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.T])
                },
                {
                    "label": "Test [:)]",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.SEMICOLON, Keycode.ZERO])
                }
            ]
        },
        {
            "name": "Test Third Layer",
            "shortcuts": [
                {
                    "label": "Test (3)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.THREE])
                },
                {
                    "label": "Test (R)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.R])
                },
                {
                    "label": "Test (D)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.D])
                },
                {
                    "label": "Test (L)",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.L])
                },
                {
                    "label": "Test [:)]",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.SEMICOLON, Keycode.ZERO])
                }
            ]
        }
    ]
}