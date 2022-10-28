"""Contando letra e encontrando índice"""

fr = str(input('Digite uma frase: '))
q1 = fr.count('a')
q2 = fr.count('A')
q3 = q1 + q2
print(f'Nessa frase contém {q3} letra(s) "a".')
pa = fr.find('a')
fa = fr.find('A')
pp = [pa, fa]
print(pp)
pu = fr.rfind('a')
print(f'{pu}')