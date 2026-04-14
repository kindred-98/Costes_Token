# BLOQUE 2 — Modularización (COMPLETO)

## 2.1 — Estructura de carpetas

| Archivo / Carpeta | Responsabilidad única | Funciones que contiene |
|---|---|---|
| `src/precios.py` | Define precios de modelos | PRECIOS, obtener_precios(), listar_modelos() |
| `src/tokens.py` | Estimación de tokens | estimar_tokens(), estimar_tokens_por_modelo() |
| `src/calculo.py` | Cálculo de costes | CalculadoraCostes, ResultadoCoste |
| `src/proyecciones.py` | Proyecciones mensuales | ProyeccionMensual, ResultadoProyeccion |
| `src/config.py` | Variables de entorno | load_env(), get_api_key(), get_token() |
| `main.py` | Punto de entrada | Orquesta y ejecuta |
| `gui.py` | Interfaz escritorio | CalculadoraApp |

## 2.2 — Prompt para refactorizar

```
Refactoriza el siguiente código siguiendo principios SOLID:
- Separation of concerns (SRP)
- Código limpio y type hints
- Sin imports no usados
- Sin ejecución directa en importación
- Validación de entrada
- Documentación con docstrings

Código original:
[código heredado]

Requisitos:
1. Separar en módulos por responsabilidad
2. cada módulo en archivo separado
3. Usar dataclasses para retornos
4. Añadir validación de parámetros
5. Incluir type hints completos
```

## 2.3 — Código refactorizado

```python
# src/precios.py
"""Precios de modelos de IA por millón de tokens."""

from typing import TypedDict

class PreciosModelo(TypedDict):
    input: float
    output: float

PRECIOS: dict[str, PreciosModelo] = {
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    # ... más modelos
}

def obtener_precios(modelo: str) -> PreciosModelo:
    """Obtiene los precios de un modelo."""
    return PRECIOS.get(modelo, PRECIOS["gpt-4o-mini"])
```

```python
# src/tokens.py
"""Estimación de tokens usando tiktoken."""

import tiktoken

def estimar_tokens(texto: str, modelo: str = "gpt-4o-mini") -> int:
    """Estima el número de tokens de un texto."""
    if not texto:
        return 0
    encoding = tiktoken.encoding_for_model(modelo)
    return len(encoding.encode(texto))
```

```python
# src/calculo.py
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

class CalculadoraCostes:
    def __init__(self, modelo: str = "gpt-4o-mini"):
        self.modelo = modelo
        self.precios: PreciosModelo = obtener_precios(modelo)

    def calcular_costes(self, tokens_input: int, tokens_output: int, validar: bool = True) -> ResultadoCoste:
        if validar:
            self._validar_tokens(tokens_input, tokens_output)
        # ... cálculo
```

```python
# src/proyecciones.py
"""Proyecciones de uso mensual."""

from dataclasses import dataclass

@dataclass
class ResultadoProyeccion:
    llamadas_mensuales: int
    tokens_input_mensual: int
    tokens_output_mensual: int
    coste_total_usd: float
    coste_por_llamada: float