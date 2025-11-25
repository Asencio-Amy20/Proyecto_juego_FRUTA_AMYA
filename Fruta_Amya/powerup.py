import pygame
import random

class PowerUp:
    def __init__(self):
        self.x = random.randint(50, 740)
        self.y = random.randint(50, 540)
        
        tipo_random = random.randint(1, 100)
        
        if tipo_random <= 30:  
            self.tipo = "velocidad"
            self.color = (255, 255, 0)  
            self.simbolo = "⚡"
        elif tipo_random <= 55:  
            self.tipo = "escudo"
            self.color = (0, 191, 255)  
            self.simbolo = "🛡"
        elif tipo_random <= 75:  
            self.tipo = "tiempo_lento"
            self.color = (147, 112, 219) 
            self.simbolo = "⏰"
        elif tipo_random <= 90:  
            self.tipo = "fruta_dorada"
            self.color = (255, 215, 0) 
            self.simbolo = "💎"
        else:  
            self.tipo = "bomba"
            self.color = (255, 69, 0)  
            self.simbolo = "💣"
        
        self.tamano = 35
        self.tiempo_vida = 300  
    
    def actualizar(self):
        """Actualiza el power-up (cuenta regresiva para desaparecer)"""
        self.tiempo_vida -= 1
        
        if self.tiempo_vida < 60:
            return self.tiempo_vida % 10 < 5
        return True
    
    def dibujar(self, pantalla):
        """Dibuja el power-up en la pantalla"""
        if self.actualizar():
            # Dibujar círculo con el color del power-up
            pygame.draw.circle(pantalla, self.color, (int(self.x), int(self.y)), self.tamano)
           
            pygame.draw.circle(pantalla, (255, 255, 255), (int(self.x), int(self.y)), self.tamano, 3)
            
            # Dibujar símbolo en el centro
            fuente = pygame.font.Font(None, 30)
            texto = fuente.render(self.simbolo, True, (0, 0, 0))
            rect_texto = texto.get_rect(center=(int(self.x), int(self.y)))
            pantalla.blit(texto, rect_texto)
    
    def esta_vivo(self):
        """Verifica si el power-up aún debe estar en el juego"""
        return self.tiempo_vida > 0


