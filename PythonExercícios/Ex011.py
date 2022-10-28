''' Faça um programa que leia a largura e a altura de uma parede em
    metros, calcule a sua área e a quantidade de tinta necessária para
    pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m/². '''

l = float(input('Largura da parede em metros: '))
a = float(input('Altura da parede em metros: '))
ar = l * a
t = ar / 2
print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {ar}m².')
print(f'Para pintar essa parede, você precisará de {t:.2f}(l) de tinta.')
