# Credit given to John Park <https://learn.adafruit.com/users/johnpark>
# at Adafruit for original code and art assets.
# https://learn.adafruit.com/halloween-countdown-display-matrix/code-the-halloween-countdown
# ** No original license provided **

import time
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal


FRAME_DURATION = 5
FRAMES = (
    "bmps/kitty.bmp",
    "bmps/green-ghost.bmp",
    "you have \nno real \nfriends",
    "bmps/roy.bmp",
    "bmps/bats.bmp",
    "your\nrecycling\ngoes to \na \nlandfill",
    "bmps/jack.bmp",
    "bmps/roynose.bmp",
    "gas\nprices\nwill\nnever\ncome\ndown",
    "bmps/spooky.bmp",
    "bmps/bats2.bmp",
    "we will\nrent\nforever",
    "bmps/ghost.bmp",
)

SYNCHRONIZE_CLOCK = True

FONT = "/ib8x8u.bdf"

# --- Display setup ---
matrixportal = MatrixPortal(
    status_neopixel=board.NEOPIXEL,
    debug=True,
    height=64,
    width=64,
    serpentine=True,
    tile_rows=2)

matrixportal.add_text(
    text_font=FONT,
    text_position=((matrixportal.graphics.display.width // 12) - 4,
                   (matrixportal.graphics.display.height // 2) - 1),
    text_color=0x800000
)

current_frame = None


def set_next_frame():
    # pylint: disable=global-statement
    global current_frame

    # Advance to next frame if we already have one
    if current_frame is not None:
        current_frame += 1

    # Loop back or set initial frame
    if current_frame is None or current_frame >= len(FRAMES):
        current_frame = 0

    # Check if Picture or Text
    print(FRAMES[current_frame])
    matrixportal.set_text("")

    if FRAMES[current_frame][-4:] == ".bmp":
        matrixportal.set_background(FRAMES[current_frame], position=(0, 0))
    else:
        matrixportal.set_background(None, position=(0, 16))
        matrixportal.set_text(FRAMES[current_frame])


# Simulate the delay in case fetching time is fast
set_next_frame()
start_time = time.monotonic()

while time.monotonic() < start_time + FRAME_DURATION:
    pass

while True:
    set_next_frame()
    time.sleep(FRAME_DURATION)
