import pygame
import sys
from jugador import Jugador
from fruta import Fruta
from obstaculo import Obstaculo

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego del Pingüino vs Tigre")

clock = pygame.time.Clock()

# Objetos
jugador = Jugador(400, 300)
fruta = Fruta()
enemigo = Obstaculo()  # el tigre

puntos = 0


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    jugador.mover(teclas)

    
    jx, jy = jugador.obtener_pos()
    enemigo.seguir_jugador(jx, jy)

    
    fx, fy = fruta.obtener_pos()
    if abs(jx - fx) < 40 and abs(jy - fy) < 40:
        puntos += 1
        fruta = Fruta()  

   
    pantalla.fill((50, 150, 200))

    
    jugador.dibujar(pantalla)
    fruta.dibujar(pantalla)
    enemigo.dibujar(pantalla)

    
    fuente = pygame.font.SysFont(None, 40)
    texto = fuente.render(f"Puntos: {puntos}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    clock.tick(60)
