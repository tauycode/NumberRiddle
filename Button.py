import pygame
from GameInfo import GameInfo

class Button:
    width = 395
    height = 109
    x, y = (GameInfo.width-width)/2, GameInfo.height-3*height
    picPath = "./assets/images/submit.png"
    surface = None
    rect = None

    def __init__(self):
        self.surface = pygame.transform.scale(pygame.image.load(self.picPath), (self.width, self.height))
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


