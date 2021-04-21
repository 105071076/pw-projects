"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This is the the extension of the breakout game.
The score board will move around the window and when the ball hits the score board,
the ball will bounce the opposite direction.
When the user hits all the bricks, he wins.
When there is no more lives or the user hits all the bricks, the game ends.

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10 # Number of rows of bricks.
BRICK_COLS = 10 # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels). 75
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels). 15
PADDLE_OFFSET = 100  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        self.ball_radius = BALL_RADIUS
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = 'True'

        # Center a filled ball in the graphical window
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle_offset = PADDLE_OFFSET
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=self.window.height - paddle_offset)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = 'True'
                self.brick.color = 'black'

                self.window.add(self.brick, x=(brick_width * j + brick_spacing * j),
                                y=brick_offset + brick_height * i + brick_spacing * i)

                if (i+j)% 2 == 0:
                    self.brick.fill_color = 'ivory'
                else:
                    self.brick.fill_color = 'black'

        # Create label when user hits 10 balls
        self.half = GLabel("WOW! TEN BRICKS ALREADY! KEEP GOING!")
        self.half.font = '-15'

        # Score cnt
        self.score_cnt = 0
        self.score = GLabel('SCORE:' + str(self.score_cnt))
        self.score.font = 'Helvetica-30-bold'
        self.score.color = 'silver'
        self.vx = 0
        self.vy = 0

        # Life 
        self.life = GLabel('LIVES:')
        self.life.font = 'Helvetica-30'
        self.life.color = 'plum'
        self.life1 = GOval(20, 20)
        self.life1.filled = True
        self.life1.fill_color = 'plum'
        self.life1.color = 'plum'
        self.life2 = GOval(20, 20)
        self.life2.filled = True
        self.life2.fill_color = 'plum'
        self.life2.color = 'plum'
        self.life3 = GOval(20, 20)
        self.life3.filled = True
        self.life3.fill_color = 'plum'
        self.life3.color = 'plum'

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.lives = 3
        onmouseclicked(self.start_ball)
        onmousemoved(self.track_paddle)

    def start_ball(self, event):
        if (self.__dx == 0) and (self.__dy == 0) and (not self.lives == 0):
            self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                            y=(self.window.height - self.ball.height) / 2)
            self.ball.fill_color = 'black'
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
            if random.random() > 0.5:
                self.__dy = -self.__dy
        return True

    def track_paddle(self, e):
        self.paddle.x = e.x - self.paddle.width / 2
        # make sure the paddle will always be in the window
        if e.x <= 0:
            self.paddle.x = 0
        elif e.x > self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width

    def check_wall(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width > self.window.width:
            self.__dx = -self.__dx

        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def check_pts(self):

        p1 = self.window.get_object_at(self.ball.x, self.ball.y)
        p2 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
        p3 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
        p4 = self.window.get_object_at(self.ball.x + self.ball_radius * 2,
                                           self.ball.y + self.ball_radius * 2)

        if p2 is not None:
            # determine which item the ball hits
            if self.ball.y > self.window.height/2:
                if self.__dy > 0:
                    self.__dy = -self.__dy
                self.ball.fill_color = 'red'
            else:
                if p2 != self.half and p2 != self.score \
                        and p2 != self.life and p2!=self.life1 and p2!= self.life2 and p2!= self.life3 :
                    self.window.remove(p2)
                    self.score_cnt += 1
                    self.score.text = ("SCORE: " + str(self.score_cnt))
                    self.__dy = -self.__dy
                self.ball.fill_color = 'gold'

        elif p4 is not None:
            if self.ball.y > self.window.height/2:
                if self.__dy > 0:
                    self.__dy = -self.__dy
                self.ball.fill_color = 'red'
            else:
                if p4 != self.half and p4 != self.score \
                        and p4 != self.life and p4!=self.life1 and p4 != self.life2 and p4 != self.life3:
                    self.window.remove(p4)
                    self.score_cnt += 1
                    self.score.text = ("SCORE: " + str(self.score_cnt))
                    self.__dy = -self.__dy
                self.ball.fill_color = 'gold'

        elif p1 is not None:
            if self.ball.y > self.window.height/2:
                if self.__dy > 0:
                    self.__dy = -self.__dy
                self.ball.fill_color = 'red'
            else:
                if p1 != self.half and p1 != self.score \
                        and p1 != self.life and p1 != self.life1 and p1 != self.life2 and p1 != self.life3:
                    self.window.remove(p1)
                    self.score_cnt += 1
                    self.score.text = ("SCORE: " + str(self.score_cnt))
                    self.__dy = -self.__dy
                self.ball.fill_color = 'gold'

        elif p3 is not None:
            if self.ball.y > self.window.height/2:
                if self.__dy > 0:
                    self.__dy = -self.__dy
                self.ball.fill_color = 'red'
            else:
                if p3 != self.half and p3 != self.score \
                        and p3 != self.life and p3 !=self.life1 and p3 != self.life2 and p3 != self.life3:
                    self.window.remove(p3)
                    self.score_cnt += 1
                    self.score.text = ("SCORE: " + str(self.score_cnt))
                    self.__dy = -self.__dy
                self.ball.fill_color = 'gold'

    def score_run(self):
        if self.vx == 0 and self.vy == 0:
            self.vx = 5
            self.vy = 3

        elif (self.score.x <= 0) or (self.score.x + self.score.width >= self.window.width):
            self.vx = -self.vx
            self.score.color = 'salmon'

        elif (self.score.y - self.score.height <= 0) or (self.score.y >= self.window.height)and self.vy > 0:
            self.vy = -self.vy
            self.score.color = 'powderblue'

        self.score.move(self.vx, self.vy)

    def cheer(self):
        # Cheering words
        obj = self.window.get_object_at(x=(self.window.width - self.half.width) / 2,
                                            y=(self.window.height - self.half.height) / 2)
        if obj is None and self.score_cnt == 10:
            self.window.add(self.half, x=(self.window.width - self.half.width) / 2,
                                y=(self.window.height - self.half.height) / 2)

        if self.score_cnt == 15:
            self.window.remove(self.half)





    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_speed):
        self.__dx = -self.__dx

    def set_dy(self, new_speed):
        self.__dy = -self.__dy

    def set2_dx(self, new_speed2):
        self.__dx = 0

    def set2_dy(self, new_speed2):
        self.__dy = 0


