# BLOQUE 3 — Tests Unitarios (COMPLETO)

## 3.1 — Prompt para generar tests

```
Genera tests unitarios para el módulo precios.py usando pytest.

Requisitos:
- Casos felices (entrada válida)
- Casos borde (límites)
- Casos de error (entrada inválida)
- Type hints
- Docstrings descriptivos

Usa pytest y pytest.approx para flotantes.
```

## 3.2 — Casos de test planificados

| Nombre del test | Tipo | Input / condición | Resultado esperado |
|---|---|---|---|
| `test_obtener_precios_gpt4o_mini` | feliz | modelo="gpt-4o-mini" | input=0.15, output=0.60 |
| `test_obtener_precios_gpt4o` | feliz | modelo="gpt-4o" | input=2.50, output=10.00 |
| `test_obtener_precios_modelo_desconocido` | borde | modelo="inválido" | usa gpt-4o-mini por defecto |
| `test_obtener_precios_gemini_flash` | feliz | modelo="gemini-1.5-flash" | input=0.075 |
| `test_obtener_precios_gpt4_turbo` | feliz | modelo="gpt-4-turbo" | input=10.00 |
| `test_obtener_precios_claude3_sonnet` | feliz | modelo="claude-3-sonnet" | input=3.00 |
| `test_listar_modelos_retorna_lista` | feliz | - | lista no vacía |
| `test_precios_todos_tienen_inputs_outputs` | borde | verifica todos | input>0, output>0 |
| `test_calcular_costes_negativo` | error | tokens=-100 | ValueError |
| `test_calcular_costes_cero` | borde | tokens=0 | coste=0 |

## 3.3 — Código de los tests

```python
# tests/test_precios.py
import pytest
from src.precios import PRECIOS, obtener_precios, listar_modelos

class TestObtenerPrecios:
    def test_obtener_precios_gpt4o_mini(self):
        precios = obtener_precios("gpt-4o-mini")
        assert precios["input"] == 0.15
        assert precios["output"] == 0.60
    
    def test_obtener_precios_modelo_desconocido(self):
        precios = obtener_precios("modelo-desconocido")
        assert precios == obtener_precios("gpt-4o-mini")
    
    # ... más tests

class TestListarModelos:
    def test_listar_modelos_retorna_lista(self):
        modelos = listar_modelos()
        assert isinstance(modelos, list)
        assert len(modelos) > 0
```

```python
# tests/test_calculo.py
import pytest
from src.calculo import CalculadoraCostes, ResultadoCoste

class TestCalcularCostes:
    def test_calcular_costes_caso_feliz(self):
        calc = CalculadoraCostes("gpt-4o-mini")
        resultado = calc.calcular_costes(200, 300, validar=False)
        assert resultado.coste_total_usd > 0
    
    def test_calcular_costes_con_validacion_error(self):
        calc = CalculadoraCostes("gpt-4o-mini")
        with pytest.raises(ValueError, match="tokens_input"):
            calc.calcular_costes(-100, 200)
```

```python
# tests/test_config.py
import os
import pytest
from unittest.mock import patch
from src.config import load_env, get_api_key, get_token

class TestGetApiKey:
    @patch.dict(os.environ, {"OPENAI_API_KEY": "sk-123"})
    def test_get_api_key_valida(self):
        key = get_api_key("OPENAI")
        assert key == "sk-123"
```