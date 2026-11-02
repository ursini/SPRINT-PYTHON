"""Leitura e gravação dos dados do sistema em arquivos JSON."""
import json

from config import ARQUIVO_DICIONARIO, ARQUIVO_FOTOS


def carregar_json(caminho, valor_padrao):
    """Lê um arquivo JSON. Se não existir ou estiver corrompido, devolve o valor padrão."""
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return valor_padrao
    except json.JSONDecodeError:
        print(f"Aviso: o arquivo {caminho.name} está corrompido. Começando com dados vazios.")
        return valor_padrao
    except OSError as erro:
        print(f"Aviso: não foi possível ler {caminho.name} ({erro}).")
        return valor_padrao


def salvar_json(caminho, dados):
    """Grava os dados em JSON, criando a pasta se necessário. Devolve True se deu certo."""
    try:
        caminho.parent.mkdir(parents=True, exist_ok=True)
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)
        return True
    except OSError as erro:
        print(f"Erro ao salvar {caminho.name}: {erro}")
        return False


def carregar_dados(dicionario_inicial):
    """Carrega dicionário e fotos do disco. Na primeira execução usa o dicionário inicial."""
    dicionario_termos = carregar_json(ARQUIVO_DICIONARIO, dicionario_inicial)
    fotos_registradas = carregar_json(ARQUIVO_FOTOS, [])
    return dicionario_termos, fotos_registradas


def salvar_dados(dicionario_termos, fotos_registradas):
    """Grava dicionário e fotos no disco. Devolve True se os dois arquivos foram salvos."""
    salvou_dicionario = salvar_json(ARQUIVO_DICIONARIO, dicionario_termos)
    salvou_fotos = salvar_json(ARQUIVO_FOTOS, fotos_registradas)
    return salvou_dicionario and salvou_fotos