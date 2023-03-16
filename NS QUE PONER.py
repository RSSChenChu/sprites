import arcade

WIDTH = 640
HEIGHT = 480
TITLE = "Mi juego"

class Juego(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.WHITE)


class SpriteControlado(arcade.Sprite):
    def actualizar(self, x, y):
        self.center_x = x
        self.center_y = y

class SpritePuntuacion(arcade.Sprite):
    def __init__(self, imagen, escala, x, y):
        super().__init__(imagen, escala)
        self.center_x = x
        self.center_y = y

class SpriteGameOver(arcade.Sprite):
    def __init__(self, imagen, escala, x, y):
        super().__init__(imagen, escala)
        self.center_x = x
        self.center_y = y


def actualizar_sprite_controlado(posicion_raton, sprite_controlado):
    sprite_controlado.actualizar(posicion_raton[0], posicion_raton[1])


def actualizar_sprite_movil(sprite_movil):
    sprite_movil.center_x += 5
    if sprite_movil.center_x > WIDTH:
        sprite_movil.center_x = 0
        sprite_movil.center_y = arcade.random_integers(0, HEIGHT)


