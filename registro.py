from config import MATERIAS_VALIDAS
from dicionario import buscar_termo, cadastrar_termo
from utils import ler_opcao, ler_inteiro, ler_texto_nao_vazio


def registrar_foto(dicionario_termos):
    """Coleta os dados de uma foto de aula e devolve o registro pronto para ser arquivado."""
    print("\n=== REGISTRAR FOTO DE AULA ===")
    materia = ler_opcao(f"Matéria ({'/'.join(MATERIAS_VALIDAS)}): ", MATERIAS_VALIDAS)
    data = ler_texto_nao_vazio("Data da aula (ex: 15/03/2026): ")
    qtd_marcacoes = ler_inteiro("Quantas marcações a IA detectou no quadro? ", minimo=0)

    termos_da_foto = []
    for i in range(qtd_marcacoes):
        termo = ler_texto_nao_vazio(f"  Marcação {i + 1} - termo destacado pelo professor: ").lower()
        entrada = buscar_termo(dicionario_termos, termo, materia)

        # Regra de negócio: se o termo já existe nessa matéria, mostra a definição;
        # senão, simula a IA aprendendo uma definição nova a partir do usuário.
        if entrada:
            print(f"  Dicionário já conhece: {entrada['definicao']}")
        else:
            cadastrar_termo(dicionario_termos, termo, materia)
            print("  Termo cadastrado no dicionário contextual.")

        termos_da_foto.append(termo)

    print(f"Foto arquivada automaticamente em Estudos/{materia}/{data}.")
    return {"materia": materia, "data": data, "termos": termos_da_foto}


def revisar_estudos(fotos_registradas):
    """Lista as fotos já arquivadas de uma matéria escolhida pelo usuário."""
    print("\n=== REVISAR ESTUDOS POR MATÉRIA ===")
    materia = ler_opcao(f"Matéria ({'/'.join(MATERIAS_VALIDAS)}): ", MATERIAS_VALIDAS)

    encontrou_registro = False
    for foto in fotos_registradas:
        if foto["materia"] == materia:
            encontrou_registro = True
            print(f"- {foto['data']}: termos = {foto['termos']}")

    if not encontrou_registro:
        print("Nenhuma foto arquivada nessa matéria ainda.")


def atualizar_estatisticas(estatisticas, materia):
    """Incrementa o contador de fotos daquela matéria e devolve o dicionário atualizado."""
    estatisticas[materia] = estatisticas.get(materia, 0) + 1
    return estatisticas


def exibir_estatisticas(estatisticas):
    """Mostra quantas fotos já foram registradas em cada matéria."""
    print("\n=== ESTATÍSTICAS POR MATÉRIA ===")
    if not estatisticas:
        print("Nenhuma foto registrada ainda.")
        return

    for materia, quantidade in estatisticas.items():
        print(f"{materia}: {quantidade} foto(s)")