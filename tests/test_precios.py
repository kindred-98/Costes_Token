"""Tests para el módulo precios.py."""

from src.precios import PRECIOS, obtener_precios, listar_modelos


class TestObtenerPrecios:
    """Tests para obtener_precios()."""
    
    def test_obtener_precios_gpt4o_mini(self):
        """Caso feliz: obtener precios de gpt-4o-mini."""
        precios = obtener_precios("gpt-4o-mini")
        assert precios["input"] == 0.15
        assert precios["output"] == 0.60
    
    def test_obtener_precios_gpt4o(self):
        """Caso feliz: obtener precios de gpt-4o."""
        precios = obtener_precios("gpt-4o")
        assert precios["input"] == 2.50
        assert precios["output"] == 10.00
    
    def test_obtener_precios_modelo_desconocido(self):
        """Caso borde: modelo no existe, usa gpt-4o-mini por defecto."""
        precios = obtener_precios("modelo-desconocido")
        assert precios == obtener_precios("gpt-4o-mini")
    
    def test_obtener_precios_gemini_flash(self):
        """Caso feliz: gemini-1.5-flash."""
        precios = obtener_precios("gemini-1.5-flash")
        assert precios["input"] == 0.075
        assert precios["output"] == 0.30


class TestListarModelos:
    """Tests para listar_modelos()."""
    
    def test_listar_modelos_retorna_lista(self):
        """Caso feliz: retorna lista de modelos."""
        modelos = listar_modelos()
        assert isinstance(modelos, list)
        assert len(modelos) > 0
    
    def test_listar_modelos_contiene_gpt4o(self):
        """Caso feliz: lista contiene gpt-4o-mini."""
        modelos = listar_modelos()
        assert "gpt-4o-mini" in modelos


class TestPreciosConstantes:
    """Tests para verificar PRECIOS."""
    
    def test_precios_tiene_modelos(self):
        """Caso feliz: PRECIOS no está vacío."""
        assert len(PRECIOS) > 0
    
    def test_precios_todos_tienen_inputs_outputs(self):
        """Caso borde: todos los modelos tienen input y output."""
        for modelo, precios in PRECIOS.items():
            assert "input" in precios
            assert "output" in precios
            assert precios["input"] > 0
            assert precios["output"] > 0