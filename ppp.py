import sys
import random
import pygame as pg


class Asteroid:

    def __init__(self):
        self.image = pg.Surface((200, 50))
        self.image.fill((150, 60, 10))
        self.pos = pg.math.Vector2(random.randrange(1230),
                                   random.randrange(750))
        self.vel = pg.math.Vector2(random.uniform(-5, 5),
                                   random.uniform(-5, 5))
        print(self.vel,self.pos)

    def update(self):
        self.pos += self.vel


class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((700, 800))
        self.clock = pg.time.Clock()
        self.bg_color = pg.Color(20, 20, 20)    
        self.asteroids = [Asteroid() for _ in range(10)]
        self.done = False

    def run(self):
        while not self.done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.done = True

            for asteroid in self.asteroids:
                asteroid.update()

            self.screen.fill(self.bg_color)
            for asteroid in self.asteroids:
                self.screen.blit(asteroid.image, asteroid.pos)

            pg.display.flip()
            self.clock.tick(30)


Game().run()
pg.quit()
sys.exit()