# ==========================================================
# SISTEMA DE CONVERSÃO DE UNIDADES
# ==========================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 07 - Revisão: Módulos
# Autor      : rafael lopes
# Data       : 12/03/2026
# Repositório: https://github.com/20251ctb0100049-a11y/2026-PS1
# ==========================================================

from conversores import (
    celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius,
    km_para_milhas, milhas_para_km, metros_para_pes,
)

from utils import cabecalho_secao, formatar_resultado, linha_separadora

def menu_temperatura():
    print(cabecalho_secao("Conversão de Temperatura"))
    valor = float(input(" Valor em °C: "))
    from conversores import (
    celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius,
    km_para_milhas, milhas_para_km, metros_para_pes,
)

from utils import cabecalho_secao, formatar_resultado, linha_separadora


def menu_temperatura():
    print(cabecalho_secao("Conversão de Temperatura"))
    valor = float(input(" Valor em °C: "))
    
    print(formatar_resultado("°C -> °F", valor, "°C", 
    celsius_para_fahrenheit(valor), "°F"))
    
    print(formatar_resultado("°C -> K", valor, "°C", celsius_para_kelvin(valor), 
    "K"))

def menu_distancia():
    print(cabecalho_secao("Conversão de Distância"))
    valor = float(input(" Valor em km: "))
    
    print(formatar_resultado("km -> mi", valor, "km", km_para_milhas(valor), "mi"))
    
    print(formatar_resultado("km -> pés", valor * 1000, "m", metros_para_pes(valor * 1000), "pés"))


def main():
    print(linha_separadora())
    print("  SISTEMA DE CONVERSÃO DE UNIDADES")
    print(linha_separadora())

    opcoes = {"1": menu_temperatura, "2": menu_distancia}

    while True:
        print("\n [1] Temperatura  [2] Distância  [0] Sair")
        escolha = input(" Opção: ").strip()
        if escolha == "0":
            print("\nSistema encerrado.")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print(" Opção inválida.")

if __name__ == "__main__":
    main()
    