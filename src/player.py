class Player(cocos.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__(resources.mario)
	
        self.position = 25, 25
        self.velocity = 0, 0
        self.speed = 500
        self.gravity = -1300

        self.player.cshape = cm.AARectShape(self.player.position, self.player.width/3, self.player.height/2)

    def on_key_press(self, symbol, modifiers):
        vel = list(self.velocity)
        if symbol == key.LEFT:
            vel[0] -= self.speed/2
        elif symbol == key.RIGHT:
            vel[0] += self.speed/2
        elif symbol == key.UP:
            if not self.jumping:
                vel[1] += self.speed
                self.jumping = True
        elif symbol == key.DOWN:
            vel[1] = -self.speed
        
        self.velocity = tuple(vel)

    def on_key_release(self, symbol, modifier):
        vel = list(self.velocity)
        if symbol == key.LEFT:
            vel[0] += self.speed/2
        elif symbol == key.RIGHT:
            vel[0] -= self.speed/2

        self.velocity = vel

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
        if self.obstacle.position[0] < 0:
            self.obstacle.position = 830, 30