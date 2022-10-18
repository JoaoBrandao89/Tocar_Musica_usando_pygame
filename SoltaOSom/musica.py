import pygame



def dar_play_em_cond():
    pygame.init()
    pygame.mixer.music.load("conderosa.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()

def dar_play_em_bardo():
    pygame.init()
    pygame.mixer.music.load("oasisbardo.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()

def dar_play_em_sweat():
    pygame.init()
    pygame.mixer.music.load("sweater.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()



