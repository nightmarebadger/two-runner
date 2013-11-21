from __future__ import division
from cocos.actions import Move
from pyglet.window import key
import cocos
import resources

class Game(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        super(Game,self).__init__(255,255,255,255)
        
        self.player = cocos.sprite.Sprite(resources.mario)
        self.player.position = 25, 25
        self.player.velocity = 0, 0
        self.player.speed = 500
        self.player.gravity = -1500
        self.add(self.player, z=0)
        self.player.do(Move())
        self.player.jumping = False

        self.schedule(self.update)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.player.velocity = -self.player.speed/2, self.player.velocity[1]
        elif symbol == key.RIGHT:
            self.player.velocity = self.player.speed/2, self.player.velocity[1]
        elif symbol == key.UP:
            if not self.player.jumping:
                self.player.velocity = self.player.velocity[0], self.player.speed
                self.player.jumping = True
        elif symbol == key.DOWN:
            self.player.velocity = self.player.velocity[0], -self.player.speed
        elif symbol == key.SPACE:
            self.player.velocity = 0, 0

    def on_key_release(self, symbol, modifier):
        if symbol == key.LEFT:
            self.player.velocity = 0, self.player.velocity[1]
        if symbol == key.RIGHT:
            self.player.velocity = 0, self.player.velocity[1]

    def update(self, dt):
        if self.player.position[1] < 25:
            self.player.position = (self.player.position[0], 26)
            self.player.velocity = (self.player.velocity[0], 0)
            self.player.jumping = False
        elif self.player.position[0] < 25:
            self.player.position = (26, self.player.position[1])
        elif self.player.position[0] > 775:
            self.player.position = (775, self.player.position[1])
        
        else:
            pass

        
if __name__ == '__main__':
    cocos.director.director.init(
        width=800,
        height=500)
    
    scene = cocos.scene.Scene()
    scene.add(Game(), z = 0)
    cocos.director.director.run(scene)
    
