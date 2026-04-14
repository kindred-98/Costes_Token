# BLOQUE 5 — Documentación (COMPLETO)

## 5.1 — Estructura de docs/

| Archivo en docs/ | Contenido / propósito |
|---|---|
| `index.md` | Índice de documentación |
| `BLOQUE1_Analisis_Problemas.md` | Análisis de problemas de diseño |
| `BLOQUE7_Reflexion.md` | Reflexión integrada y autoevaluación |
| `BLOQUE8_Memoria_Final.md` | Memoria final del proyecto |

## 5.2 — README.md

```markdown
# Calculadora de Costes de APIs de IA

Calculadora de coste para APIs de modelos de IA (OpenAI, Anthropic, Google).

## Descripción

Proyecto que calcula costes estimados de uso de APIs de IA basándose en el número de tokens.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```python
from src import CalculadoraCostes, ProyeccionMensual

calc = CalculadoraCostes("gpt-4o-mini")
resultado = calc.calcular_costes(tokens_input=200, tokens_output=300)
print(f"Coste: {resultado.coste_total_usd} USD")
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
├── main.py           # Punto de entrada
├── gui.py           # Interfaz de escritorio
├── requirements.txt # Dependencias
├── src/            # Código fuente
│   ├── precios.py
│   ├── tokens.py
│   ├── calculo.py
│   └── proyecciones.py
└── tests/         # Tests unitarios
```

## Tests

```bash
pytest tests/ -v
```

## Pipeline CI

GitHub Actions ejecuta:
- Linter (ruff)
- Tests + Coverage 80%
- SonarCloud (externo)
- Snyk (externo)

## Licencia

MIT
```

## 5.3 — Commits semánticos

| Tipo de cambio | Tu mensaje de commit | ¿Por qué este mensaje? |
|---|---|---|
| Modularización | `feat(src): separar en módulos por responsabilidad` | Nueva funcionalidad | Añadir tests | `test: añadir 38 tests con 99% coverage` | Cobertura mejorada |
| CI/CD | `ci: configurar GitHub Actions con coverage 80%` | Automatización |
| Documentación README | `docs: completar README del proyecto` | Documentación |
| Corrección de bug | `fix: corregir división por cero en proyecciones` | Bug corregido |
| Configuración seguridad | `security: añadir config.py para API keys` | Seguridad |
| GUI | `feat(gui): añadir interfaz con customtkinter` | Nueva funcionalidad |