import pygame, sys, random
from object import *
from frog import *
from lane import *

# main game
class Game:
    def __init__(self, screen_dimensions, screen_caption, screen_color):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_mode(screen_dimensions, pygame.RESIZABLE)
        pygame.display.set_caption(screen_caption)
        self.screen_color = screen_color
        self.DISPLAY = pygame.display.get_surface()

        # sprite group (stores created sprites and puts them on screen)
        self.object_group = pygame.sprite.Group() # grouping background objects/sprites
        self.car_group = pygame.sprite.Group() # grouping cars
        self.river_group = pygame.sprite.Group() # grouping logs and turtles
        self.frog_group = pygame.sprite.Group() # grouping frog variations

        self.all_groups = [self.object_group, self.car_group, self.river_group, self.frog_group]

        self.river_speeds = {} # river lane speeds dictionary
        self.assetSetup()

    # display and configure assets
    def assetSetup(self):
        Object((0,0), (672,768), "assets/background.png", self.object_group) # background
        
        for x in range(14):
            Object((x*48, 384), (48,48), "assets/grass/purple.png", self.object_group) # purple grass dividing river and road
            Object((x*48, 672), (48,48), "assets/grass/purple.png", self.object_group) # purple grass stretching along starting row
        for x in range(28):
            Object((x*24, 72), (24, 72), "assets/grass/green.png", self.object_group) # green grass at finish

        # lanes
        speeds = [-1.25, -1, -.75, -.5, -.25, .25, .5, .75, 1, 1.25] # speeds for objects moving across lanes (negatives move left and positives move right)
        random.shuffle(speeds)

        # river lanes
        for y in range(5):
            y_pos = y*48 + 144 # going from top river lane to bottom
            new_lane = Lane((0, y_pos), self.river_group, speeds.pop(), "river") # set up each lane and add a speed from the speed list
            self.river_speeds[y_pos//48] = new_lane.speed # keys for river lane dictionary (3, 4, 5, 6, 7(corresponding rows))

        # street lanes
        for y in range(5):
            y_pos = y*48 + 432 # going from top street lane to bottom
            Lane((0, y_pos), self.car_group, speeds.pop(), "street") # set up each lane and add a speed from the speed list

        self.frog = Frog((336,672), (48,48), "assets/frog/frog_up.png", self.frog_group, [self.car_group, self.river_group], self.river_speeds) # player frog

    # main game loop
    def run(self):
        while True:

            self.clock.tick(60) # frame rate

            self.frog.keyups = []  # store pressed keys        
            for event in pygame.event.get():                
                if event.type == pygame.QUIT:   # close the game when quit
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:  # store pressed keys
                    self.frog.keyups.append(event.key)
            # update sprites
            for group in self.all_groups:
                for sprite in group:
                    sprite.update()            ################ISSUE###########   for loop has weird coloring in VS Code for some reason
                    
                group.draw(self.DISPLAY) # draw updated group on screen
            pygame.display.update()

game = Game((672,768), "Frogger", (0,0,0)) # dimensions = 14x16 tiles with each tile 48x48 pixels
game.run()
