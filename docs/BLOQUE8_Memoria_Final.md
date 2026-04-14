# Memoria Final — Refactorización de Calculadora de Costes

## 1. ¿Por qué el código original estaban mal configurado?

El código heredado en `costes_Inicio.py` presentaba **7 problemas de diseño** principales:

### 1.1 Imports no usados
```python
import os  # NO SE USA
from openai import OpenAI  # NO SE USA
```
Añade carga innecesaria y confusión.

### 1.2 Ejecución directa mezclada con lógica
```python
calc = CalculadoraCostes("gpt-4o-mini")
print(...)
```
Al importar la clase, automáticamente se ejecutan los ejemplos.

### 1.3 Constantes dentro de la clase
```python
class CalculadoraCostes:
    PRECIOS = {...}
```
Viola el principio de responsabilidad única. Los precios deben estar separados.

### 1.4 Sin validación de entrada
```python
tokens_input = -100  # Accepted sin error
```
Produce cálculos incoherentes.

### 1.5 Sin manejo de errores
```python
modelo = "inexistente"
# Usa valores por defecto silenciosamente
```

### 1.6 Docstrings incompletos
Dificulta el mantenimiento.

### 1.7 Estructura plana
Todo en un solo archivo. Imposible de testear y mantener.

---

## 2. Cambios realizados

### 2.1 Estructura nueva

```
proyecto/
├── main.py                       # Punto de entrada CLI
├── gui.py                        # Interfaz de escritorio
├── requirements.txt              # Dependencias
├── .gitignore                    # Archivos protegidos
├── env.example                   # Plantilla de variables
├── sonar-project.properties      # Config SonarCloud
├── src/                          # Código fuente
│   ├── __init__.py
│   ├── precios.py                # Precios de modelos
│   ├── tokens.py                 # Estimación de tokens
│   ├── calculo.py                # Cálculo de costes
│   ├── proyecciones.py           # Proyecciones mensuales
│   └── config.py                 # Variables de entorno
├── tests/                        # Tests unitarios
│   ├── test_calculo.py
│   ├── test_config.py
│   ├── test_precios.py
│   └── test_proyecciones.py
├── .github/workflows/             # CI/CD
│   └── ci.yml
└── docs/                          # Documentación
```

### 2.2 Mejoras implementadas

| Antes | Después | Motivo |
|-------|---------|-------|
| `import os, OpenAI` no usados | Solo `tiktoken` | Código limpio |
| Ejecución en imports | `if __name__ == "__main__"` | Import sin ejecución |
| `PRECIOS` en clase | Módulo separado `precios.py` | Mantenible |
| Sin validación | `ValueError` si negativo | Datos coherentes |
| Sin tests | **38 tests** con pytest | Confianza |
| Sin CI/CD | GitHub Actions | Automatización |
| Sin cobertura | **99% coverage** | Calidad garantizada |
| Sin seguridad | `config.py` + `.gitignore` | API keys protegidas |
| GUI básica | customtkinter + tema claro/oscuro | Interfaz profesional |

---

## 3. Aplicaciones extras (no estaban en el código original)

### 3.1 Módulo de configuración segura
```python
# src/config.py
"""Configuración segura de variables de entorno."""
from dotenv import load_dotenv

def get_api_key(service: str) -> str | None:
    """Obtiene API key de forma segura."""
    load_env()
    key = os.getenv(f"{service}_API_KEY")
    if not key or key.startswith("tu_"):
        return None
    return key
```

### 3.2 Interfaz GUI con customtkinter
- Tema oscuro (por defecto)
- Tema claro (con colors de empresa)
- Botón para cambiar entre temas
- Cálculo de costes en tiempo real
- Validación de entrada

### 3.3 Pipeline CI/CD completo
```yaml
jobs:
  test:
    - ruff (linter)
    - pytest + coverage 80%
    - Codecov
    
  security:
    - Snyk (vulnerabilidades)
    - SonarCloud (calidad código)
```

### 3.4 Archivos de protección
- `.gitignore` completo (venv, pycache, .env, etc.)
- `env.example` plantilla
- `.venv/` entorno virtual local

### 3.5 Documentación profesional
- README.md completo
- docs/ con BLOQUEx_COMPLETO.md
- Tablas de casos de test
- Commits semánticos documentados

---

## 4. Métricas finales

| Métrica | Valor |
|--------|-------|
| Tests | 38 |
| Coverage | 99% |
| Módulos src/ | 5 |
| Jobs CI/CD | 2 |
| Modelos soportados | 6 |
| Documentos docs/ | 7+ |

---

## 5. Conclusiones

La refactorización transformó un código heredado funcional pero problemático en un proyecto profesional:

- **Mantenible**: Módulos separados por responsabilidad única
- **Testeable**: 38 tests con 99% coverage
- **Automatizado**: CI/CD con GitHub Actions
- **Seguro**: API keys en variables de entorno
- **Documentado**: README + docs/
- **Extensible**: GUI con customtkinter

El proyecto está listo para producción y cumple con todos los requisitos del ejercicio de Fundación Dicampus.

---

## 6. Commits semánticos realizados

| Tipo | Mensaje |
|------|--------|
| `feat(src):` | Separar en módulos por responsabilidad |
| `test:` | Añadir 38 tests con 99% coverage |
| `ci:` | Configurar GitHub Actions con coverage 80% |
| `docs:` | Completar README del proyecto |
| `security:` | Añadir config.py para API keys |
| `feat(gui):` | Interfaz con customtkinter |
| `fix:` | Corregir división por cero en proyecciones |
| `refactor:` | Mejorar estructura del proyecto |

