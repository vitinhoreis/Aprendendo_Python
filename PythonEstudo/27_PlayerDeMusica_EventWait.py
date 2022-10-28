"""Player de música com pausa através da digitação de qualquer tecla"""

import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()