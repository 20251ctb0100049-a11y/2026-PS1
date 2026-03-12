# debug_teste/01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!
# Rode de dentro de 05_modulos/: python debug_teste/01b-debug.py

from conversores import celsius_para_kelvin

resultado = celsius_para_kelvin(25)
print(f"25°C em K: {resultado}")

from utils.formatador import formatar_resultado

print(formatar_resultado("teste", 100, "km", 62.1, "mi"))

from conversores import km_para_milhas

print(f"50 km = {km_para_milhas(50):.2f} mi")
