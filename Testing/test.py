import arcade

<<<<<<< Updated upstream
arcade.open_window(800, 800, "Drawing Example")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

# Draw the ground
arcade.draw_lrtb_rectangle_filled(0, 799, 350, 0, arcade.csscolor.LIGHT_GREEN)


arcade.draw_rectangle_filled(90, 265, 120, 150, arcade.csscolor.GRAY)
arcade.draw_triangle_filled(90, 490, 30, 340, 150, 340, arcade.csscolor.DARK_GRAY)
arcade.draw_rectangle_filled(240, 265, 120, 150, arcade.csscolor.GREY)
arcade.draw_triangle_filled(240, 490, 180, 340, 300, 340, arcade.csscolor.DARK_GRAY)

# Draw the sun
arcade.draw_circle_filled(700, 650, 40, arcade.color.YELLOW)

# Draw some clouds
arcade.draw_circle_filled(250, 550, 30, arcade.color.WHITE)
arcade.draw_circle_filled(300, 550, 30, arcade.color.WHITE)
arcade.draw_circle_filled(350, 550, 30, arcade.color.WHITE)

arcade.draw_circle_filled(500, 500, 30, arcade.color.WHITE)
arcade.draw_circle_filled(550, 500, 30, arcade.color.WHITE)
arcade.draw_circle_filled(600, 500, 30, arcade.color.WHITE)

# Draw a tree
arcade.draw_rectangle_filled(550, 250, 20, 80, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(550, 330, 40, arcade.csscolor.DARK_GREEN)

# Draw birds
arcade.draw_arc_outline(400, 500, 20, 20, arcade.color.BLACK, 200, 360, 3)
arcade.draw_arc_outline(420, 500, 20, 20, arcade.color.BLACK, 180, 340, 3)

# Finish rendering
arcade.finish_render()

arcade.run()


=======
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snow_person(150, 140)
    draw_snow_person(450, 180)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()
>>>>>>> Stashed changes
