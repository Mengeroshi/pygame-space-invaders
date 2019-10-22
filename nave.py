import pygame

class Nave:
    def __init__(self, space_invaders):
        """ Inicializa la nave y su posicion """
        self.pant_game = space_invaders.pantalla
        self.pant_rect = space_invaders.pantalla.get_rect()

        #carga la imagen y su rectangulo
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #Pone la nave enmedio de la parte inferior
        self.rect.midbottom = self.pant_rect.midbottom

    def blitme(self):
        """ Dibuja la nave en su actual locacion """
        self.pant_game.blit(self.image, self.rect)