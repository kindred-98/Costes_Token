"""Estimación de tokens usando tiktoken."""

import tiktoken
from typing import Optional


def estimar_tokens(texto: str, modelo: str) -> int:
    modelos_openai = {
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4-turbo",
        "gpt-3.5-turbo"
    }

    # Si el modelo es de OpenAI → usar tiktoken
    if modelo in modelos_openai:
        try:
            encoding = tiktoken.encoding_for_model(modelo)
            return len(encoding.encode(texto))
        except Exception:
            pass  # fallback si falla

    # Si NO es OpenAI → estimación genérica
    # 1 token ≈ 4 caracteres
    return max(1, len(texto) // 4)

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