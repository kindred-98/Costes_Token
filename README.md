<div align="center">

# 🧮 Calculadora de Costes de APIs de IA

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Coverage](https://img.shields.io/badge/Coverage-99%25-brightgreen?style=flat)](https://github.com)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)](https://github.com)
[![Security](https://img.shields.io/badge/Security-Snyk-223355?style=flat&logo=snyk&logoColor=white)](https://snyk.io)
[![Quality](https://img.shields.io/badge/Quality-SonarCloud-FF6488?style=flat&logo=sonarsource&logoColor=white)](https://sonarcloud.io)

---
</div>

## 📖 Descripción

Proyecto profesional 💼 que calcula costes estimados de uso de APIs de IA basándose en el número de tokens de entrada y salida. 
Incluye interfaz de escritorio interactiva, tests unitarios robustos y pipeline CI/CD completamente automatizado.

### ✨ Características Principales

| Característica | Descripción |
|----------------|-------------|
| 🔢 **Cálculo de Costes** | Calcula costes por tokens de entrada y salida |
| 📊 **Proyecciones** | Estima uso mensual y anual |
| 🤖 **Estimación de Tokens** | Usa tiktoken para precisión |
| 🖥️ **Interfaz GUI** | Modo claro/oscuro con customtkinter |
| ✅ **Tests** | 38 tests con 99% coverage |
| ⚡ **CI/CD** | Automatización completa |

---

## 🚀 Instalación

```bash
# 📥 Clonar el repositorio
git clone https://github.com/tu-usuario/Costes_Token.git
cd Costes_Token

# 🐍 Crear entorno virtual (recomendado)
python -m venv .venv

# ✅ Activar entorno virtual
# Windows (PowerShell): .venv\Scripts\Activate.ps1
# Windows (CMD):    .venv\Scripts\activate.bat
# Linux/Mac:       source .venv/bin/activate

# 📦 Instalar dependencias
pip install -r requirements.txt
```

---

## 💻 Uso CLI

```python
# 📥 Importar módulos
from src import CalculadoraCostes, ProyeccionMensual

# 💰 Calcular coste de una llamada API
calc = CalculadoraCostes("gpt-4o-mini")
resultado = calc.calcular_costes(tokens_input=200, tokens_output=300)
print(f"💵 Coste: {resultado.coste_total_usd} USD")

# 📈 Proyectar uso mensual
proyeccion = ProyeccionMensual("gpt-4o-mini").proyectar(
    llamadas_por_dia=100,
    tokens_input_por_llamada=200,
    tokens_output_por_llamada=300
)
print(f"📅 Coste mensual: {proyeccion.coste_total_usd} USD")
```

---

## 🖥️ Uso GUI (Interfaz Gráfica)

```bash
# 🎨 Ejecutar interfaz de escritorio
python gui.py
```

| Elemento | Descripción |
|----------|-------------|
| 🎯 **Modelo** | Selector de modelo de IA |
| 📝 **Texto** | Campo para analizar |
| 🧮 **Calcular** | Botón principal |
| 🧹 **Limpiar** | Limpia campos |
| 🚪 **Salir** | Cierra aplicación |
| 🌗 **Tema** | Cambia entre claro/oscuro |

---

## 🤖 Modelos de IA Soportados

| Modelo | Input ($/M) | Output ($/M) |
|--------|------------|-------------|
| 🤖 gpt-4o | $2.50 | $10.00 |
| ⚡ gpt-4o-mini | $0.15 | $0.60 |
| 🚀 gpt-4-turbo | $10.00 | $30.00 |
| 🧠 claude-3-sonnet | $3.00 | $15.00 |
| ✨ gemini-1.5-flash | $0.075 | $0.30 |
| 💎 gemini-1.5-pro | $1.25 | $5.00 |

---

## 📁 Estructura del Proyecto

```
proyecto/
├── 📄 main.py                       # ▸ Punto de entrada CLI
├── 🖥️ gui.py                        # ▸ Interfaz de escritorio
├── 📦 requirements.txt              # ▸ Dependencias del proyecto
├── 📚 README.md                     # ▸ Este documento
├── 🛡️ .gitignore                    # ▸ Archivos protegidos
├── 📝 env.example                   # ▸ Plantilla de variables
├── 🔐 sonar-project.properties      # ▸ Configuración SonarCloud
├── 📂 src/                          # ▸ Código fuente
│   ├── __init__.py
│   ├── 💰 precios.py                # ▸ Precios de modelos
│   ├── 🔢 tokens.py                 # ▸ Estimación de tokens
│   ├── 🧮 calculo.py                # ▸ Cálculo de costes
│   ├── 📈 proyecciones.py           # ▸ Proyecciones mensuales
│   └── 🔐 config.py                 # ▸ Variables de entorno
├── 🧪 tests/                        # ▸ Tests unitarios
│   ├── test_calculo.py
│   ├── test_config.py
│   ├── test_precios.py
│   └── test_proyecciones.py
├── 📖 docs/                         # ▸ Documentación
└── ⚙️ .github/workflows/            # ▸ Pipeline CI/CD
    └── ci.yml
```

---

## 🧪 Tests

```bash
# ▶️ Ejecutar todos los tests
pytest tests/ -v

# 📊 Con coverage detallado
pytest tests/ --cov=src --cov-report=term-missing
```

### 📈 Métricas de Tests

| Métrica | Valor |
|--------|-------|
| 🧪 **Total Tests** | 38 |
| ✅ **Passing** | 38 (100%) |
| 📊 **Coverage** | 99% |
| ⚡ **Coverage mínimo** | 80% |

---

## ⚙️ Pipeline CI/CD

| Fase | Herramienta | Descripción |
|------|-----------|-----------|
| 🔍 **Linter** | ruff | Análisis de código estático |
| 🧪 **Tests** | pytest | Ejecución de pruebas |
| 📊 **Coverage** | pytest-cov | Coverage mínimo 80% |
| 🌐 **Codecov** | Codecov | Reporte de coverage |
| 🔒 **Seguridad** | Snyk | Análisis de vulnerabilidades |
| 🎯 **Calidad** | SonarCloud | Análisis de código |

---

## 🔐 Variables de Entorno

```bash
# 📋 Copiar plantilla
cp env.example .env

# ✏️ Editar con tus API keys
OPENAI_API_KEY=tu_api_key_aqui
ANTHROPIC_API_KEY=tu_api_key_aqui
```

---

## 🛡️ Seguridad

| Medida | Implementación |
|--------|--------------|
| 🔑 **API Keys** | Variables de entorno (`.env`) |
| 🚫 **Secrets** | Nunca hacer commit |
| 🔐 **GitHub Actions** | Secrets encriptados |
| 📛 **.gitignore** | Protegido automáticamente |

---

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.

---

## 👤 Autor

| Información | Detalle |
|-------------|---------|
| 👤 **Nombre** | **A.D.E.V** |
| 📧 **Email** | angelechenique134@gmail.com |
| 🐙 **GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-kindred--98-181717?style=for-the-badge&logo=github)](https://github.com/kindred-98) |
| 🏢 **Organización** | Kindred |

---

## 🎉 Contribuir

¡Las contribuciones son bienvenidas! 📝

1. 🍴 Fork del repositorio
2. 🌿 Crear rama (`git checkout -b feature/nueva-funcionalidad`)
3. �  Commit cambios (`git commit -m '✨feat: nueva funcionalidad'`)
4. 🚀 Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. 📬 Pull Request

---

<div align="center">

## 🌟 Proyecto Completado por A.D.E.V

*Construido con Python 🐍, pytest 🧪, GitHub Actions ⚡ y muchta determinación 💪*

</div>