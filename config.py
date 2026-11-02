"""Constantes de configuração do projeto VisionForge | Lens IA."""
from pathlib import Path

MATERIAS_VALIDAS = ["biologia", "redes", "direito", "matematica", "historia"]
NOMES_MATERIAS = {
    "biologia": "Biologia",
    "redes": "Redes",
    "direito": "Direito",
    "matematica": "Matemática",
    "historia": "História",
}

TIPOS_MARCACAO = ["circulo", "sublinhado", "asterisco", "maiusculo"]
NOMES_TIPOS = {
    "circulo": "círculo",
    "sublinhado": "sublinhado",
    "asterisco": "asterisco",
    "maiusculo": "palavra em maiúsculo",
}

PASTA_ARQUIVO_VIRTUAL = "Estudo_Importante"

PASTA_BASE = Path(__file__).resolve().parent
PASTA_DADOS = PASTA_BASE / "dados"
PASTA_EXPORTACAO = PASTA_BASE / "exportacao"
ARQUIVO_DICIONARIO = PASTA_DADOS / "dicionario.json"
ARQUIVO_FOTOS = PASTA_DADOS / "fotos.json"
ARQUIVO_EXPORTACAO = PASTA_EXPORTACAO / "lens_ia_export.json"

FORMATO_DATA = "%d/%m/%Y"

# API externa: Wikipédia
URL_API_WIKIPEDIA = "https://pt.wikipedia.org/w/api.php"
TIMEOUT_API_SEGUNDOS = 5
TAMANHO_MAXIMO_DEFINICAO = 300