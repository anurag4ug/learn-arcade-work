import arcade


screen_width = 800
screen_height = 800

def draw_moon(x,y):

    """Draw a moon"""

    # Using two circles to make a crescent moon
    arcade.draw_circle_filled(x, y, 45, arcade.csscolor.GREY)
    arcade.draw_circle_filled(x+15, y+10, 35, arcade.csscolor.BLUE)

def draw_ground():

    """Draw a ground"""

    arcade.draw_lrtb_rectangle_filled(0,799,400,0,arcade.csscolor.LIGHT_GREEN)

def draw_road():

    """Draw a road"""

    arcade.draw_lrtb_rectangle_filled(0,799,150,50,arcade.csscolor.BLACK)

    arcade.draw_lrtb_rectangle_filled(0,799,105,95,arcade.csscolor.YELLOW)

def draw_star(x,y):

    """Draw a Star"""

    # Draw Lines
    arcade.draw_line(x-5, y, x+5, y, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_line(x, y-5, x, y+5, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_line(x - 5, y - 4, x + 5, y + 4, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_line(x-5, y+4,x+5,y-4, arcade.csscolor.WHITE_SMOKE)

def draw_trees(x,y):

    """Draw a tree"""

    arcade.draw_rectangle_filled(x, y, 30, 120, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(x, y+120, x-30, y, x+30, y, arcade.csscolor.DARK_GREEN)

def draw_house(x,y):

    """Draw a House"""

    # Draw building
    arcade.draw_rectangle_filled(x, y, 120, 150, arcade.csscolor.OLIVE)

    # Draw Roof
    arcade.draw_triangle_filled(x, y+225, x-60, y+75, x+60, y+75, arcade.csscolor.LIGHT_YELLOW)

    # Draw Windows
    arcade.draw_rectangle_filled(x-30, y+35, 40, 40, arcade.csscolor.LIGHT_GREY)
    arcade.draw_rectangle_filled(x+30, y+35, 40, 40, arcade.csscolor.LIGHT_GREY)



def main():
    arcade.open_window(screen_width, screen_height, 'Assignment for lab 3')
    arcade.set_background_color(arcade.color.BLUE)
    arcade.start_render()
    draw_moon(700, 700)
    draw_ground()
    draw_road()
    draw_star(200, 700)
    draw_star(400, 650)
    draw_star(250, 640)
    draw_star(300, 690)
    draw_star(80, 640)
    draw_star(270, 680)
    draw_star(620, 700)
    draw_star(500, 720)
    draw_star(40, 720)
    draw_star(400, 700)
    draw_trees(320, 360)
    draw_trees(380,250)
    draw_trees(600,350)
    draw_trees(450,300)
    draw_trees(550,260)
    draw_house(90, 265)
    draw_house(240, 265)
    draw_house(720,265)



    arcade.finish_render()
    arcade.run()

main()