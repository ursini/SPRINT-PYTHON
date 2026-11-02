"""Exportação dos dados para o restante da solução (aplicação web em React)."""
from datetime import datetime

from config import ARQUIVO_EXPORTACAO
from persistencia import salvar_json
from registro import calcular_estatisticas


def montar_pacote_exportacao(dicionario_termos, fotos_registradas):
    """Monta o dicionário que será gravado no arquivo de integração."""
    return {
        "projeto": "VisionForge | JOVI | Lens IA",
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "estatisticas": calcular_estatisticas(fotos_registradas),
        "fotos": fotos_registradas,
        "dicionario": dicionario_termos,
    }


def exportar_dados(dicionario_termos, fotos_registradas):
    """Gera o arquivo JSON de integração com o app web e informa o resultado ao usuário."""
    print("\n=== EXPORTAR DADOS PARA O APP WEB ===")
    if not fotos_registradas:
        print("Ainda não há fotos registradas. Será exportado apenas o dicionário.")

    pacote = montar_pacote_exportacao(dicionario_termos, fotos_registradas)
    if salvar_json(ARQUIVO_EXPORTACAO, pacote):
        print(f"Arquivo gerado em: {ARQUIVO_EXPORTACAO}")
        print(f"Conteúdo: {len(fotos_registradas)} foto(s) e {len(dicionario_termos)} termo(s).")
    else:
        print("Não foi possível gerar o arquivo de exportação.")