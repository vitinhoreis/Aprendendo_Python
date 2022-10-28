''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
    No final, mostre os 10 primeiros termos dessa progressão. '''

pt = int(input('Digite o primeiro termo de uma PA: '))
ra = int(input('Digite a razão dessa PA: '))

for c in range(pt, ra*10+pt, ra):
    print(c, end=', ')