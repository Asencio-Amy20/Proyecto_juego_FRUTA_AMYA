import pygame
from jugador import Jugador
from fruta import Fruta
from obstaculo import Obstaculo

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("FrutaManía 🍎")
        self.reloj = pygame.time.Clock()
        self.jugador = Jugador(400, 300)
        self.fruta = Fruta()
        self.obstaculo = Obstaculo()
        self.puntaje = 0
        self.ejecutando = True

    def checar_colisiones(self):
        jugador_rect = pygame.Rect(self.jugador.x, self.jugador.y, 60, 60)
        fruta_rect = pygame.Rect(self.fruta.x, self.fruta.y, 40, 40)
        obstaculo_rect = pygame.Rect(self.obstaculo.x, self.obstaculo.y, 70, 70)

        if jugador_rect.colliderect(fruta_rect):
            self.puntaje += 1
            self.fruta = Fruta()  # Nueva fruta

        if jugador_rect.colliderect(obstaculo_rect):
            self.ejecutando = False

    def iniciar(self):
        fuente = pygame.font.Font(None, 36)

        while self.ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.ejecutando = False

            teclas = pygame.key.get_pressed()
            self.jugador.mover(teclas)
            self.checar_colisiones()
            self.obstaculo.seguir_jugador(self.jugador.x, self.jugador.y)


            # Fondo verde claro
            self.pantalla.fill((200, 255, 200))

            self.fruta.dibujar(self.pantalla)
            self.obstaculo.dibujar(self.pantalla)
            self.jugador.dibujar(self.pantalla)

            texto = fuente.render(f"Puntaje: {self.puntaje}", True, (0, 0, 0))
            self.pantalla.blit(texto, (10, 10))

            pygame.display.update()
            self.reloj.tick(30)

        pygame.quit()
