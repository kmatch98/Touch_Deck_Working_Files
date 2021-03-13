import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
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
                    "icon": "touch_deck_icons/Play_48x48.bmp",
                    "actions": (KEY, [Keycode.K])
                },
                {
                    "label": "Pause",
                    "icon": "touch_deck_icons/Pause_48x48.bmp",
                    "actions": (KEY, [Keycode.K])
                },
                {
                    "label": "FastForward",
                    "icon": "touch_deck_icons/test48_icon.bmp",
                    "actions": (KEY, [Keycode.RIGHT_ARROW])
                },
                {
                    "label": "Rewind",
                    "icon": "touch_deck_icons/Previous_48x48.bmp",
                    "actions": (KEY, [Keycode.LEFT_ARROW])
                },
                {
                    "label": "Next",
                    "icon": "touch_deck_icons/Next_48x48.bmp",
                    "actions": (KEY, [Keycode.RIGHT_SHIFT, Keycode.N])
                }
            ]
        }
    ]
}