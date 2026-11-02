"""
Projeto: VisionForge | JOVI | Lens IA
Sprint 4 - Computational Thinking with Python

A Lens IA é uma funcionalidade nativa da câmera do celular JOVI que detecta
um quadro de aula, reconhece as marcações feitas pelo professor (círculos,
sublinhados, asteriscos e palavras em maiúsculo), identifica os termos
importantes, exibe o card "Dicionário da aula" (o significado de uma palavra
muda de acordo com a matéria) e arquiva a foto automaticamente em
Estudo_Importante/Matéria, para facilitar a revisão antes da prova.

Novidades da Sprint 4:
    - Persistência dos dados em arquivos JSON (pasta "dados/")
    - Consumo da API externa da Wikipédia para sugerir definições
    - Exportação de dados em JSON para o app web (pasta "exportacao/")
    - Tratamento de exceções com try/except e validação de datas
    - Fluxo da solução: detecção do quadro, tipos de marcação, card do
      dicionário e revisão por Estudos > Matéria > Data

Funcionalidades do menu:
    1 - Registrar Foto de Aula
    2 - Consultar Dicionário de Termos
    3 - Revisar Estudos (Matéria > Data)
    4 - Ver Estatísticas por Matéria
    5 - Exportar Dados para o App Web
    6 - Sair

Integrantes:
    Gustavo Braga - RM 569211 | Henry Gabriel - RM 570063
    Leonardo Ursini - RM 569812 | Matheus Carvalho - RM 569454
    Nicholas Belo - RM 571063
"""

from dicionario import consultar_dicionario, criar_dicionario_inicial
from exportacao import exportar_dados
from menu import exibir_menu
from persistencia import carregar_dados, salvar_dados
from registro import (
    calcular_estatisticas,
    exibir_estatisticas,
    registrar_foto,
    revisar_estudos,
)


def executar_opcao(opcao, dicionario_termos, fotos_registradas):
    """Executa a opção escolhida. Devolve False quando o usuário pede para sair."""
    match opcao:
        case "1":
            nova_foto = registrar_foto(dicionario_termos)
            if nova_foto:
                fotos_registradas.append(nova_foto)
            salvar_dados(dicionario_termos, fotos_registradas)
        case "2":
            consultar_dicionario(dicionario_termos)
            salvar_dados(dicionario_termos, fotos_registradas)
        case "3":
            revisar_estudos(fotos_registradas, dicionario_termos)
        case "4":
            exibir_estatisticas(calcular_estatisticas(fotos_registradas))
        case "5":
            exportar_dados(dicionario_termos, fotos_registradas)
        case "6":
            print("Dados salvos. Encerrando o programa. Bons estudos!")
            return False
        case _:
            print("Opção inválida, escolha um número de 1 a 6.")
    return True


def main():
    """Carrega os dados salvos e controla o menu principal."""
    dicionario_termos, fotos_registradas = carregar_dados(criar_dicionario_inicial())
    executando = True

    while executando:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        executando = executar_opcao(opcao, dicionario_termos, fotos_registradas)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma interrompido pelo usuário. Até a próxima!")