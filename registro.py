"""Registro de fotos de aula, revisão (Estudos > Matéria > Data) e estatísticas."""
from datetime import datetime

from config import (FORMATO_DATA, MATERIAS_VALIDAS, NOMES_TIPOS,
                    PASTA_ARQUIVO_VIRTUAL, TIPOS_MARCACAO)
from dicionario import buscar_termo, cadastrar_termo, nome_da_materia
from utils import ler_data, ler_inteiro, ler_opcao, ler_sim_nao, ler_texto_nao_vazio


def caminho_de_arquivo(materia, data):
    """Monta o caminho virtual onde a foto é arquivada: Estudo_Importante/Matéria/Data."""
    return f"{PASTA_ARQUIVO_VIRTUAL}/{nome_da_materia(materia)}/{data.replace('/', '-')}"


def ler_tipo_marcacao():
    """Mostra os tipos de marcação reconhecidos e devolve o tipo escolhido."""
    for numero, tipo in enumerate(TIPOS_MARCACAO, start=1):
        print(f"      {numero} - {NOMES_TIPOS[tipo]}")
    escolha = ler_inteiro("      Tipo de marcação detectada: ", minimo=1, maximo=len(TIPOS_MARCACAO))
    return TIPOS_MARCACAO[escolha - 1]


def exibir_card_dicionario(foto, dicionario_termos):
    """Mostra o card 'Dicionário da aula' com cada termo marcado e seu significado."""
    marcacoes = foto["marcacoes"]
    print("\n--- DICIONÁRIO DA AULA ---")
    print(f"{nome_da_materia(foto['materia'])} | {foto['data']} | {len(marcacoes)} termo(s) detectado(s)")
    if not marcacoes:
        print("  (nenhuma marcação nessa foto)")
    for marcacao in marcacoes:
        entrada = buscar_termo(dicionario_termos, marcacao["termo"], foto["materia"])
        definicao = entrada["definicao"] if entrada else "definição não encontrada"
        print(f"  [{NOMES_TIPOS.get(marcacao['tipo'], marcacao['tipo'])}] {marcacao['termo']}: {definicao}")


def registrar_foto(dicionario_termos):
    """Simula a Lens IA: devolve o registro da foto arquivada ou None se não for um quadro de aula."""
    print("\n=== REGISTRAR FOTO DE AULA ===")
    if not ler_sim_nao("A câmera detectou um quadro de aula? (s/n): "):
        print(f"Foto comum: fica na galeria e não é arquivada em {PASTA_ARQUIVO_VIRTUAL}.")
        return None

    materia = ler_opcao(f"Matéria ({'/'.join(MATERIAS_VALIDAS)}): ", MATERIAS_VALIDAS)
    data = ler_data("Data da aula (DD/MM/AAAA): ")
    qtd_marcacoes = ler_inteiro("Quantas marcações a IA detectou no quadro? ", minimo=0)

    marcacoes = []
    for i in range(qtd_marcacoes):
        print(f"  Marcação {i + 1}")
        termo = ler_texto_nao_vazio("    Termo destacado pelo professor: ").lower()
        tipo = ler_tipo_marcacao()

        # Regra de negócio: o significado depende da matéria da foto. Se o termo já existe
        # nessa matéria, usa o dicionário; senão, a IA sugere (API) e o usuário confirma.
        if buscar_termo(dicionario_termos, termo, materia):
            print("    Termo já está no dicionário contextual.")
        else:
            cadastrar_termo(dicionario_termos, termo, materia)
            print("    Termo cadastrado no dicionário contextual.")

        marcacoes.append({"termo": termo, "tipo": tipo})

    foto = {"materia": materia, "data": data, "marcacoes": marcacoes}
    print(f"\nFoto arquivada automaticamente em {caminho_de_arquivo(materia, data)}.")
    exibir_card_dicionario(foto, dicionario_termos)
    return foto


def chave_de_data(foto):
    """Converte a data da foto em datetime para ordenação. Datas inválidas vão para o fim."""
    try:
        return datetime.strptime(foto["data"], FORMATO_DATA)
    except (ValueError, KeyError):
        return datetime.min


def revisar_estudos(fotos_registradas, dicionario_termos):
    """Navegação Estudos > Matéria > Data: escolhe a aula e mostra o card com os significados."""
    print("\n=== REVISAR ESTUDOS ===")
    materia = ler_opcao(f"Matéria ({'/'.join(MATERIAS_VALIDAS)}): ", MATERIAS_VALIDAS)

    fotos_da_materia = [foto for foto in fotos_registradas if foto["materia"] == materia]
    if not fotos_da_materia:
        print("Nenhuma foto arquivada nessa matéria ainda.")
        return

    fotos_ordenadas = sorted(fotos_da_materia, key=chave_de_data, reverse=True)
    print(f"\nAulas de {nome_da_materia(materia)} (mais recentes primeiro):")
    for numero, foto in enumerate(fotos_ordenadas, start=1):
        print(f"  {numero} - {foto['data']} ({len(foto['marcacoes'])} marcação(ões))")

    escolha = ler_inteiro("Escolha a aula pelo número: ", minimo=1, maximo=len(fotos_ordenadas))
    exibir_card_dicionario(fotos_ordenadas[escolha - 1], dicionario_termos)


def calcular_estatisticas(fotos_registradas):
    """Calcula, por matéria, quantas fotos e quantas marcações foram registradas."""
    estatisticas = {}
    for foto in fotos_registradas:
        resumo = estatisticas.setdefault(foto["materia"], {"fotos": 0, "marcacoes": 0})
        resumo["fotos"] += 1
        resumo["marcacoes"] += len(foto["marcacoes"])
    return estatisticas


def exibir_estatisticas(estatisticas):
    """Mostra quantas fotos e marcações já foram registradas em cada matéria."""
    print("\n=== ESTATÍSTICAS POR MATÉRIA ===")
    if not estatisticas:
        print("Nenhuma foto registrada ainda.")
        return

    for materia, resumo in estatisticas.items():
        print(f"{nome_da_materia(materia)}: {resumo['fotos']} foto(s), {resumo['marcacoes']} marcação(ões)")

    total_fotos = sum(resumo["fotos"] for resumo in estatisticas.values())
    total_marcacoes = sum(resumo["marcacoes"] for resumo in estatisticas.values())
    print(f"TOTAL: {total_fotos} foto(s), {total_marcacoes} marcação(ões)")