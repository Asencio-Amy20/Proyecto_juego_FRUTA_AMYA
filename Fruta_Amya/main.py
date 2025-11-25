import pygame
from juego import Juego
from menu import Menu

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fruta Manía")

    menu = Menu(pantalla)

    ejecutando = True
    while ejecutando:
        opcion = menu.mostrar()   # Muestra el menú y devuelve la opción

        if opcion == "jugar":
            juego = Juego(pantalla)
            juego.iniciar()

        elif opcion == "records":
            menu.mostrar_records()  # Regresa al menú automáticamente

        elif opcion == "controles":
            menu.mostrar_controles()  # Regresa al menú automáticamente

        elif opcion == "salir":
            ejecutando = False

    pygame.quit()


if __name__ == "__main__":
    main()
