"""Estimación de tokens usando tiktoken."""

import tiktoken
from typing import Optional


def estimar_tokens(texto: str, modelo: str = "gpt-4o-mini") -> int:
    """Estima el número de tokens de un texto."""
    if not texto:
        return 0
    encoding = tiktoken.encoding_for_model(modelo)
    return len(encoding.encode(texto))


def estimar_tokens_por_modelo(texto: str, modelo: Optional[str] = None) -> dict[str, int]:
    """Estima tokens para múltiples modelos."""
    modelos = ["gpt-4o", "gpt-4o-mini", "claude-3-sonnet"]
    if modelo:
        modelos = [modelo] if modelo in modelos else ["gpt-4o-mini"]
    
    resultados = {}
    for mod in modelos:
        try:
            resultados[mod] = estimar_tokens(texto, mod)
        except KeyError:
            resultados[mod] = estimar_tokens(texto, "gpt-4o-mini")
    return resultados