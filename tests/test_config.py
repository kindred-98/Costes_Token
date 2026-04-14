"""Tests para el módulo config.py."""

import os
import pytest  # noqa: F401
from unittest.mock import patch
from src.config import load_env, get_api_key, get_token


class TestLoadEnv:
    """Tests para load_env()."""
    
    def test_load_env_sin_archivo(self):
        """Caso borde: sin archivo .env."""
        load_env()


class TestGetApiKey:
    """Tests para get_api_key()."""
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "sk-1234567890"})
    def test_get_api_key_valida(self):
        """Caso feliz: obtiene API key válida."""
        key = get_api_key("OPENAI")
        assert key == "sk-1234567890"
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "tu_api_key_aqui"}, clear=True)
    def test_get_api_key_no_configurada(self):
        """Caso borde: API key no configurada."""
        key = get_api_key("OPENAI")
        assert key is None
    
    @patch.dict(os.environ, {}, clear=True)
    def test_get_api_key_no_existe(self):
        """Caso borde: variable no existe."""
        key = get_api_key("OPENAI")
        assert key is None


class TestGetToken:
    """Tests para get_token()."""
    
    @patch.dict(os.environ, {"MY_TOKEN": "token_valido_123"})
    def test_get_token_valido(self):
        """Caso feliz: obtiene token válido."""
        token = get_token("MY_TOKEN")
        assert token == "token_valido_123"
    
    @patch.dict(os.environ, {"MY_TOKEN": "tu_token_aqui"}, clear=True)
    def test_get_token_no_configurado(self):
        """Caso borde: token no configurado."""
        token = get_token("MY_TOKEN")
        assert token is None
    
    @patch.dict(os.environ, {}, clear=True)
    def test_get_token_no_existe(self):
        """Caso borde: variable no existe."""
        token = get_token("MY_TOKEN")
        assert token is None