import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 15


class Comet:
    """A class representing a comet controlled by the mouse."""

    def __init__(self, position_x, position_y, color):
        """Initialize the comet."""
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.hit_sound = arcade.load_sound(":resources:sounds/jump2.wav")
        self.trail_particles = []

    def draw(self):
        """Draw the comet."""
        # Draw the comet's core
        arcade.draw_circle_filled(self.position_x, self.position_y, 20, self.color)

        # Draw the comet's trail particles
        for particle in self.trail_particles:
            arcade.draw_circle_filled(particle[0], particle[1], 3, arcade.color.WHITE_SMOKE)

    def update(self, x, y):
        # Add a new trail particle
        self.trail_particles.append((self.position_x, self.position_y))

        # Keep only the last few trail particles
        self.trail_particles = self.trail_particles[-20:]

        if self.position_x < 10:
            arcade.play_sound(self.hit_sound)

        if self.position_x > SCREEN_WIDTH - 10:
            arcade.play_sound(self.hit_sound)

        if self.position_y > SCREEN_HEIGHT - 10:
            arcade.play_sound(self.hit_sound)

        if self.position_y < 10:
            arcade.play_sound(self.hit_sound)


class KeyboardControlledObject:
    """A class representing an object controlled by keyboard input."""

    def __init__(self, position_x, position_y, color):
        """Initialize the object."""
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.change_x = 0
        self.change_y = 0
        self.hit_sound = arcade.load_sound(":resources:sounds/coin1.wav")

    def draw(self):
        arcade.draw_triangle_filled(self.position_x - 30, self.position_y - 30,
                                     self.position_x + 30, self.position_y - 30,
                                     self.position_x, self.position_y - 90,
                                     arcade.csscolor.LIGHT_GREEN)

        arcade.draw_circle_filled(self.position_x, self.position_y, 30, self.color)

    def update(self):
        """Update the position of the object."""
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Ensure object stays within the screen boundaries
        if self.position_x < 30:
            self.position_x = 30
            arcade.play_sound(self.hit_sound)

        elif self.position_x > SCREEN_WIDTH - 30:
            self.position_x = SCREEN_WIDTH - 30
            arcade.play_sound(self.hit_sound)

        if self.position_y < 90:
            self.position_y = 90
            arcade.play_sound(self.hit_sound)
        elif self.position_y > SCREEN_HEIGHT - 30:
            self.position_y = SCREEN_HEIGHT - 30
            arcade.play_sound(self.hit_sound)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.BROWN)
        self.comet = Comet(0, 0, arcade.color.RED)
        self.object = KeyboardControlledObject(50, 50, arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        self.comet.draw()
        self.object.draw()

    def update(self, delta_time):
        self.comet.update(self.comet.position_x, self.comet.position_y)
        self.object.update()

    def on_mouse_motion(self, x, y, dx, dy):
        """Handle mouse motion events."""
        self.comet.position_x = x
        self.comet.position_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.object.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.object.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.object.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.object.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.object.change_x = 0
        elif key in [arcade.key.UP, arcade.key.DOWN]:
            self.object.change_y = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "My Lab 7")
    arcade.run()


main()
