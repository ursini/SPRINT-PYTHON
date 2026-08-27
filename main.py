"""
Projeto: VisionForge | JOVI | Lens IA
Sprint 3 - Computational Thinking with Python

A Lens IA é uma funcionalidade de câmera que reconhece marcações feitas
pelo professor no quadro (círculos, sublinhados, asteriscos), identifica
os termos importantes, exibe um dicionário contextual (o significado de
uma palavra muda de acordo com a matéria) e arquiva a foto automaticamente
por matéria, para facilitar a revisão antes da prova.

Funcionalidades do menu:
    1 - Registrar Foto de Aula
    2 - Consultar Dicionário de Termos
    3 - Revisar Estudos por Matéria
    4 - Ver Estatísticas por Matéria
    5 - Sair

Integrantes:
    Gustavo Braga - RM 569211 | Henry Gabriel - RM 570063
    Leonardo Ursini - RM 569812 | Matheus Carvalho - RM 569454
    Nicholas Belo - RM 57106
"""

from dicionario import criar_dicionario_inicial, consultar_dicionario
from registro import (
    registrar_foto,
    revisar_estudos,
    atualizar_estatisticas,
    exibir_estatisticas,
)
from menu import exibir_menu


def main():
    """Controla o menu principal e direciona para cada funcionalidade."""
    dicionario_termos = criar_dicionario_inicial()
    fotos_registradas = []
    estatisticas = {}
    executando = True

    while executando:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                nova_foto = registrar_foto(dicionario_termos)
                fotos_registradas.append(nova_foto)
                estatisticas = atualizar_estatisticas(estatisticas, nova_foto["materia"])
            case "2":
                consultar_dicionario(dicionario_termos)
            case "3":
                revisar_estudos(fotos_registradas)
            case "4":
                exibir_estatisticas(estatisticas)
            case "5":
                print("Encerrando o programa. Bons estudos!")
                executando = False
            case _:
                print("Opção inválida, escolha um número de 1 a 5.")


if __name__ == "__main__":
    main()