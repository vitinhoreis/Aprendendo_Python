'''Uma grande empresa de jogos está querendo tornar seus games mais desafiadores. Por isso ela contratou você para
desenvolver um algoritmo que será aplicado futuramente em diversos outros games: o algoritmo da sorte de Fibonnaci.

A ideia dessa empresa, é claro, é fazer com que seja mais difícil os jogadores terem sucesso nas ações que realizam
nos games. Por isso o seu algoritmo deverá funcionar da seguinte forma: o usuário deve digitar um valor numérico
inteiro e o algoritmo deverá verificar se esse valor encontra-se na sequência de Fibonnaci. Caso o número esteja na
sequência, o algoritmo deve exibir a mensagem “Ação bem sucedida!” e, caso não esteja, deve exibir a mensagem “A ação falhou...”.

A sequência de Fibonacci é muito simples e possui uma lógica de fácil compreensão: ela se inicia em 1 e cada novo
elemento da sequência é a soma entre os dois elementos anteriores. Portanto: 1, 1, 2, 3, 5, 8, 13, 21, e assim por diante.

Logo, se o usuário digitar o número 55 o programa deverá informar que a ação foi bem sucedida, afinal 55 está entre
os números da sequência.

Mas se o usuário digitar o número 6, por exemplo, a ação não será bem sucedida, pois o número 6 não está na sequência.'''


print(" = " * 60)

print("Vamos ver se você está com sorte. Que comecem os jogos!")

continuar = str(input("\nEstá pronto para continuar?\nDigite 'S' para continuar ou 'N' para parar:")) #Recebe a intenção do usuário de continuar, ou não.
print("-" * 80)

while continuar not in 'SsNn': #Se a reposta para 'continuar' não estiver entre as opções 'S, s, N, n' a pergunta será feita novamente até se ter uma resposta válida.
    print("Opção inválida. Tente novamente.")
    continuar = str(input("\nEstá pronto para continuar?\nDigite 'S' para continuar ou 'N' para parar:"))
    print("-" * 80)

while continuar in 'Ss': #Executará enquanto a resposta para 'continuar' for 'S, s' (SIM)
    termo1 = 0
    termo2 = 1
    termo3 = 0

    numero_escolhido = int(input("\nDigite um número inteiro (Exemplos: 1, 2, 3 ou 4): ")) #Número escolhido pelo usuário, este será avaliado se está na sequência de Fibonacci.

    while termo3 <= numero_escolhido: #Será executado enquanto o 'termo3' for <= o número escolhido pelo usuário.
        termo3 = termo1 + termo2 #O termo3 vai ser a soma entre os 2 termos anteriores, ou seja, 'termo1' + 'termo2'.
        termo1 = termo2 #A cada loop o 'termo1' receberá o valor que antes estava no 'termo2'.
        termo2 = termo3 #A cada loop o 'termo2' receberá o valor que antes estava no 'termo3'.

    if numero_escolhido == termo1 or numero_escolhido == termo2 or numero_escolhido == termo3: #Executará se o número escolhido pelo jogador em algum momento for = a um dos 3 termos.
        print(f"\nO número {numero_escolhido} está na sequência de Fibonacci.")
        print("\nAção bem sucedida!")
        print("-" * 80)
        continuar = str(input("\nEstá pronto para continuar?\nDigite 'S' para continuar ou 'N' para parar:")) #Recebe a intenção do usuário de continuar, ou não.

        while continuar not in 'SsNn': #Se a reposta para 'continuar' não estiver entre as opções 'S, s, N, n' a pergunta será feita novamente até se ter uma resposta válida.
            print("Opção inválida. Tente novamente.")
            print("-" * 80)
            continuar = str(input("\nEstá pronto para continuar?\nDigite 'S' para continuar ou 'N' para parar:")) #Recebe a intenção do usuário de continuar, ou não.

        print("-" * 80)

    else: #Executará se o número escolhido pelo jogador nunca aparecer entre a sequência de Fibonacci, ou seja, entre os 3 termos.
        print(f"\nO número {numero_escolhido} não está na sequência de Fibonacci.")
        print("\nA ação falhou!")
        print("-" * 80)
        continuar = str(input("\nEstá pronto para continuar?\nDigite 'S' para continuar ou 'N' para parar:")) #Recebe a intenção do usuário de continuar, ou não.

        while continuar not in 'SsNn': #Se a reposta para 'continuar' não estiver entre as opções 'S, s, N, n' a pergunta será feita novamente até se ter uma resposta válida.
            print("Opção inválida. Tente novamente.")
            print("-" * 80)
            continuar = str(input("\nEstá pronto para continuar?\nDigite 'S' para continuar ou 'N' para parar:")) #Recebe a intenção do usuário de continuar, ou não.

        print("-" * 80)

print("Fim de jogo.")
print(" = " * 60)