import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_house(x, y):
    """ Draw a simple house """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # House body
    arcade.draw_rectangle_filled(300 + x, 200 + y, 150, 150, arcade.color.BROWN)

    # Roof
    arcade.draw_triangle_filled(225 + x, 350 + y, 375 + x, 350 + y, 300 + x, 450 + y, arcade.color.RED)

    # Door
    arcade.draw_rectangle_filled(300 + x, 130 + y, 30, 60, arcade.color.BROWN)

    # Window
    arcade.draw_rectangle_filled(270 + x, 230 + y, 40, 40, arcade.color.SKY_BLUE)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    draw_house(50, 50)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
