"""Tests para el módulo calculo.py."""

import pytest
from src.calculo import CalculadoraCostes, ResultadoCoste


class TestCalculadoraCostes:
    """Tests para CalculadoraCostes."""
    
    def test_init_modelo_por_defecto(self):
        """Caso feliz: modelo por defecto es gpt-4o-mini."""
        calc = CalculadoraCostes()
        assert calc.modelo == "gpt-4o-mini"
    
    def test_init_modelo_explicito(self):
        """Caso feliz: modelo especificado."""
        calc = CalculadoraCostes("gpt-4o")
        assert calc.modelo == "gpt-4o"


class TestCalcularCostes:
    """Tests para calcular_costes()."""
    
    def test_calcular_costes_cero_tokens(self):
        """Caso borde: cero tokens."""
        calc = CalculadoraCostes("gpt-4o-mini")
        resultado = calc.calcular_costes(0, 0, validar=False)
        assert resultado.coste_total_usd == 0.0
    
    def test_calcular_costes_caso_feliz(self):
        """Caso feliz: cálculo básico."""
        calc = CalculadoraCostes("gpt-4o-mini")
        resultado = calc.calcular_costes(200, 300, validar=False)
        
        coste_input_esperado = (200 / 1_000_000) * 0.15
        coste_output_esperado = (300 / 1_000_000) * 0.60
        
        assert resultado.tokens_input == 200
        assert resultado.tokens_output == 300
        assert pytest.approx(resultado.coste_input_usd) == coste_input_esperado
        assert pytest.approx(resultado.coste_output_usd) == coste_output_esperado
        assert pytest.approx(resultado.coste_total_usd) == coste_input_esperado + coste_output_esperado
    
    def test_calcular_costes_sin_validacion(self):
        """Caso borde: sin validación de entrada."""
        calc = CalculadoraCostes("gpt-4o-mini")
        resultado = calc.calcular_costes(-100, 200, validar=False)
        assert resultado.tokens_input == -100
    
    def test_calcular_costes_solo_input(self):
        """Caso borde: solo input tokens."""
        calc = CalculadoraCostes("gpt-4o-mini")
        resultado = calc.calcular_costes(1000, 0, validar=False)
        assert resultado.coste_output_usd == 0.0
        assert resultado.coste_input_usd > 0
    
    def test_calcular_costes_con_validacion_error(self):
        """Caso error: tokens negativos con validacion."""
        calc = CalculadoraCostes("gpt-4o-mini")
        with pytest.raises(ValueError, match="tokens_input"):
            calc.calcular_costes(-100, 200)
    
    def test_calcular_costes_output_negativo(self):
        """Caso error: output negativo."""
        calc = CalculadoraCostes("gpt-4o-mini")
        with pytest.raises(ValueError, match="tokens_output"):
            calc.calcular_costes(100, -200)


class TestResultadoCoste:
    """Tests para ResultadoCoste."""
    
    def test_coste_total_cent(self):
        """Caso feliz: coste_total_cent."""
        resultado = ResultadoCoste(
            tokens_input=200,
            tokens_output=300,
            coste_input_usd=0.00003,
            coste_output_usd=0.00018,
            coste_total_usd=0.00021
        )
        assert resultado.coste_total_cent == 0.021