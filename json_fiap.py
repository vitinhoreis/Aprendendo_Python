# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Manipulação de arquivos e JSON
# %% [markdown]
# ## Revisão de estrutura de dados! :)

# %%
exemplo_de_lista        = [] # mutável
exemplo_de_tupla        = () # imutável
exemplo_de_dicionario   = {} # mutável


# %%
lista_simples_sw = ['Yoda', 'Mace Windu', 'Anakyn Skywalker', 'R2-D2', 'Dex']
tupla_simples_sw = ('Yoda', 'Mace Windu', 'Anakyn Skywalker', 'R2-D2', 'Dex')

# %% [markdown]
# ### Podemos adicionar estruturas dentro de estruturas para atingir objetivos mais complexos

# %%
# Listas dentro de listas
lista_2d_sw = [
    ['Yoda','Mestre Jedi'],
    ['Mace Windu','Mestre Jedi'],
    ['Anakin Skywalker','Cavaleiro Jedi'],
    ['R2-D2','Dróide'],
    ['Dex','Balconista']
]

print(lista_2d_sw[0][1])


# %%
# tuplas dentro de listas
lista_de_tuplas = [
    ('Yoda','Mestre Jedi'),
    ('Mace Windu','Mestre Jedi'),
    ('Anakin Skywalker','Cavaleiro Jedi'),
    ('R2-D2','Dróide'),
    ('Dex','Balconista')
]

print(lista_2d_sw[4][1])

# %% [markdown]
# ### Os dicionários tem uma função muito legal para não depender de ordenação, onde ao invés de buscarmos por posição, buscamos por nome da chave

# %%
dicionario_sw = {
    'Yoda':'Mestre Jedi',
    'Mace Windu':'Mestre Jedi',
    'Anakin Skywalker':'Cavaleiro Jedi',
    'R2-D2':'Dróide',
    'Dex':'Balconista'
}

# não preciso saber qual a posiçao para chamar um item específico 
# e nem iterar para descobrir se ele existe
print(dicionario_sw['R2-D2']) 


# %%
# iterando somente com as chaves
for key in dicionario_sw.keys():
    print(key)


# %%
# iterando somente com os valores
for value in dicionario_sw.values():
    print(value)


# %%
# iterando em ambos, chave e valor
for key, value in dicionario_sw.items():
    print(key, '-', value)

# %% [markdown]
# ## Como manipular dicionários?

# %%
dicionario_mestres_jedi = {}

for key, value in dicionario_sw.items():
    if value == 'Mestre Jedi':
        dicionario_mestres_jedi[key] = value

print(dicionario_mestres_jedi)


# %%
# e para remover uma chave...
print(dicionario_mestres_jedi)
print(dicionario_mestres_jedi.pop('Yoda'))
print(dicionario_mestres_jedi)

# %% [markdown]
# ### Eu tinha dito que nós podemos usar estruturas dentro de estruturas, né?

# %%
# e isso não é diferente com Dicionários!
dicionario_de_atributos = {
    'Yoda':['Pequeno', 'Verde', 'Mestre Jedi'],
    'Mace Windu':['Mestre Jedi', 'Careca', 'Alto'],
    'Anakin Skywalker':['Cavaleiro Jedi', 'Mudou de ideia', 'Agora é Sith'],
    'R2-D2':['Dróide', 'Mecânico', 'Melhor robozin'],
    'Dex':['Balconista', 'Alado']
}

print(dicionario_de_atributos['Yoda'][0])

# %% [markdown]
# #### Ficou um pouco bagunçado, várias coisas sem muito nexo juntas... Como organizar?

# %%
# dicionário de dicionários! :D
dicionario_de_atributos = {
    'Yoda': {
        'Cargo': 'Mestre Jedi',
        'Tags': [            
            'Pequeno',
            'Verde'
        ]
    }, 
    'Mace Windu': {
        'Cargo': 'Mestre Jedi',
        'Tags': [
            'Careca',
            'Alto'
        ]
    },
    'Anakin Skywalker': {
        'Cargo': 'Cavaleiro Jedi',
        'Tags': [ 
            'Mudou de ideia', 
            'Agora é Sith'
        ]
    }, 
    'R2-D2': {
        'Cargo': 'Mecânico',
        'Tags': [
            'Dróide',  
            'Melhor robozin'
        ]
    }, 
    'Dex': {
        'Cargo': 'Balconista',
        'Tags': [
            'Alado'
        ]
    }
}


# %%
print(dicionario_de_atributos['Yoda'])
print(dicionario_de_atributos['Yoda']['Tags'])
print(dicionario_de_atributos['Yoda']['Tags'][0])
print(dicionario_de_atributos['Yoda']['Cargo'])

# %% [markdown]
# ### Bem melhor, né? Mas e se a gente quiser salvar essa estrutura bem organizada para usar em outro lugar?
# %% [markdown]
# ## Manipulação de arquivos! E claro, JSON!

# %%
# é sempre importante garantirmos que um arquivo será aberto para edição (caso exista)
# e ao final do processo, fechado. Podemos usar comando específico para abrir e fechar, ou então...
with open('arquivo.txt', 'a') as arquivo:
    arquivo.write('May the force be with you')

# %% [markdown]
# - 'r' abrir para leitura (modo padrão).
# - 'w' abrir para a escrita, sobrescrevendo o conteúdo.
# - 'x' abrir para a criação de arquivo, gerando uma falha se existir um arquivo de mesmo nome.
# - 'a' abrindo para escrita, anexando o novo conteúdo ao final do conteúdo já existente no arquivo.
# - 'b' abrir em modo binário.
# - 't' abrir em modo de texto (modo padrão).
# - '+' abrir para atualização (escrita e leitura).

# %%
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write(dicionario_de_atributos)

# %% [markdown]
# ### Hmmm... Se não podemos salvar diretamente, vamos precisar iterar em cada objeto e ir escrevendo linha a linha? :(

# %%
# ainda bem que a resposta é não :D
# mas para fazer isso de maneira eficiente vamos precisar utilizar o formato de arquivos JSON
# e consequentemente, um módulo só dele para nos ajudar a manipulá-lo:
import json


# %%
with open('arquivo_json.json', 'w', encoding='utf-8') as arquivo:
    arquivo.write(
        json.dumps(dicionario_de_atributos,
                   indent=4,  # identação para leitura 
                   ensure_ascii=False  # acentuação e outros caracteres   
        ) 
    )

# %% [markdown]
# # s2

# %%
# agora que o arquivo foi salvo, precisamos ler ele novamente:
with open('arquivo_json.json', 'r', encoding='utf-8') as arquivo:
    arquivo_json = json.load(arquivo)
    print(arquivo_json, '\n')
    print(type(arquivo_json))

# %% [markdown]
# ## Assim podemos fazer a leitura de arquivos salvos por outros sistemas e trabalhar como se fossem dicionários aninhados, conforme exploramos no início da aula :)

# %%



