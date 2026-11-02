"""Funções de leitura e validação de entradas do usuário."""
from datetime import datetime

from config import FORMATO_DATA


def ler_opcao(mensagem, opcoes_validas):
    """Lê um texto do usuário e valida contra uma lista de opções."""
    while True:
        valor = input(mensagem).strip().lower()
        if valor in opcoes_validas:
            return valor
        print(f"Opção inválida. Escolha uma dessas: {', '.join(opcoes_validas)}")


def ler_inteiro(mensagem, minimo=0, maximo=None):
    """Lê um número inteiro do usuário, validando o formato e os limites (mínimo e máximo)."""
    while True:
        texto = input(mensagem).strip()
        try:
            numero = int(texto)
        except ValueError:
            print(f"'{texto}' não é um número inteiro. Tente novamente.")
            continue

        if numero < minimo:
            print(f"O número deve ser maior ou igual a {minimo}.")
        elif maximo is not None and numero > maximo:
            print(f"O número deve ser menor ou igual a {maximo}.")
        else:
            return numero


def ler_texto_nao_vazio(mensagem):
    """Lê um texto do usuário garantindo que ele não fique em branco."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Esse campo não pode ficar vazio, tente novamente.")


def ler_data(mensagem):
    """Lê uma data no formato DD/MM/AAAA e devolve o texto já validado."""
    while True:
        texto = input(mensagem).strip()
        try:
            datetime.strptime(texto, FORMATO_DATA)
            return texto
        except ValueError:
            print("Data inválida. Use o formato DD/MM/AAAA (ex: 15/03/2026).")


def ler_sim_nao(mensagem):
    """Lê uma resposta s/n e devolve True para 'sim' e False para 'não'."""
    resposta = ler_opcao(mensagem, ["s", "n"])
    return resposta == "s"