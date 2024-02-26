import arcade

screen_width = 800
screen_height = 800

def draw_ground():
    #draw a ground
    arcade.draw_lrtb_rectangle_filled(0,799,420,0,arcade.csscolor.GRAY)












def main():
    arcade.open_window(screen_width, screen_height, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_ground()





    arcade.finish_render()
    arcade.run()

main()