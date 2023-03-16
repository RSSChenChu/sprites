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


def detectar_colisiones(sprite_controlado, sprite_puntuacion, sprite_game_over, puntos):
    if arcade.check_for_collision(sprite_controlado, sprite_puntuacion):
        sprite_puntuacion.kill()
        puntos += 1
    if arcade.check_for_collision(sprite_controlado, sprite_game_over):
        arcade.close_window()
        print("GAME OVER")
    return puntos


def dibujar_sprites(sprite_controlado, sprite_puntuacion, sprite_game_over):
    sprite_controlado.draw()
    sprite_puntuacion.draw()
    sprite_game_over.draw()


def main():
    juego = Juego()
    sprite_controlado = SpriteControlado("sprite_controlado.png", 0.5)
    sprite_controlado.position = (WIDTH // 2, HEIGHT // 2)
    sprite_puntuacion = SpritePuntuacion("sprite_puntuacion.png", 0.5, 100, 100)
    sprite_game_over = SpriteGameOver("sprite_game_over.png", 0.5, WIDTH // 2, HEIGHT // 2)
    puntos = 0

    @juego.event
    def on_draw():
        arcade.start_render()
        dibujar_sprites(sprite_controlado, sprite_puntuacion, sprite_game_over)

    @juego.event
    def on_mouse_motion(x, y, dx, dy
