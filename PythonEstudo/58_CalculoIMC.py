''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
    calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    - Abaixo de 18.5   : Abaixo do peso            - 30 até 40    : Obesidade
    - Entre 18.5 e 25 :  Peso ideal                - Acima de 40 : Obesidade mórbida
    - 25 até 30      :  Sobrepeso   '''

print('Vamos calcular seu IMC(Índice de Massa Corporal')

print('-=' * 20)

pe = float(input('Digite seu peso (kg): '))
al = float(input('Digite sua altura (m): '))

print('-=' * 20)

imc = pe / al ** 2

if imc < 18.5:
    print(f'Seu IMC está {imc:.1f}.')
    print('Você está abaixo do peso ideal para sua altura. SE CUIDE!')

elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC está {imc:.1f}.')
    print(f'Parabéns! Você está com o peso ideal para a sua altura.')

elif imc >= 25 and imc < 30:
    print(f'Seu IMC está {imc:.1f}.')
    print('Cuidado, você está com sobrepeso.')

elif imc >= 30 and imc < 40:
    print(f'Seu IMC está {imc:.1f}.')
    print('Atenção! Você está na faixa de obesidade.')

else:
    print(f'Seu IMC está {imc:.1f}.')
    print('Atenção! Você está na faixa de obesidade.')