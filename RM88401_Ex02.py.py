''''Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde as crianças aprendam
a controlar os seus gastos.

Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar
QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das
transações que realizou.

Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação'''

print(" = " * 60)

print("Vamos calcular seus gastos diários!\n")

valor_transacao = 0 #Atribuindo um valor inicial para o valor de uma transação = 0

valor_total = 0 #Atribuindo um valor incical para o total das transações = 0

cont = 1 #Atribuindo o valor inicial da variável responsável por fazer a contagem de loops feitos

continuar = str(input("Deseja continuar os cálculos?\nDigite 'S' para continuar ou 'N' para parar: ")) #Condição para continuar, dependendo da resposta do usuário

while continuar in 'Ss':

    quantidade_transacoes = int(input("\nDigite a quantidade de transações feitas hoje: ")) #Recebe a quantidade de transações

    if quantidade_transacoes <= 0: #Condição para se a resposta da variável 'quantidade_transacoes' for <= 0
        print("\nVocê não fez transações hoje, portanto seus gastos totalizaram R$0,00.")
        print("-" * 80)

    else: #Condição para se a resposta da variável 'quantidade_transacoes' for > 0
        while cont <= quantidade_transacoes: #Loop que será realizado enquanto o contador for <= a quantidade de transações
            valor_transacao = float(input(f"Digite o valor da sua {cont}ª transação: ")) #Recebe o valor de cada transação
            valor_total = valor_total + valor_transacao #Calcula o valor total das transações, adicionando os novos valores
            cont = cont + 1 #Calcula as voltas do loop
        valor_medio = valor_total / quantidade_transacoes #Calcula o valor médio das transações
        print(f"\nForam feitas {quantidade_transacoes} transações hoje, com um um valor total de: R${valor_total:.2f}.")
        print(f"O valor médio entre as transações é de: R${valor_medio:.2f}.")
        print("-" * 80)
    continuar = str(input("Deseja continuar os cálculos?\nDigite 'S' para continuar ou 'N' para parar: ")) #Condição para continuar, dependendo da resposta do usuário

print("FIM!")

print(" = " * 60)