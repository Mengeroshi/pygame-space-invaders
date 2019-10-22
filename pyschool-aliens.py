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
            #Loop que observa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #llama la nave
            self.nave.blitme()

            #Refresca la pantalla
            pygame.display.flip()

if __name__ == '__main__':
    juego_shidori = Pyschool()
    juego_shidori.run_game()

        