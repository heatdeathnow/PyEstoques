from yaml import safe_dump, safe_load
from os import getenv, mkdir
from os.path import exists, join
import var


def push() -> None:
    """
    Pega todos os dados de todas as linhas e salva num arquivo YAML no diretório do AppData.
    """

    global file_path

    dic = {}
    for i in range(1, len(var.add['contents']) - 1):
        dic[f'{i}'] = [var.owned['contents'][i].value(),
                       var.price['contents'][i].value(),
                       var.item['contents'][i].text(),
                       var.needed['contents'][i].value()]
        
    with open(file_path, 'w') as file:
        file.write(safe_dump(dic))


def pull() -> dict:
    """
    Lê o arquivo do programa no diretório AppData e retorna um dicionário com os dados.
    """

    global file_path
    with open(file_path, 'r') as file:
        return safe_load(file.read())


dir_path = join(getenv('APPDATA'), '_Estoques')
file_path = join(dir_path, 'data.yml')

# Cria o diretório e o arquivo, caso estes não existam.
if not exists(dir_path):
    mkdir(dir_path)
if not exists(file_path):
    with open(file_path, 'x') as file: file.close()
