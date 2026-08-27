def ler_opcao(mensagem, opcoes_validas):
    """Lê um texto do usuário e valida contra uma lista de opções."""
    while True:
        valor = input(mensagem).strip().lower()
        if valor in opcoes_validas:
            return valor
        print(f"Opção inválida. Escolha uma dessas: {', '.join(opcoes_validas)}")


def ler_inteiro(mensagem, minimo=0):
    """Lê um número inteiro do usuário, validando o formato e o valor mínimo."""
    while True:
        texto = input(mensagem).strip()
        if texto.isdigit() and int(texto) >= minimo:
            return int(texto)
        print(f"Digite um número inteiro válido, maior ou igual a {minimo}.")


def ler_texto_nao_vazio(mensagem):
    """Lê um texto do usuário garantindo que ele não fique em branco."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Esse campo não pode ficar vazio, tente novamente.")