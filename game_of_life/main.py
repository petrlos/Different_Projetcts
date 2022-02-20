#Game of Life
from gamefield import GameField
from gol import GoLstep
import pyglet

size = 6

window = pyglet.window.Window(600,400, caption="Game of Life")
label = pyglet.text.Label()

field = GameField(size, True)
label.text = "blah"

@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event #enter closes window
def on_key_press(key_code, modifier):
    if key_code == pyglet.window.key.ENTER:
        window.close()
    if key_code == pyglet.window.key.SPACE:
        field = GoLstep(field, size)


pyglet.app.run()