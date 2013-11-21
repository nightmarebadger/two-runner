import pyglet

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

mario = pyglet.resource.image("mario.jpg")
