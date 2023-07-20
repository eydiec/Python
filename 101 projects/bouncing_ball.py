"""
File: SC101Assignment1
Name: Eydie
-------------------------
TODO: for the first three click, the ball will bounce back and fro,
firction is considered thus the height will be lower onwards
after three bounce, any click wont make any movement
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 10
DELAY = 100
GRAVITY = 3
SIZE = 20
REDUCE = 0.7
START_X = 30
START_Y = 40
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)  #
window = GWindow(800, 500, title='bouncing_ball.py')
Ha = True
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global Ha
    ball.filled = True
    window.add(ball)
    onmouseclicked(click)


def click(mouse):
    global Ha, count  # the 開關 and the counting will continue
    movey = 0  # the falling speed starts from 0

    if Ha and count < 3:
        while True:
            Ha = False  # to close the 開關 so any click wont affect in progress
            if ball.x + SIZE < window.width:
                ball.move(VX, movey)
                pause(DELAY)
                if ball.y + SIZE >= window.height:
                    movey *= -1  # the opposite direction if it hits the floor
                    movey *= REDUCE
                    ball.move(VX, movey)
                else:
                    movey += GRAVITY  # the falling speed adds on
                pause(DELAY)
            else:  # if the ball falls outside the window
                window.add(ball, x=START_X, y=START_Y)
                count += 1
                Ha = True
                break


if __name__ == "__main__":
    main()
