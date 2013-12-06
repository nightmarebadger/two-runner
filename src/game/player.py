from __future__ import division

from cocos.actions import Move
from pyglet.window import key
import cocos
import cocos.collision_model as cm

import resources

class Player(cocos.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__(resources.mario)
    
        self.position = 25, 25
        self.velocity = 0, 0
        self.speed = 500
        self.gravity = -1300

        self.cshape = cm.AARectShape(self.position, self.width/3, self.height/2)

        self.schedule(self.update)

    def update(self, dt):
        self.cshape.center = self.position
        
        if self.position[1] <= 25:
            self.position = (self.position[0], 25)
            self.velocity = (self.velocity[0], 0)
            self.jumping = False
        if self.position[0] < 25:
           self.position = (25, self.position[1])
        elif self.position[0] > 775:
            self.position = (775, self.position[1])
        else:
            pass