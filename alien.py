import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, space_invaders):
        """ Crea una bala """
        super().__init__()
        self.pantalla = space_invaders.pantalla

     #carga la imagen y su rectangulo
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
    
    #Pone el alien en la esquina superior izquierda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
