"""Configuración segura de variables de entorno."""

import os
from pathlib import Path
from dotenv import load_dotenv


def load_env() -> None:
    """Carga variables de entorno desde .env"""
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def get_api_key(service: str) -> str | None:
    """Obtiene API key de forma segura."""
    load_env()
    key = os.getenv(f"{service}_API_KEY")
    if not key or key.startswith("tu_"):
        return None
    return key


def get_token(name: str) -> str | None:
    """Obtiene token de forma segura."""
    load_env()
    token = os.getenv(name)
    if not token or token.startswith("tu_"):
        return None
    return token


__all__ = ["load_env", "get_api_key", "get_token"]