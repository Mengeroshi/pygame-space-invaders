import pygame

from pygame.sprite import Sprite

class Bala(Sprite):
    def __init__(self, space_invaders):
        """ Crea una bala """
        super().__init__()
        self.pantalla = space_invaders.pantalla
        self.conf = space_invaders.conf
        self.color = self.conf.bala_color

        #Creacion de un rectangulo
        self.rect = pygame.Rect(0,0, self.conf.bala_ancho, self.conf.bala_alto)
        self.rect.midtop = space_invaders.nave.rect.midtop

        self.y = float(self.rect.y)
    
    def update(self):
        """ Mueve la bala en la pantalla """
        self.y -= self.conf.bala_speed
        self.rect.y = self.y
    
    def dibujar(self):
        """ Dibuja una bala en la pantalla """
        pygame.draw.rect(self.pantalla, self.color, self.rect)