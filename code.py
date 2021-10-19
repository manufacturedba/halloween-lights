# Credit given to John Park <https://learn.adafruit.com/users/johnpark>
# at Adafruit for original code and art assets.
# https://learn.adafruit.com/halloween-countdown-display-matrix/code-the-halloween-countdown
# ** No original license provided **

import time
import board
from adafruit_matrixportal.matrixportal import MatrixPortal


FRAME_DURATION = 5
FRAMES = (
    "bmps/bats.bmp",
    "bmps/jack.bmp",
    "bmps/green-ghost.bmp",
    "bmps/spooky.bmp",
    "bmps/scary.bmp",
    "bmps/bats2.bmp",
    "bmps/ghost.bmp",
)

SYNCHRONIZE_CLOCK = True

# --- Display setup ---
matrixportal = MatrixPortal(
    status_neopixel=board.NEOPIXEL,
    debug=True,
    height=64,
    width=64,
    serpentine=True, 
    tile_rows=2)

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
    if FRAMES[current_frame][-4:] == ".bmp":
        matrixportal.set_background(FRAMES[current_frame], position=(0, 16))
        matrixportal.set_text("")


# Simulate the delay in case fetching time is fast
set_next_frame()
start_time = time.monotonic()
if SYNCHRONIZE_CLOCK:
    matrixportal.get_local_time()

while time.monotonic() < start_time + FRAME_DURATION:
    pass

while True:
    set_next_frame()
    time.sleep(FRAME_DURATION)
