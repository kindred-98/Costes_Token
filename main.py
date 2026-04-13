"""Calculadora de Costes de APIs de IA - Punto de entrada."""

from src import CalculadoraCostes, ProyeccionMensual


def main():
    print("=" * 60)
    print("CALCULADORA DE COSTES DE APIs DE IA")
    print("=" * 60)

    calc = CalculadoraCostes("gpt-4o-mini")

    print("\n[EJEMPLO 1: Conversacion tipica (pregunta + respuesta)]")
    conversacion = calc.calcular_costes(tokens_input=200, tokens_output=300)
    print(f"Tokens input: {conversacion.tokens_input} = {conversacion.coste_input_usd:.6f} USD")
    print(f"Tokens output: {conversacion.tokens_output} = {conversacion.coste_output_usd:.6f} USD")
    print(f"Coste total: {conversacion.coste_total_usd:.6f} USD ({conversacion.coste_total_cent:.4f} centimos)")

    print("\n[EJEMPLO 2: Chatbot educativo (100 consultas/dia)]")
    proyeccion = ProyeccionMensual("gpt-4o-mini").proyectar(
        llamadas_por_dia=100,
        tokens_input_por_llamada=200,
        tokens_output_por_llamada=300
    )
    print(f"Llamadas mensuales: {proyeccion.llamadas_mensuales}")
    print(f"Coste total mensual: {proyeccion.coste_total_usd:.2f} USD")
    print(f"Coste por llamada: {proyeccion.coste_por_llamada:.6f} USD")

    print("\n[EJEMPLO 3: Aplicacion de resumenes (500 documentos/mes)]")
    proyeccion_docs = ProyeccionMensual("gpt-4o-mini").proyectar(
        llamadas_por_dia=16,
        tokens_input_por_llamada=3000,
        tokens_output_por_llamada=400
    )
    print(f"Documentos procesados: {proyeccion_docs.llamadas_mensuales}")
    print(f"Coste total mensual: {proyeccion_docs.coste_total_usd:.2f} USD")

    print("\n[EJEMPLO 4: Comparativa de modelos]")
    for modelo in ["gpt-4o-mini", "gpt-4o", "gemini-1.5-flash"]:
        resultado = ProyeccionMensual(modelo).proyectar(333, 150, 50)
        print(f"{modelo.upper()}: {resultado.coste_total_usd:.2f} USD")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()