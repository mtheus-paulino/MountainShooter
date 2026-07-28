import Font
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, C_WHITE


class Menu():
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')    #carregar imagem de background
        self.rect = self.surf.get_rect(left=0, top=0 ) #criando um retangulo

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # Com menos 1 toca pra sempre
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # aqui vamos desenhar
            self.menu_text(50, "Mountain",COLOR_ORANGE, ((WIN_WIDTH / 2) , 70))
            self.menu_text(50, "Shooter",COLOR_ORANGE, ((WIN_WIDTH / 2) , 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2) , 180 + 30 * i))

            pygame.display.flip()

            # Chek for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window
                    quit() #end_pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)