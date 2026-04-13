"""Tests para el módulo proyecciones.py."""

import pytest
from src.proyecciones import ProyeccionMensual, ResultadoProyeccion


class TestProyeccionMensual:
    """Tests para ProyeccionMensual."""
    
    def test_init_modelo_por_defecto(self):
        """Caso feliz: modelo por defecto."""
        proj = ProyeccionMensual()
        assert proj.calculadora.modelo == "gpt-4o-mini"
    
    def test_init_modelo_explicito(self):
        """Caso feliz: modelo especificado."""
        proj = ProyeccionMensual("gpt-4o")
        assert proj.calculadora.modelo == "gpt-4o"


class TestProyectar:
    """Tests para proyectar()."""
    
    def test_proyectar_caso_feliz(self):
        """Caso feliz: proyección básica."""
        proj = ProyeccionMensual("gpt-4o-mini")
        resultado = proj.proyectar(
            llamadas_por_dia=100,
            tokens_input_por_llamada=200,
            tokens_output_por_llamada=300,
            dias_mes=30,
            validar=False
        )
        
        assert resultado.llamadas_mensuales == 3000
        assert resultado.tokens_input_mensual == 600000
        assert resultado.tokens_output_mensual == 900000
        assert resultado.coste_total_usd > 0
        assert resultado.coste_por_llamada > 0
    
    def test_proyectar_un_dia(self):
        """Caso borde: un día."""
        proj = ProyeccionMensual("gpt-4o-mini")
        resultado = proj.proyectar(
            llamadas_por_dia=10,
            tokens_input_por_llamada=100,
            tokens_output_por_llamada=100,
            dias_mes=1,
            validar=False
        )
        
        assert resultado.llamadas_mensuales == 10
    
    def test_proyectar_cero_llamadas(self):
        """Caso borde: cero llamadas por día."""
        proj = ProyeccionMensual("gpt-4o-mini")
        resultado = proj.proyectar(
            llamadas_por_dia=0,
            tokens_input_por_llamada=100,
            tokens_output_por_llamada=100,
            dias_mes=30,
            validar=False
        )
        
        assert resultado.llamadas_mensuales == 0
        assert resultado.coste_total_usd == 0
    
    def test_proyectar_con_validacion_error(self):
        """Caso error: llamadas negativas."""
        proj = ProyeccionMensual("gpt-4o-mini")
        with pytest.raises(ValueError, match="llamadas_por_dia"):
            proj.proyectar(
                llamadas_por_dia=-10,
                tokens_input_por_llamada=100,
                tokens_output_por_llamada=100
            )
    
    def test_proyectar_diferentes_modelos(self):
        """Caso feliz: diferentes modelos."""
        modelos = ["gpt-4o-mini", "gpt-4o", "gemini-1.5-flash"]
        
        for modelo in modelos:
            proj = ProyeccionMensual(modelo)
            resultado = proj.proyectar(10, 100, 50, validar=False)
            assert resultado.coste_total_usd > 0


class TestResultadoProyeccion:
    """Tests para ResultadoProyeccion."""
    
    def test_resultado_proyeccion_atributos(self):
        """Caso feliz: todos los atributos."""
        resultado = ResultadoProyeccion(
            llamadas_mensuales=3000,
            tokens_input_mensual=600000,
            tokens_output_mensual=900000,
            coste_input_usd=0.09,
            coste_output_usd=0.54,
            coste_total_usd=0.63,
            coste_por_llamada=0.00021
        )
        
        assert resultado.llamadas_mensuales == 3000
        assert resultado.coste_total_usd == 0.63
        assert resultado.coste_por_llamada == 0.00021