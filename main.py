import pygame

pygame.init()

#Criando uma janela
print('Setup started')
screen = pygame.display.set_mode((800, 600))
window = pygame.display.set_mode(size=(640, 480))
print('Setup finished')

print('Loop started')
while True: #para coneguir deixar a janela aberta
    #Chek for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close Window
            quit() #end_pygame

