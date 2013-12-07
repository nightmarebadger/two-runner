from __future__ import division

from cocos.collision_model import AARectShape
from cocos.director import director
from cocos.sprite import Sprite

from game.resources import resources

class Player(Sprite):
    def __init__(
            self,
            position=(25, 25),
            velocity=(0, 0),
            speed=500,
            gravity= -1300,
            *args,
            **kwargs):

        # Push the needed attributes into kwargs
        kwargs['position'] = position

        super(Player, self).__init__(resources.mario, *args, **kwargs)

        self.speed = speed
        self.gravity = gravity
        self.velocity = velocity

        self.cshape = AARectShape(self.position, self.width//3, self.height//2)

        self.schedule(self.update)

    def update(self, dt):
        self.cshape.center = self.position

        win_width, win_height = director.get_window_size()

        xmin = self.width//2
        xmax = win_width - xmin

        ymin = self.height//2

        if self.position[1] <= ymin:
            self.position = (self.position[0], ymin)
            self.velocity = (self.velocity[0], 0)
            self.jumping = False
        if self.position[0] < xmin:
           self.position = (xmin, self.position[1])
        elif self.position[0] > xmax:
            self.position = (xmax, self.position[1])
        else:
            pass
