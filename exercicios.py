


def calcula_media(boletim):
    if len(boletim) == 0:
        boletim.append(0.0)
        quantidadenotas = len(boletim)
        soma = sum(boletim)
        media = soma / quantidadenotas
        print(f"Sua média final foi {media:.2f}")
    else:
        quantidadenotas = len(boletim)
        soma = sum(boletim)
        media = soma / quantidadenotas
        print(f"Sua média final foi {media:.2f}")


def mensagem_saudacao(periodo):
    if periodo == "M":
        periodo = "Bom dia"
    elif periodo == "V":
        periodo = "Boa tarde"
    elif periodo == "N":
        periodo = "Boa noite"
    else:
        periodo = "Olá"
    return print(periodo)


def calcula_situacao(nota):
    if nota == 10:
        situacao = "Aprovado com Distinção!"
    elif nota >= 7:
        situacao = "Aprovado!"
    elif nota < 7:
        situacao = "Reprovado!"
    return print(situacao)
