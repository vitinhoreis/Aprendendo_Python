''' Faça um programa que leia um número qualquer e mostre o seu fatorial.
    Ex:
    5! = 5x4x3x2x1 = 120 '''

#num = int(input('Digite um número para ver seu fatorial: '))
#n1 = num

#for c in range(num-1, 0, -1):
    #num = num * c
#print(f'O fatorial de {n1} = {num}.')



n = int(input('Informe um número inteiro: '))
p = n
res = 1
string =''
while n >= 1:
    res *= n
    string += str(n) + 'x'
    n -= 1

print(f'{p}! = {string[:len(string)-1]} = {res}')




