import random, pygame
from obstacle import *

class Lane:
    def __init__(self, position, group, speed, lane_type):
        self.position = position
        self.group = group
        self.speed = speed
        self.lane_type = lane_type

        self.setupObstacles()

    def setupObstacles(self):
        if self.speed > 0:
            self.direction = "right"
        else:
            self.direction = "left"

        if self.lane_type == "street":
            car = random.randint(1,2) # pick between the 2 car images
            image_directory = f"assets/{self.lane_type}/{self.direction}/{car}.png" # find and set car image

            Obstacle(self.position, (48,48), image_directory, self.group, self.speed).setImage() # car at tile 0
            Obstacle((self.position[0] + 5*48, self.position[1]), (48,48), image_directory, self.group, self.speed).setImage() # another car moved 5 tiles right
            Obstacle((self.position[0] + 10*48, self.position[1]), (48,48), image_directory, self.group, self.speed).setImage() # another car moved 10 tiles right

        elif self.lane_type == "river":
            if self.direction == "left": # turtles
                left, middle, right = f"assets/{self.lane_type}/{self.direction}/turtle.png", f"assets/{self.lane_type}/{self.direction}/turtle.png", f"assets/{self.lane_type}/{self.direction}/turtle.png"
            elif self.direction == "right": # logs
                left, middle, right = f"assets/{self.lane_type}/{self.direction}/short_log.png", f"assets/{self.lane_type}/{self.direction}/short_log.png", f"assets/{self.lane_type}/{self.direction}/short_log.png"
            
            # grouped logs and turtles
            Obstacle(self.position, (48,48), left, self.group, self.speed).setImage() # lane tile 0
            Obstacle((self.position[0] + 48, self.position[1]), (48,48), middle, self.group, self.speed).setImage() # another moved 1 tile right
            Obstacle((self.position[0] + 2*48, self.position[1]), (48,48), right, self.group, self.speed).setImage() # another moved 2 tiles right

            Obstacle((self.position[0] + 7*48, self.position[1]), (48,48), left, self.group, self.speed).setImage() # lane tile 7 (on x-axis) at start
            Obstacle((self.position[0] + 8*48, self.position[1]), (48,48), middle, self.group, self.speed).setImage() # lane tile 8 at start
            Obstacle((self.position[0] + 9*48, self.position[1]), (48,48), right, self.group, self.speed).setImage() # lane tile 9 at start