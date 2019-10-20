import sys
import pygame

class Pyschool:
    """ Clase central donde correra el juego """
    def __init__(self):
        pygame.init()

        #Abre la pantalla
        self.pantalla = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Hola Pyschool")
    
    def run_game(self):
        """ Corre un loop que correra el juego """
        while True:
            #Loop que observa eventos
            for event in  pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Refresca la pantalla
            pygame.display.flip()

if __name__ == '__main__':
    juego_shidori = Pyschool()
    juego_shidori.run_game()

        