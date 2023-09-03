
from campy.graphics.gwindow import GWindow

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 100  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.paddle_offset = PADDLE_OFFSET
        self.window_width = (brick_cols * (brick_width + brick_spacing) - brick_spacing) * 1.3
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)



        # create the scorecard on the right
        self.scorecard = GRect(width=self.window_width / 5, height=self.window_height)
        self.scorecard.filled = True
        self.scorecard.color = self.scorecard.fill_color = 'grey'
        # add scorecard below



        # create outline
        self.outline = GRect(width=self.window_width - self.scorecard.width, height=self.window_height - 1)
        self.outline.filled = True
        self.outline.color = 'ivory'
        self.outline.fill_color = 'black'
        self.outline._line_width = 10.0
        self.window.add(self.outline)

        # background
        self.background = GImage('earth.jpg')

        self.window.add(self.background, x= 3, y= 320)

        # add scorecard here
        self.window.add(self.scorecard, x=self.window.width - self.scorecard.width, y=0)




        # create the round
        self.round = GLabel('Round')
        self.round.color = 'blue'
        self.window.add(self.round, x=self.window.width - self.scorecard.width / 2 - self.round.width, y=70)
        self.round.font = 'Times-24-bold'

        self.roundsquare = GRect(self.round.width, self.round.height)
        self.roundsquare.filled = True
        self.roundsquare.color = 'slategray'
        self.window.add(self.roundsquare, x=self.round.x, y=self.round.y)

        self.labelround = GLabel('01')
        self.labelround.color = 'green'
        self.window.add(self.labelround, x=self.window.width - self.scorecard.width / 2 - self.labelround.width / 1.3,
                        y=self.round.y + 2*self.labelround.height )
        self.labelround.font = 'Times-24-bold'

        # create the label of score
        self.label1 = GLabel('Score')
        self.label1.color = 'blue'
        self.window.add(self.label1, x=self.window.width - self.scorecard.width / 2 - self.label1.width, y=150)
        self.label1.font = 'Times-24-bold'

        self.scoresquare = GRect(self.round.width, self.label1.height)
        self.scoresquare.filled = True
        self.scoresquare.color = 'slategray'
        self.window.add(self.scoresquare, x=self.roundsquare.x, y=self.label1.y)

        self.labelscore = GLabel('00')
        self.labelscore.color = 'green'
        self.window.add(self.labelscore, x=self.labelround.x-5, y=self.scoresquare.y + self.scoresquare.height + 3)
        self.labelscore.font = 'Times-24-bold'

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = self.paddle.color = 'ivory'
        self.window.add(self.paddle, x=(self.window_width - paddle_width) / 2,
                        y=self.window_height - self.paddle_offset)

        # make paddle a ship
        self.ship_l = GRect(paddle_width / 4, paddle_height + 4)
        self.ship_l.filled = True
        self.ship_l.fill_color = 'tomato'
        self.window.add(self.ship_l, x=self.paddle.x, y=self.paddle.y - 2)

        self.ship_r = GRect(paddle_width / 4, paddle_height + 4)
        self.ship_r.filled = True
        self.ship_r.fill_color = 'tomato'
        self.window.add(self.ship_r, x=self.paddle.x + self.paddle.width,
                        y=self.paddle.y - 2)


        # create the space of ship
        self.label2 = GLabel('Ships')
        self.label2.color = 'crimson'
        self.window.add(self.label2, x=self.window.width - self.scorecard.width / 2 - self.label2.width, y=400)
        self.label2.font = 'Times-24-bold'

        self.shipspace = GRect(self.paddle.width + 1.5 * self.ship_l.width, 10 * self.paddle.height,
                               x=self.label2.x - 17, y=self.label2.y + 3)
        self.shipspace.filled = True
        self.shipspace.color = 'slategray'

        self.window.add(self.shipspace)

        # add ship waiting in the right
        self.paddle1 = GRect(paddle_width, paddle_height)
        self.paddle1.filled = True
        self.paddle1.fill_color = self.paddle.color = 'ivory'
        self.window.add(self.paddle1, x=self.shipspace.x + 7,
                        y=self.window.height - self.paddle_offset - 8 * self.paddle.height)
        self.ship_l1 = GRect(paddle_width / 4, paddle_height + 4)
        self.ship_l1.filled = True
        self.ship_l1.fill_color = 'tomato'
        self.window.add(self.ship_l1, x=self.paddle1.x, y=self.paddle1.y - 2)
        self.ship_r1 = GRect(paddle_width / 4, paddle_height + 4)
        self.ship_r1.filled = True
        self.ship_r1.fill_color = 'tomato'
        self.window.add(self.ship_r1, x=self.ship_l1.x + self.paddle.width, y=self.ship_l1.y)

        self.paddle2 = GRect(paddle_width, paddle_height)
        self.paddle2.filled = True
        self.paddle2.fill_color = self.paddle.color = 'ivory'
        self.window.add(self.paddle2, x=self.shipspace.x + 7,
                        y=self.window.height - self.paddle_offset - 4 * self.paddle.height)
        self.ship_l2 = GRect(paddle_width / 4, paddle_height + 4)
        self.ship_l2.filled = True
        self.ship_l2.fill_color = 'tomato'
        self.window.add(self.ship_l2, x=self.paddle2.x, y=self.paddle2.y - 2)
        self.ship_r2 = GRect(paddle_width / 4, paddle_height + 4)
        self.ship_r2.filled = True
        self.ship_r2.fill_color = 'tomato'
        self.window.add(self.ship_r2, x=self.paddle2.x + self.paddle.width, y=self.ship_l2.y)

        # Draw bricks
        for i in range(BRICK_COLS):
            self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
            i = (self.brick.height + BRICK_SPACING) * i
            for j in range(BRICK_ROWS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                if j % 3 == 0:
                    self.brick.color = self.brick.fill_color = 'blue'
                elif j % 3 == 1:
                    self.brick.color = self.brick.fill_color = 'green'
                elif j % 3 == 2:
                    self.brick.color = self.brick.fill_color = 'red'
                j = (self.brick.width + BRICK_SPACING) * j
                self.window.add(self.brick, x=self.outline.line_width + j, y=40 + i)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.color = self.ball.fill_color = 'ivory'
        self.window.add(self.ball, x=(self.window_width - self.scorecard.width - ball_radius) / 2,
                        y=self.window_height / 2)
        # self.window.add(self.ball, x=0,
        #                 y=self.window_height / 2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        self.ballmoving = True
        onmouseclicked(self.ball_move)
        self.restart = 0
        onmousemoved(self.paddle_move)



    def ball_move(self, mouse):

        self.ballmoving = False

        # if 0 >= self.ball.y >= self.window.height - self.ball.height:
        # self.set_v()

    def paddle_move(self, mouse):
        self.paddle.x = mouse.x - PADDLE_WIDTH / 2
        if self.ball.y >= self.window.height and 0 <= self.restart <= 3:
            self.restart += 1
            # self.paddle.y = self.window.height - PADDLE_OFFSET * (1 + 2 * (self.restart - 1))

        self.ship_l.x = self.paddle.x
        self.ship_l.y = self.paddle.y - 2
        self.ship_r.x = self.paddle.x + self.paddle.width
        self.ship_r.y = self.paddle.y - 2
        if self.paddle.x <= 1:
            self.paddle.x = 1
            self.ship_l.x = 1
            self.ship_r.x = self.paddle.width

        elif self.paddle.x + self.paddle.width + self.ship_r.width >= self.scorecard.x:
            self.paddle.x = self.window.width - self.scorecard.width - self.paddle.width - self.ship_r.width - 1
            self.ship_l.x = self.paddle.x - 1
            self.ship_r.x = self.paddle.x + self.paddle.width - 1

    def set_v(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = random.randint(INITIAL_Y_SPEED, INITIAL_Y_SPEED + 7)
        if random.random() > 0.5:
            self.__dx *= -1
        # if random.random() > 0.5:
        #     self.__dy *= -1
        # self.ball.move(self.__dx, self.__dy)

    def get_x(self):
        return self.__dx

    def get_y(self):
        return self.__dy

    def get_life(self):
        return self.restart

    def get_score(self):
        return self.labelscore

