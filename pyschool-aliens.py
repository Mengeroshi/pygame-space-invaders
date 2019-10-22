import sys
import pygame

from settings import Configurador
from nave import Nave

class Pyschool:
    """ Clase central donde correra el juego """
    def __init__(self):
        pygame.init()
        self.conf = Configurador()

        #Abre la pantalla
        self.pantalla = pygame.display.set_mode(
            (self.conf.ancho_pant, self.conf.largo_pant))
        
        pygame.display.set_caption("Hola Pyschool")

        self.nave = Nave(self)
    
    def run_game(self):
        """ Corre un loop que correra el juego """
        while True:
            self._check_events()
            self.nave.refrescar()
            self._actulizar_pant()

            
    def _check_events(self):
        """ Checa los eventos """
        #Loop que observa eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #keydowns
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.nave.mover_derecha = True
                elif event.key == pygame.K_LEFT:
                    self.nave.mover_izquierda = True

            #Keyups
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.nave.mover_derecha = False
                elif event.key == pygame.K_LEFT:
                    self.nave.mover_izquierda = False

    def _actulizar_pant(self):
        """ Actualiza las imagenes y refresca la pantalla """
        #llama la nave
        self.nave.blitme()
        #Refresca la pantalla
        pygame.display.flip()


if __name__ == '__main__':
    juego_shidori = Pyschool()
    juego_shidori.run_game()