''' Crie um programa que leia uma frase qualquer e diga
    se ela é um palíndromo, desconsiderando os espaços.
    Ex:
    APÓS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA '''

frase = str(input('Digite uma frase: ')).strip().upper()

separar = frase.split()
juntar = ''.join(separar)
contrário = juntar[::-1]

print(f'A frase "{frase}" junta fica "{juntar}" e ao contrário fica "{contrário}".')

if juntar == contrário:
    print('A frase é um palíndromo.')

else:
    print('A frase não é um palíndromo.')