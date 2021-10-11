import json


# abertura do arquivo 
with open('arquivo_json.json', 'r') as arquivo:
    # varredura do arquivo
    for key, value in json.load(arquivo).items():
       if value['Cargo'] == 'Cavaleiro Jedi':
           print(key + ' é um ' + value['Cargo'])
           print('Seus atributos são: ' + ', '.join(value['Tags']))
