# BLOQUE 1 — Análisis de Problemas de Diseño

## Código heredado analyzed: `costes_Inicio.py`

## Problemas de diseño identificados

| # | Problema detectado | Impacto en producción |
|---|---|---|
| 1 | **Import no usado** (`import os`, `from openai import OpenAI`) | El código no las usa, añade carga innecesaria |
| 2 | **Ejecución directa mezclada con lógica** (líneas 69-126) | No se puede importar la clase sin ejecutar todo |
| 3 | **Constantes como atributos de clase** (`PRECIOS` dentro de `CalculadoraCostes`) | Difícil de mantener y extender |
| 4 | **Sin validación de entrada** (`tokens_input`, `tokens_output` pueden ser negativos) | Cálculos incoherentes o errores |
| 5 | **Sin manejo de errores** (modelo no existe → crash) | El programa falla silenciosamente |
| 6 | **Docstrings incompletos** | Dificulta el mantenimiento |
| 7 | **Sin type hints en algunos parámetros** | Menos claridad para el IDE |

## Análisis detallado

### Problema 1: Imports no usados
```python
import os  # NO SE USA
from openai import OpenAI  # NO SE USA
```
El código usa `tiktoken` pero no `os` ni `OpenAI`.

### Problema 2: Ejecución directa mezclada
```python
calc = CalculadoraCostes("gpt-4o-mini")
print(...)
```
Al hacer `from costes_Inicio import CalculadoraCostes`, automáticamente se ejecutan los prints.

### Problema 3: Constantes dentro de la clase
```python
class CalculadoraCostes:
    PRECIOS = {...}  # Debería estar fuera
```
Debería ser un módulo separado para facilitar cambios de precios.

### Problema 4: Sin validación
```python
def calcular_costes(self, tokens_input: int, ...):
    # ¿Qué pasa si tokens_input = -100?
```
No hay validación de valores negativos.

### Problema 5: Sin manejo de errores
```python
self.precios = self.PRECIOS.get(modelo, ...)
```
Si el modelo no existe, usa valores por defecto silenciosamente.