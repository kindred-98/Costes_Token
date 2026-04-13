# Calculadora de Costes de APIs de IA

Calculadora de coste para APIs de modelos de IA (OpenAI, Anthropic, Google).

## Descripción

Proyecto que calcula costes estimados de uso de APIs de IA basándose en el número de tokens de entrada y salida.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```python
from calculadora import CalculadoraCostes, ProyeccionMensual

# Calcular coste de una llamada
calc = CalculadoraCostes("gpt-4o-mini")
resultado = calc.calcular_costes(tokens_input=200, tokens_output=300)
print(f"Coste: {resultado.coste_total_usd} USD")

# Proyectar uso mensual
proyeccion = ProyeccionMensual("gpt-4o-mini").proyectar(
    llamadas_por_dia=100,
    tokens_input_por_llamada=200,
    tokens_output_por_llamada=300
)
print(f"Coste mensual: {proyeccion.coste_total_usd} USD")
```

## Modelos soportados

- gpt-4o
- gpt-4o-mini
- gpt-4-turbo
- claude-3-sonnet
- gemini-1.5-flash
- gemini-1.5-pro

## Estructura del proyecto

```
proyecto/
├── main.py                 # Punto de entrada
├── gui.py                 # Interfaz de escritorio
├── requirements.txt      # Dependencias
├── src/                  #Código fuente
│   ├── __init__.py
│   ├── precios.py       # Precios de modelos
│   ├── tokens.py        # Estimación de tokens
│   ├── calculo.py       # Cálculo de costes
│   └── proyecciones.py  # Proyecciones mensuales
├── tests/               # Tests unitarios
└── .github/workflows/  # CI/CD
```

## Tests

```bash
pytest tests/ -v
```

## Pipeline CI

GitHub Actions ejecuta automáticamente:
- Linter (ruff)
- Tests unitarios
- Cobertura de código

## Licencia

MIT