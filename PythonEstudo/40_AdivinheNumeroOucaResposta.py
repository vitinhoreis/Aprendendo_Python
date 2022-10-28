"""Adivinhe o número e ouça se acertou ou errou"""

import random
import playsound
ne = int(input('Tente descobrir qual número eu escolhi de 0 a 5: '))
n1 = random.randint(0, 5)
if ne == n1:
    playsound.playsound(u'C:/Developer/Projetos/Aprendendo_Python/CursoemVideo/AcertoMizeravi.mp3')
    print(f'Você acertou! O número ecolhido foi {n1}')
else:
    playsound.playsound(u'C:/Developer/Projetos/Aprendendo_Python/CursoemVideo/ErrouFaustao.mp3')
    print(f'O número escolhido foi {n1}. Tente novamente')