""" Sprite Sample Program """

import random
import arcade
import os

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.34
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_METEOR = 1
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameOver(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.CYAN)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME OVER", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=75, anchor_x="center")

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.meteor_sprite = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SPANISH_SKY_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/enemies/slimeBlock.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(":resources:images/items/star.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        self.meteor_sprite = arcade.Sprite(":resources:/images/space_shooter/meteorGrey_big4.png",
                                               SPRITE_SCALING_METEOR)
        self.meteor_sprite.center_x = random.randrange(SCREEN_WIDTH)
        self.meteor_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        self.coin_list.append(self.meteor_sprite)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


        self.meteor_sprite.center_x += 2.5
        if self.meteor_sprite.right > SCREEN_WIDTH or self.meteor_sprite.left < 0:
            self.meteor_sprite.change_x *= -1
            print('hola')
        if self.meteor_sprite.top > SCREEN_HEIGHT or self.meteor_sprite.bottom < 0:
            self.meteor_sprite.change_y *= -1
            print('Funciona')

        self.meteor_sprite.update()

        if arcade.check_for_collision(self.player_sprite, self.meteor_sprite):
            over_view = GameOver()
            self.window.show_view(over_view)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
