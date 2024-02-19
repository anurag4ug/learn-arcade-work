import arcade

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

