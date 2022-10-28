"""Classificando o caracter digitado"""

n = input('Digite algo: ')
print(type(n))
print('O caracter digitado é "Numérico": ', n.isnumeric())
print('O caracter digitado é "Alfabético": ', n.isalpha())
print('O caracter digitado é "Decimal": ', n.isdecimal())
print('O caracter digitado é "Espaço": ', n.isspace())
print('O caracter digitado é "Digito": ', n.isdigit())
print('O caracter digitado é "Alfanumérico": ', n.isalnum())
