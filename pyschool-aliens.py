import sys
import pygame

from settings import Configurador
from nave import Nave
from bala import Bala

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
        self.balas = pygame.sprite.Group()
    
    def run_game(self):
        """ Corre un loop que correra el juego """
        while True:
            self._check_events()
            self.nave.refrescar()
            self._balas_refrescar()
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
                elif event.key == pygame.K_SPACE:
                    self._disparar()

            #Keyups
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.nave.mover_derecha = False
                elif event.key == pygame.K_LEFT:
                    self.nave.mover_izquierda = False

    def _disparar(self):
        if len(self.balas) < 3:
            nueva_bala = Bala(self)
            self.balas.add(nueva_bala)

    def _balas_refrescar(self):
        self.balas.update()

        for bala in self.balas.copy():
            if bala.rect.bottom <= 0:
                self.balas.remove(bala)

    def _actulizar_pant(self):
        """ Actualiza las imagenes y refresca la pantalla """
        self.pantalla.fill(self.conf.fondo_color)
        #llama la nave
        self.nave.blitme()
        for bala in self.balas.sprites():
            bala.dibujar()
        #Refresca la pantalla
        pygame.display.flip()


if __name__ == '__main__':
    juego_shidori = Pyschool()
    juego_shidori.run_game()