"""
This is my first time using python to draw a picture. I hope,I can whisper more instructions to my computer using python in the near future.
"""

#Life is what happens when you're busy making other plans.

import arcade

arcade.open_window(800, 800, "Drawing Example")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 799, 350, 0, arcade.csscolor.LIGHT_GREEN)

arcade.draw_rectangle_filled(90, 265, 120, 150, arcade.csscolor.GRAY)
arcade.draw_triangle_filled(90, 490, 30, 340, 150, 340, arcade.csscolor.DARK_GRAY)
arcade.draw_rectangle_filled(240, 265, 120, 150, arcade.csscolor.GREY)
arcade.draw_triangle_filled(240, 490, 180, 340, 300, 340, arcade.csscolor.DARK_GRAY)

arcade.draw_rectangle_filled(60,300,40,40, arcade.csscolor.LIGHT_GREY)
arcade.draw_rectangle_filled(120,300,40,40, arcade.csscolor.LIGHT_GREY)
arcade.draw_rectangle_filled(210,300,40,40, arcade.csscolor.LIGHT_GREY)
arcade.draw_rectangle_filled(270,300,40,40,arcade.csscolor.LIGHT_GREY)

arcade.draw_circle_filled(700, 650, 40, arcade.color.YELLOW,)

arcade.draw_line(700,650,620,650,arcade.csscolor.YELLOW,3)
arcade.draw_line(700,650,780,650,arcade.csscolor.YELLOW,3)
arcade.draw_line(700,650,700,570,arcade.csscolor.YELLOW,3)
arcade.draw_line(700,650,700,730,arcade.csscolor.YELLOW,3)

arcade.draw_circle_filled(100, 700, 30, arcade.color.WHITE)
arcade.draw_circle_filled(150, 700, 30, arcade.color.WHITE)
arcade.draw_circle_filled(200, 700, 30, arcade.color.WHITE)

arcade.draw_circle_filled(250, 650, 30, arcade.color.WHITE)
arcade.draw_circle_filled(300, 650, 30, arcade.color.WHITE)
arcade.draw_circle_filled(350, 650, 30, arcade.color.WHITE)

arcade.draw_rectangle_filled(470, 250, 30, 120, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(470, 370, 440, 250, 500, 250, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(550, 250, 30, 120, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(550, 370, 520, 250, 580, 250, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(630, 250, 30, 120, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(630, 370, 600, 250, 660, 250, arcade.csscolor.DARK_GREEN)

arcade.draw_arc_outline(500, 750, 20, 20, arcade.csscolor.BLACK, 0, 140, 3)
arcade.draw_arc_outline(520, 750, 20, 20, arcade.csscolor.BLACK, 40, 180, 3)

arcade.draw_arc_outline(550, 720, 20, 20, arcade.csscolor.BLACK, 0, 140, 3)
arcade.draw_arc_outline(570, 720, 20, 20, arcade.csscolor.BLACK, 40, 180, 3)

arcade.draw_arc_outline(600, 750, 20, 20, arcade.csscolor.BLACK, 0, 140, 3)
arcade.draw_arc_outline(620, 750, 20, 20, arcade.csscolor.BLACK, 40, 180, 3)

arcade.draw_text('#11.11',700,50,arcade.csscolor.BLACK,20)

arcade.finish_render()

arcade.run()