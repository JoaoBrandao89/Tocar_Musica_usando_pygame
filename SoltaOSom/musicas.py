import pygame
def darplay():
    pygame.init()
    pygame.mixer.music.load("conderosa.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()