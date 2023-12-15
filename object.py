import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, position, size, image_directory, group):
        super().__init__(group)
        self.position = position

        self.position = position
        self.size = size
        self.image_directory = image_directory

    def setImage(self):
        self.image = pygame.image.load(self.image_directory) # load image
        self.image = pygame.transform.scale(self.image, self.size) # set appropriate size
        self.surf = pygame.Surface(self.size).convert_alpha()    # "convert alpha" keeps recognizes transparent pixels
        self.surf.fill((0,0,0,0)) # transparent RGB values so that we don't see any transparent pixels
        self.rect = self.surf.get_rect(topleft = self.position) # creating a rectangle around the sprite so that the top left will be true (0,0) and hitboxes will be more normal
        self.surf.blit(self.image, (0,0)) # draws the object image on top of the surface

    # update for actions on the sprite
    def update(self):
        self.setImage()