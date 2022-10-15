import pygame
pygame.init()
tela = pygame.display.set_mode((400,400),0,32)
pygame.display.set_caption("tocando musica no pygame")
branco = (255,255,255)
pygame.mixer.music.load('conderosa.mp3')


pygame.mixer.music.play()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False