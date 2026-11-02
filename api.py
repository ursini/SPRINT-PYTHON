"""Integração com a API externa da Wikipédia para sugerir definições de termos."""
import json
import urllib.error
import urllib.parse
import urllib.request

from config import TAMANHO_MAXIMO_DEFINICAO, TIMEOUT_API_SEGUNDOS, URL_API_WIKIPEDIA


def montar_url_busca(termo, materia):
    """Monta a URL de busca usando a matéria como contexto (ex: 'protocolo redes')."""
    parametros = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": f"{termo} {materia}",
        "gsrlimit": 1,
        "prop": "extracts",
        "exintro": 1,
        "explaintext": 1,
        "exsentences": 2,
        "redirects": 1,
    }
    return f"{URL_API_WIKIPEDIA}?{urllib.parse.urlencode(parametros)}"


def extrair_definicao(resposta_json):
    """Extrai o texto do primeiro resultado da resposta da API. Devolve None se não houver."""
    paginas = resposta_json.get("query", {}).get("pages", {})
    for pagina in paginas.values():
        texto = pagina.get("extract", "").strip()
        if texto:
            if len(texto) > TAMANHO_MAXIMO_DEFINICAO:
                texto = texto[:TAMANHO_MAXIMO_DEFINICAO].rstrip() + "..."
            return texto
    return None


def buscar_definicao_online(termo, materia):
    """Consulta a Wikipédia e devolve uma definição sugerida, ou None se falhar."""
    url = montar_url_busca(termo, materia)
    requisicao = urllib.request.Request(
        url, headers={"User-Agent": "VisionForge-LensIA/1.0 (projeto academico FIAP)"}
    )
    try:
        with urllib.request.urlopen(requisicao, timeout=TIMEOUT_API_SEGUNDOS) as resposta:
            conteudo = json.loads(resposta.read().decode("utf-8"))
        return extrair_definicao(conteudo)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, UnicodeDecodeError):
        return None