"""Cálculo de costes de APIs de IA."""

from dataclasses import dataclass
from .precios import obtener_precios, PreciosModelo


@dataclass
class ResultadoCoste:
    tokens_input: int
    tokens_output: int
    coste_input_usd: float
    coste_output_usd: float
    coste_total_usd: float
    
    @property
    def coste_total_cent(self) -> float:
        return self.coste_total_usd * 100


class CalculadoraCostes:
    def __init__(self, modelo: str = "gpt-4o-mini"):
        self.modelo = modelo
        self.precios: PreciosModelo = obtener_precios(modelo)
    
    def calcular_costes(
        self, 
        tokens_input: int, 
        tokens_output: int,
        validar: bool = True
    ) -> ResultadoCoste:
        """Calcula el coste de una llamada API."""
        if validar:
            self._validar_tokens(tokens_input, tokens_output)
        
        coste_input = (tokens_input / 1_000_000) * self.precios["input"]
        coste_output = (tokens_output / 1_000_000) * self.precios["output"]
        
        return ResultadoCoste(
            tokens_input=tokens_input,
            tokens_output=tokens_output,
            coste_input_usd=coste_input,
            coste_output_usd=coste_output,
            coste_total_usd=coste_input + coste_output
        )
    
    def _validar_tokens(self, tokens_input: int, tokens_output: int) -> None:
        """Valida que los tokens sean positivos."""
        if tokens_input < 0:
            raise ValueError("tokens_input debe ser >= 0")
        if tokens_output < 0:
            raise ValueError("tokens_output debe ser >= 0")