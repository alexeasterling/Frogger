import pygame
from object import *

class Obstacle(Object):
    def __init__(self, position, size, image, group, speed):
        super().__init__(position, size, image, group)

        self.speed = speed

    def moveObstacle(self):
        x = self.position[0]
        y = self.position[1]

        x += self.speed # movement speed determined by lane

        if x >= 48 * 15: # if off screen to the right
            x = -48 # move to 1 tile off screeen to the left to flow back in right
        if x <= 48 * -2: # if off screen to the left
            x = 48 * 14 # move to 1 tile off screen to the right to flow back in left

        self.position = (x,y)

    def update(self):
        self.setImage()
        self.moveObstacle()