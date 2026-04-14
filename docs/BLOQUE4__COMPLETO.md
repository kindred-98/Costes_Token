# BLOQUE 4 — Pipeline CI/CD (COMPLETO)

## 4.1 — Fases del pipeline

| Fase del pipeline | ¿Qué debe hacer? | Comando / herramienta |
|---|---|---|
| 1. Checkout del código | Descarga el repositorio | `actions/checkout@v4` |
| 2. Configurar Python | Instala Python 3.14 | `actions/setup-python@v5` |
| 3. Instalar dependencias | Instala librerías | `pip install -r requirements.txt` |
| 4. Ejecutar linter | Revisa código | `ruff check src/ tests/` |
| 5. Tests unitarios | Ejecuta pruebas | `pytest tests/ -v` |
| 6. Cobertura de tests | Verifica coverage | `pytest --cov=src --cov-fail-under=80` |
| 7. Análisis de seguridad | Busca vulnerabilidades | `snyk` (externo) |
| 8. Análisis de código | Calidad del código | `SonarCloud` (externo) |

## 4.2 — Fichero ci.yml completo

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.14'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      
      - name: Run linter (ruff)
        run: pip install ruff && ruff check src/ tests/
      
      - name: Run tests with coverage
        run: pytest tests/ -v --cov=src --cov-report=xml --cov-fail-under=80
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml
          flags: unittests

  security:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Run Snyk
        uses: snyk/actions/python@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      
      - name: Run SonarCloud
        uses: SonarSource/sonarcloud-github-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 4.3 — ¿Qué ocurre si un test falla?

**Flujo cuando un test falla:**

1. **El pipeline se detiene** - No pasa a la siguiente fase
2. **Se bloquea el merge** - No puedes hacer merge del PR
3. **Notificación automática** - GitHub te avisa por email y en el PR
4. **Logs disponibles** - En la pestaña "Actions" del repositorio
5. **Cómo depurar:**
   - Ve a GitHub → Actions → Click en el workflow fallido
   - Revisa los logs de cada step
   - El error te indica qué test falló y por qué
   - Arregla el código o el test
   - Haz push de nuevo

**Si pones coverage baja del 80%:**
- El pipeline falla
- Tienes que añadir más tests
- No se permite hacer merge