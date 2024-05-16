
import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.3
SPRITE_SCALING_BOMB = 0.3
COIN_COUNT = 40
BOMB_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Lab 8"


class Coin(arcade.Sprite):

    # This class represents the coins on our screen.
    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1
        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class Bomb(arcade.Sprite):

    # This class represents the bombs on our screen.

    def reset_pos(self):
        # Reset the bomb to a random spot below the screen
        self.center_y = random.randrange(SCREEN_HEIGHT - 820, SCREEN_HEIGHT - 720)
        self.center_x = random.randrange(SCREEN_WIDTH - 1400, SCREEN_WIDTH - 400)

    def update(self):
        # Move the bomb
        self.center_y += 1
        self.center_x += 1
        # See if the bomb has gone off the top of the screen.
        # If so, reset it.
        if self.bottom > SCREEN_HEIGHT or self.left > SCREEN_WIDTH:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_sprite_list = None
        self.coin_sprite_list = None
        self.bomb_sprite_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.coin_sound = arcade.load_sound(":resources:sounds/coin2.wav")
        self.bomb_sound = arcade.load_sound(":resources:sounds/error1.wav")

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.HOT_PINK)

        # Flag to track game over
        self.game_over = False

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.coin_sprite_list = arcade.SpriteList()
        self.bomb_sprite_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/robot/robot_fall.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_sprite_list.append(coin)

        # Create the bombs
        for i in range(BOMB_COUNT):
            bomb = Bomb(":resources:images/tiles/bomb.png", SPRITE_SCALING_BOMB)
            bomb.center_x = random.randrange(SCREEN_WIDTH)
            bomb.center_y = random.randrange(SCREEN_HEIGHT)
            self.bomb_sprite_list.append(bomb)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.coin_sprite_list.draw()
        self.bomb_sprite_list.draw()
        self.player_sprite_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.LIGHT_GRAY, font_size=40, anchor_x="center")

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """
        if not self.game_over:
            self.coin_sprite_list.update()
            self.bomb_sprite_list.update()

            coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_sprite_list)

            # Loop through each colliding coin, remove it, and add to the score.
            for coin in coin_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.coin_sound)

            bomb_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bomb_sprite_list)

            for bomb in bomb_hit_list:
                bomb.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(self.bomb_sound)

            # Check if all coins are collected
            if len(self.coin_sprite_list) == 0:
                self.game_over = True


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()