'''O projeto HealthTrack está tomando forma e podemos pensar em algoritmos que possam ser reaproveitados quando
   estivermos implementando o front e o back do nosso sistema. Uma das funções mais procuradas por usuários de
   aplicativos de saúde é o de controle de calorias ingeridas em um dia. Por essa razão, você deve elaborar um
   algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu naquele dia e depois possa
   informar o número de calorias de cada um dos alimentos. Como não estudamos listas nesse capítulo você não deve
   se preocupar em armazenar todas as calorias digitadas, mas deve exibir o total de calorias no final.'''

print(" = " * 60)

print("Vamos calcular quantas calorias foram ingeridas hoje!\n")

total_calorias = 0 #Atribuindo um valor inicial ao total de calorias ingeridas

quantidade_refeicoes = int(input("Digite quantas refeições você ingeriu: ")) #Recebendo a quantidade de refeições feitas

for x in range(1, quantidade_refeicoes + 1): #Criando um loop baseado na quantidade de refeições feitas
    calorias = float(input(f"Digite a quantidade de caloria da {x}ª refeição: ")) #Quantidade de caloria por refeição
    total_calorias = total_calorias + calorias #Clculando o total de caloria, somando entre refeições

print(f"\nO total de calorias ingeridas foi de: {total_calorias:.2f} cal.")

print(" = " * 60)