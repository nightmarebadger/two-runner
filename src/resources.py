import pyglet

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

mario = pyglet.resource.image("mario.jpg")
obstacle = pyglet.resource.image("obstacle.png")
background = pyglet.resource.image("background.jpg")