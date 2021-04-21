"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gobjects import GOval, GRect, GLabel
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000/120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts
life_cnt = NUM_LIVES
graphics = BreakoutGraphics()



def main():

    global graphics, life_cnt
    graphics.window.add(graphics.score, 250, graphics.score.height + 3)
    graphics.window.add(graphics.life, 0, graphics.life.height + 3)
    graphics.window.add(graphics.life1, graphics.life.width + 3, 3)
    graphics.window.add(graphics.life2, graphics.life.width + 6 + graphics.life1.width, 3)
    graphics.window.add(graphics.life3, graphics.life.width + 9 + graphics.life1.width * 2, 3)

    # Add animation loop here!

    while True:

        pause(FRAME_RATE)
        dx = graphics.get_dx()
        dy = graphics.get_dy()

        graphics.ball.move(dx, dy)
        # Check wall
        graphics.check_wall()

        # Check four points
        graphics.check_pts()

        # Life cnt
        if graphics.ball.y > graphics.window.height:
            life_cnt -= 1
            graphics.life.text = 'LIVES:'
            graphics.lives = life_cnt
            if life_cnt == 2:
                graphics.window.remove(graphics.life1)
            elif life_cnt == 1:
                graphics.window.remove(graphics.life2)
            elif life_cnt == 0:
                graphics.window.remove(graphics.life3)
            graphics.window.remove(graphics.ball)
            graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                y=(graphics.window.height - graphics.ball.height) / 2)
            dx = 0
            dy = 0
            graphics.set2_dx(dx)
            graphics.set2_dy(dy)

        if life_cnt == 0:
            graphics.window.remove(graphics.ball)
            oh_no = GLabel("NO MORE LIVES! :'( ")
            oh_no.font = 'Helvetica-25-italic'
            graphics.window.add(oh_no, x=(graphics.window.width - oh_no.width) / 2,
                                y=(graphics.window.height - oh_no.height) / 2)
            break

        elif graphics.score_cnt == graphics.brick_rows * graphics.brick_cols:
            graphics.window.remove(graphics.ball)
            oh_no = GLabel("YOU WIN! :D ")
            oh_no.font = 'Helvetica-25-italic'
            graphics.window.add(oh_no, x=(graphics.window.width - oh_no.width) / 2,
                                y=(graphics.window.height - oh_no.height) / 2)
            break


if __name__ == '__main__':
    main()
