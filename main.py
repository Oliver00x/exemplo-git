from cadastros import salvarcadastro, vercadastros
import json


comando = "0"
while comando != "3":
    comando = int(input(""" 
1. Novo cadastro
2. Ver cadastrados 
3. Sair

Digite o número referente a opção desejada: """))

    if comando == 1:
        nome = input(str("Nome: ")).lower().strip()
        idade = input("Idade: ").strip()
        email = input("E-mail: ").strip()
        telefone = input("Telefone: ").strip()

        cadastro= {
            "Cadastro":{
                "Nome": nome,
                "Idade": idade,
                "E-mail": email,
                "Telefone": telefone
            }
        }
        salvarcadastro(cadastro)
    
    #if comando == 2: 
       # resultado = vercadastros()
       #EM PROGRESSO =)
