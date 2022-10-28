"""Usando a biblioteca 'pygame' para tocar uma música"""

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Agora você escuta?')