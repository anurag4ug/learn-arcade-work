"""
Hi, It's my first arcade game programming class. Today we are learning how to draw an image with python.
"""

# Professor Wolff is teaching us how to do that in the clubhouse.

import arcade

arcade.open_window(450, 600, "Lab for February 13,2024")

arcade.set_background_color(arcade.csscolor.MAROON)

arcade.start_render()
# Tree trunk
# Center of 300, 300
# Width of 100
# Height of 100
arcade.draw_rectangle_filled(300, 300, 100, 100, arcade.csscolor.SIENNA)

# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
arcade.finish_render()

arcade.run()