import pygame

class Nave:
    def __init__(self, space_invaders):
        """ Inicializa la nave y su posicion """
        self.pant_game = space_invaders.pantalla
        self.pant_rect = space_invaders.pantalla.get_rect()

        #carga la imagen y su rectangulo
        self.image = pygame.image.load("images/nave.bmp")
        self.rect = self.image.get_rect()

        #Pone la nave enmedio de la parte inferior
        self.rect.midbottom = self.pant_rect.midbottom

        self.x = float(self.rect.x)

        #Booleano de moviemiento
        self.mover_derecha = False
        self.mover_izquierda = False

    def blitme(self):
        """ Dibuja la nave en su actual locacion """
        self.pant_game.blit(self.image, self.rect)
    
    def refrescar(self):
        """ Actuliza el movimiento """
        if self.mover_derecha and self.rect.right < self.pant_rect.right:
            self.x += 1

        elif self.mover_izquierda and self.rect.left > 0 :
            self.x -= 1

        self.rect.x = self.x