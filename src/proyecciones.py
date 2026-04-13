"""Proyecciones de uso mensual."""

from dataclasses import dataclass
from .calculo import CalculadoraCostes


@dataclass
class ResultadoProyeccion:
    llamadas_mensuales: int
    tokens_input_mensual: int
    tokens_output_mensual: int
    coste_input_usd: float
    coste_output_usd: float
    coste_total_usd: float
    coste_por_llamada: float


class ProyeccionMensual:
    def __init__(self, modelo: str = "gpt-4o-mini"):
        self.calculadora = CalculadoraCostes(modelo)
    
    def proyectar(
        self,
        llamadas_por_dia: int,
        tokens_input_por_llamada: int,
        tokens_output_por_llamada: int,
        dias_mes: int = 30,
        validar: bool = True
    ) -> ResultadoProyeccion:
        """Proyecta costes mensuales."""
        if validar:
            self._validar_entrada(llamadas_por_dia, tokens_input_por_llamada, tokens_output_por_llamada)
        
        llamadas_mensuales = llamadas_por_dia * dias_mes
        tokens_input_mensual = llamadas_mensuales * tokens_input_por_llamada
        tokens_output_mensual = llamadas_mensuales * tokens_output_por_llamada
        
        resultado = self.calculadora.calcular_costes(
            tokens_input_mensual,
            tokens_output_mensual,
            validar=False
        )
        
        coste_por_llamada = (
            resultado.coste_total_usd / llamadas_mensuales 
            if llamadas_mensuales > 0 else 0.0
        )
        
        return ResultadoProyeccion(
            llamadas_mensuales=llamadas_mensuales,
            tokens_input_mensual=tokens_input_mensual,
            tokens_output_mensual=tokens_output_mensual,
            coste_input_usd=resultado.coste_input_usd,
            coste_output_usd=resultado.coste_output_usd,
            coste_total_usd=resultado.coste_total_usd,
            coste_por_llamada=coste_por_llamada
        )
    
    def _validar_entrada(
        self,
        llamadas_por_dia: int,
        tokens_input: int,
        tokens_output: int
    ) -> None:
        """Valida los parámetros de entrada."""
        if llamadas_por_dia <= 0:
            raise ValueError("llamadas_por_dia debe ser > 0")
        if tokens_input < 0:
            raise ValueError("tokens_input debe ser >= 0")
        if tokens_output < 0:
            raise ValueError("tokens_output debe ser >= 0")