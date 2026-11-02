"""Dicionário contextual: o significado de um termo muda de acordo com a matéria."""
from api import buscar_definicao_online
from config import MATERIAS_VALIDAS, NOMES_MATERIAS
from utils import ler_opcao, ler_sim_nao, ler_texto_nao_vazio


def criar_dicionario_inicial():
    """Retorna a lista inicial de termos (usada apenas na primeira execução)."""
    return [
        {"termo": "mitocondria", "materia": "biologia", "definicao": "Organela responsável pela produção de energia (ATP)."},
        {"termo": "ciclo de krebs", "materia": "biologia", "definicao": "Sequência de reações que ocorre na matriz da mitocôndria e libera energia na respiração celular."},
        {"termo": "protocolo", "materia": "redes", "definicao": "Conjunto de regras que define como os dispositivos se comunicam."},
        {"termo": "protocolo de camada", "materia": "redes", "definicao": "Regras usadas na comunicação entre duas camadas equivalentes do modelo de rede."},
        {"termo": "protocolo", "materia": "direito", "definicao": "Registro formal de um ato ou documento jurídico."},
    ]


def nome_da_materia(materia):
    """Devolve o nome de exibição da matéria (com acento e maiúscula inicial)."""
    return NOMES_MATERIAS.get(materia, materia.capitalize())


def buscar_termo(dicionario_termos, termo, materia):
    """Procura um termo dentro da matéria informada. Retorna o dicionário do termo ou None."""
    for entrada in dicionario_termos:
        if entrada["termo"] == termo and entrada["materia"] == materia:
            return entrada
    return None


def buscar_em_outras_materias(dicionario_termos, termo, materia):
    """Devolve as entradas do mesmo termo cadastradas em matérias diferentes da informada."""
    return [e for e in dicionario_termos if e["termo"] == termo and e["materia"] != materia]


def obter_definicao(termo, materia):
    """Tenta sugerir uma definição pela API; se não conseguir, pede ao usuário."""
    print(f"  Termo novo em {nome_da_materia(materia)}. Buscando sugestão online...")
    sugestao = buscar_definicao_online(termo, materia)

    if sugestao:
        print(f"  Sugestão encontrada: {sugestao}")
        if ler_sim_nao("  Usar essa definição? (s/n): "):
            return sugestao
    else:
        print("  Não foi possível obter uma sugestão online (sem conexão ou termo não encontrado).")

    return ler_texto_nao_vazio("  Digite a definição do termo: ")


def cadastrar_termo(dicionario_termos, termo, materia):
    """Obtém a definição de um termo novo, adiciona ao dicionário e devolve a nova entrada."""
    definicao = obter_definicao(termo, materia)
    nova_entrada = {"termo": termo, "materia": materia, "definicao": definicao}
    dicionario_termos.append(nova_entrada)
    return nova_entrada


def exibir_outros_contextos(dicionario_termos, termo, materia):
    """Mostra como o mesmo termo é definido em outras matérias (o coração do dicionário contextual)."""
    outras = buscar_em_outras_materias(dicionario_termos, termo, materia)
    if outras:
        print("Atenção ao contexto! Esse termo tem outro significado em:")
        for entrada in outras:
            print(f"  - {nome_da_materia(entrada['materia'])}: {entrada['definicao']}")


def consultar_dicionario(dicionario_termos):
    """Consulta o significado de um termo dentro de uma matéria."""
    print("\n=== CONSULTAR DICIONÁRIO DE TERMOS ===")
    materia = ler_opcao(f"Matéria ({'/'.join(MATERIAS_VALIDAS)}): ", MATERIAS_VALIDAS)
    termo = ler_texto_nao_vazio("Termo que deseja consultar: ").lower()

    entrada = buscar_termo(dicionario_termos, termo, materia)
    if entrada:
        print(f"{termo} ({nome_da_materia(materia)}): {entrada['definicao']}")
        exibir_outros_contextos(dicionario_termos, termo, materia)
        return

    print(f"Termo ainda não cadastrado em {nome_da_materia(materia)}.")
    exibir_outros_contextos(dicionario_termos, termo, materia)
    if ler_sim_nao("Deseja cadastrá-lo nessa matéria agora? (s/n): "):
        nova_entrada = cadastrar_termo(dicionario_termos, termo, materia)
        print(f"Cadastrado! {termo} ({nome_da_materia(materia)}): {nova_entrada['definicao']}")