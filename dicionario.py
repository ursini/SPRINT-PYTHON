from config import MATERIAS_VALIDAS
from utils import ler_opcao, ler_texto_nao_vazio
 
 
def criar_dicionario_inicial():
    """Retorna a lista inicial de termos já cadastrados no dicionário contextual."""
    return [
        {"termo": "mitocondria", "materia": "biologia", "definicao": "Organela responsável pela produção de energia (ATP)."},
        {"termo": "protocolo", "materia": "redes", "definicao": "Conjunto de regras que define como os dispositivos se comunicam."},
        {"termo": "protocolo", "materia": "direito", "definicao": "Registro formal de um ato ou documento jurídico."},
    ]
 
 
def buscar_termo(dicionario_termos, termo, materia):
    """Procura um termo dentro da matéria informada. Retorna o dicionário do termo ou None."""
    for entrada in dicionario_termos:
        if entrada["termo"] == termo and entrada["materia"] == materia:
            return entrada
    return None
 
 
def cadastrar_termo(dicionario_termos, termo, materia):
    """Pede a definição de um termo novo, adiciona ao dicionário e devolve a nova entrada."""
    definicao = ler_texto_nao_vazio(f"  Termo novo em {materia}. Qual a definição? ")
    nova_entrada = {"termo": termo, "materia": materia, "definicao": definicao}
    dicionario_termos.append(nova_entrada)
    return nova_entrada
 
 
def consultar_dicionario(dicionario_termos):
    """Consulta o significado de um termo dentro de uma matéria."""
    print("\n=== CONSULTAR DICIONÁRIO DE TERMOS ===")
    materia = ler_opcao(f"Matéria ({'/'.join(MATERIAS_VALIDAS)}): ", MATERIAS_VALIDAS)
    termo = ler_texto_nao_vazio("Termo que deseja consultar: ").lower()
 
    entrada = buscar_termo(dicionario_termos, termo, materia)
    if entrada:
        print(f"{termo} ({materia}): {entrada['definicao']}")
    else:
        print("Termo ainda não cadastrado nessa matéria. Registre-o em uma próxima foto.")