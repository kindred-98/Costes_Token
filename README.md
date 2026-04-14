# Calculadora de Costes de APIs de IA

Calculadora de costes para APIs de modelos de IA (OpenAI, Anthropic, Google).

## Descripción

Proyecto profesional que calcula costes estimados de uso de APIs de IA basándose en el número de tokens de entrada y salida. Incluye interfaz de escritorio, tests unitarios y pipeline CI/CD.

## Características

- Cálculo de costes por tokens
- Proyecciones mensuales
- Estimación de tokens con tiktoken
- Interfaz de escritorio (modo claro/oscuro)
- Tests con 99% coverage
- CI/CD automatizado

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/Costes_Token.git
cd Costes_Token

# Crear entorno virtual (recomendado)
python -m venv .venv

# Activar entorno virtual
# Windows: .venv\Scripts\Activate.ps1
# Linux/Mac: source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Uso CLI

```python
from src import CalculadoraCostes, ProyeccionMensual

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

## Uso GUI

```bash
python gui.py
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
├── main.py                    # Punto de entrada CLI
├── gui.py                     # Interfaz de escritorio
├── requirements.txt         # Dependencias
├── README.md                 # Documentación
├── .gitignore               # Archivos ignorados
├── sonar-project.properties # Configuración SonarCloud
├── src/                     # Código fuente
│   ├── __init__.py
│   ├── precios.py          # Precios de modelos
│   ├── tokens.py          # Estimación de tokens
│   ├── calculo.py        # Cálculo de costes
│   ├── proyecciones.py  # Proyecciones mensuales
│   └── config.py         # Variables de entorno
├── tests/                  # Tests unitarios
│   ├── test_calculo.py
│   ├── test_config.py
│   ├── test_precios.py
│   └── test_proyecciones.py
├── docs/                   # Documentación
└── .github/workflows/     # CI/CD
    └── ci.yml
```

## Tests

```bash
# Ejecutar todos los tests
pytest tests/ -v

# Con coverage
pytest tests/ --cov=src --cov-report=term-missing
```

**Coverage: 99%**

## Pipeline CI

GitHub Actions ejecuta automáticamente:

1. **Linter** (ruff) - Análisis de código
2. **Tests** - 38 tests unitarios
3. **Coverage** - Mínimo 80%
4. **SonarCloud** - Análisis de código (externo)
5. **Snyk** - Seguridad (externo)

## Variables de entorno

Copia `.env.example` a `.env` y configura tus API keys:

```bash
cp env.example .env
```

## Seguridad

- Las API keys se cargan desde variables de entorno
- Nunca hacer commit de `.env`
- Tokens en GitHub Actions como secrets

## Licencia

MIT

---

## Autor

Proyecto desarrollado como ejercicio de refactorización profesional.