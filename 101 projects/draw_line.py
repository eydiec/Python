"""
File: SC101Assignment1
Name: Eydie
-------------------------
TODO: the program will identify every click. if its the odd click, there
will be a circle, otherwise, there will be a line connecting the circle and the
next click, the circle disappeared in the meanwhile
"""

from campy.graphics.gobjects import GOval, GLine, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
count = 1
window = GWindow()
count_Label = GLabel('Score: ' + str(count))
ball = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    global count

    onmouseclicked(add)


def add(mouse):
    global count

    if count % 2 == 1:  # the first time will show the ball
        ball.filled = False
        ball.fill_color = 'black'
        window.add(ball, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)

        count_Label.text = 'Score: ' + str(count)


    else:
        # the second time, which is counted as 1+2n, will not show the ball, but a line in between

        window.remove(ball)
        Line = GLine(ball.x, ball.y, mouse.x, mouse.y)
        window.add(Line)
    count += 1


if __name__ == "__main__":
    main()
