"""Manipulando String"""

frase = 'Aprendendo Python'
print(len(frase))
print(frase[:14])
print(frase.upper())
print(frase.lower())
print(frase.count('o'))
print(frase.upper().count('O'))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Aprendendo'))
print(frase.split())
print(frase.split()[0])