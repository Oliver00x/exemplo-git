import json


def salvarcadastro(cadastro):
    with open("cadastros.json", "a") as arquivo:
        json.dump(cadastro, arquivo)


def vercadastros():
    resultado = {}
    with open("cadastros.json", "r") as arquivos:
        resultado = json.load(arquivos)
    print(resultado["Nome"])
#Em progresso
    