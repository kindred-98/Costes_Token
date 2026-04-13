"""Precios de modelos de IA por millón de tokens."""

from typing import TypedDict


class PreciosModelo(TypedDict):
    input: float
    output: float


PRECIOS: dict[str, PreciosModelo] = {
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4-turbo": {"input": 10.00, "output": 30.00},
    "claude-3-sonnet": {"input": 3.00, "output": 15.00},
    "gemini-1.5-flash": {"input": 0.075, "output": 0.30},
    "gemini-1.5-pro": {"input": 1.25, "output": 5.00},
}


def obtener_precios(modelo: str) -> PreciosModelo:
    """Obtiene los precios de un modelo."""
    return PRECIOS.get(modelo, PRECIOS["gpt-4o-mini"])


def listar_modelos() -> list[str]:
    """Lista todos los modelos disponibles."""
    return list(PRECIOS.keys())