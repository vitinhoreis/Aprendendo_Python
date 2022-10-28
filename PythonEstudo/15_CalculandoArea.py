"""Calculando a área de uma parede"""

n1 = float(input('Largura da parede em metros: '))
n2 = float(input('Altura da parede em metros: '))
n3 = n1*n2
n4 = n3/(2**2)
print(f'A parede tem uma área equivalente à {n3} metros quadrados, e será necessário {n4} L de tinta para pinta-la')
