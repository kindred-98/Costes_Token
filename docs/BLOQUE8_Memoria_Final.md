# Memoria Final — Refactorización de Calculadora de Costes

## ¿Por qué el código original estaba mal configurado?

El código heredado en `costes_Inicio.py` presentaba **7 problemas de diseño** principales:

### 1. Imports no usados
```python
import os  # NO SE USA
from openai import OpenAI  # NO SE USA
```
Añade carga innecesaria y confusión.

### 2. Ejecución directa mezclada con lógica
```python
calc = CalculadoraCostes("gpt-4o-mini")
print(...)
```
Al importar la clase, automáticamente se ejecutan los ejemplos.

### 3. Constantes dentro de la clase
```python
class CalculadoraCostes:
    PRECIOS = {...}
```
Viola el principio de responsabilidad única. Los precios deben estar separados.

### 4. Sin validación de entrada
```python
tokens_input = -100  # Accepted sin error
```
Produce cálculos incoherentes.

### 5. Sin manejo de errores
```python
modelo = "inexistente"
# Usa valores por defecto silenciosamente
```

### 6. Docstrings incompletos
Dificulta el mantenimiento.

### 7. Estructura plana
Todo en un solo archivo. Imposible de testear y mantener.

---

## Cambios realizados

### Estructura nueva
```
proyecto/
├── main.py
├── gui.py
├── requirements.txt
├── calculadora/
│   ├── __init__.py
│   ├── precios.py      (separado)
│   ├── tokens.py       (separado)
│   ├── calculo.py     (separado)
│   └── proyecciones.py (separado)
├── tests/
│   ├── test_precios.py
│   ├── test_calculo.py
│   └── test_proyecciones.py
├── .github/workflows/
│   └── ci.yml
└── docs/
```

### Mejoras implementadas

| Antes | Después | Motivo |
|-------|---------|-------|
| `import os, OpenAI` no usados | Solo `tiktoken` | Código limpio |
| Ejecución en imports | `if __name__ == "__main__"` | Import sin ejecución |
| `PRECIOS` en clase | Módulo separado `precios.py` | Mantenible |
| Sin validación | `ValueError` si negativo | Datos coherentes |
| Sin manejo errores | Fallback con warning | Trazabilidad |
| Sin tests | 25 tests con pytest | Confianza |
| Sin CI/CD | GitHub Actions | Automatización |
| Sin docs | README + docs/ | Documentación |

---

## Conclusiones

La refactorización transformó un código heredado funcional pero problemático en un proyecto profesional:

- **Mantenible**: Módulos separados
- **Testeable**: 25 tests pasando
- **Automatizado**: CI/CD configurado
- **Documentado**: README y docs/
- **Extensible**: GUI incluida

El proyecto está listo para producción y cumple con todos los requisitos del ejercicio.