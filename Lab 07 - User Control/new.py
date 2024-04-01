import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ball:
    def __init__(self, position_x, position_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):

        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.ball = Ball(50, 50, 30, arcade.color.CREAM)

        self.set_mouse_visible(False)

    def on_mouse_motion(self, x, y, dx, dy):

        self.ball.position_x = x
        self.ball.position_y = y

    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrtb_rectangle_filled(0, 799, 599, 0, arcade.csscolor.LIGHT_BLUE)

        arcade.draw_lrtb_rectangle_filled(0, 799, 250, 0, arcade.csscolor.LIGHT_GREEN)

        # Trees

        arcade.draw_rectangle_filled(470, 250, 30, 120, arcade.csscolor.SIENNA)
        arcade.draw_triangle_filled(470, 370, 440, 250, 500, 250, arcade.csscolor.DARK_GREEN)

        arcade.draw_rectangle_filled(90, 265, 120, 150, arcade.csscolor.GRAY)
        arcade.draw_triangle_filled(90, 490, 30, 340, 150, 340, arcade.csscolor.DARK_GRAY)
        arcade.draw_rectangle_filled(240, 265, 120, 150, arcade.csscolor.GREY)
        arcade.draw_triangle_filled(240, 490, 180, 340, 300, 340, arcade.csscolor.DARK_GRAY)

        arcade.draw_rectangle_filled(60, 300, 40, 40, arcade.csscolor.LIGHT_GREY)
        arcade.draw_rectangle_filled(120, 300, 40, 40, arcade.csscolor.LIGHT_GREY)
        arcade.draw_rectangle_filled(210, 300, 40, 40, arcade.csscolor.LIGHT_GREY)
        arcade.draw_rectangle_filled(270, 300, 40, 40, arcade.csscolor.LIGHT_GREY)

        arcade.draw_circle_filled(100, 550, 30, arcade.color.WHITE)
        arcade.draw_circle_filled(150, 550, 30, arcade.color.WHITE)
        arcade.draw_circle_filled(200, 550, 30, arcade.color.WHITE)

        # Birds using arcs
        arcade.draw_arc_outline(450, 575, 20, 20, arcade.csscolor.BLACK, 0, 180, 3)
        arcade.draw_arc_outline(470, 575, 20, 20, arcade.csscolor.BLACK, 0, 180, 3)

        arcade.draw_arc_outline(500, 550, 20, 20, arcade.csscolor.BLACK, 0, 180, 3)
        arcade.draw_arc_outline(520, 550, 20, 20, arcade.csscolor.BLACK, 0, 180, 3)

        self.ball.draw()

        arcade.finish_render()


def main():
    window = MyGame()
    arcade.run()


main()
