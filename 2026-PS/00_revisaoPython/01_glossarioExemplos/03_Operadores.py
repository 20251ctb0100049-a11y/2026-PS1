# -*- coding: utf-8 -*-
"""
==============================================================================
ARQUIVO: 03_Operadores.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo sobre Operadores em Python.
    Baseado integralmente no "Glossário 04 - Operadores".

CONTEÚDO PROGRAMÁTICO:
    1. Atribuição Simples e Composta (=, +=, -=).
    2. Operadores Aritméticos (+, -, *, /, //, %, **).
    3. Operadores Relacionais/Comparação (==, !=, >, <).
    4. Operadores Lógicos (and, or, not).
    5. Precedência de Operadores (Ordem de avaliação).
    6. Operações com Strings (Concatenação e Repetição).
    7. Exemplo Integrador: Simulador de Desconto.

==============================================================================
"""

import sys
import time

def limpar_tela():
    """Limpa visualmente o terminal."""
    print("\n" * 5)
    print("=" * 80)

def esperar():
    """Pausa para leitura."""
    input("\n[Pressione ENTER para continuar...]")

def mostrar_codigo_didatico(codigo):
    """Exibe o código com numeração e destaque para os comentários."""
    print("\n📄 CÓDIGO EM ANÁLISE (Observe os comentários #):")
    print("-" * 80)
    linhas = codigo.strip().split('\n')
    for i, linha in enumerate(linhas):
        print(f"{i+1:02d} | {linha}")
    print("-" * 80)
    print("\n▶️  INICIANDO EXECUÇÃO PASSO A PASSO...\n")
    time.sleep(1.5)
    return linhas

def executar_linha(numero_linha, atraso=1.0):
    """Simula o processamento da linha."""
    print(f"⚙️  [Lendo Linha {numero_linha:02d}]...", end="\r")
    time.sleep(atraso)
    print(f"✅ [Executado Linha {numero_linha:02d}]   ")

# ==============================================================================
# TÓPICO 1: ATRIBUIÇÃO (SIMPLES E COMPOSTA)
# ==============================================================================
def atribuicao():
    limpar_tela()
    print("🔹 TÓPICO 1: OPERADORES DE ATRIBUIÇÃO")
    print("-" * 80)
    print("Conceito: O sinal '=' não é igualdade, é ATRIBUIÇÃO (Recebe).")
    print("Atalhos: +=, -=, *= (realizam a conta e guardam o resultado).")
    print("-" * 80)

    # Exemplo baseado no Exemplo 3 do Glossário
    codigo = """# Atribuição Simples
contador = 0            # Variável 'contador' recebe 0

# Atribuição Composta (Incremento)
contador += 1           # Equivalente a: contador = contador + 1
print(f"Contador: {contador}")

# Acumulador (Soma progressiva)
total = 100
total -= 20             # Equivalente a: total = total - 20 (Desconto)
total *= 2              # Equivalente a: total = total * 2 (Dobro)
print(f"Total: {total}")"""

    mostrar_codigo_didatico(codigo)

    executar_linha(2)
    print("   ↳ MEMÓRIA: 'contador' iniciado com 0.")

    executar_linha(5)
    print("   ↳ CÁLCULO: 0 + 1 = 1. 'contador' atualizado para 1.")
    
    executar_linha(6)
    print("   ↳ SAÍDA: Contador: 1")

    executar_linha(9)
    print("   ↳ MEMÓRIA: 'total' iniciado com 100.")
    
    executar_linha(10)
    print("   ↳ CÁLCULO: 100 - 20 = 80. 'total' atualizado para 80.")
    
    executar_linha(11)
    print("   ↳ CÁLCULO: 80 * 2 = 160. 'total' atualizado para 160.")
    
    executar_linha(12)
    print("   ↳ SAÍDA: Total: 160")
    
    esperar()

# ==============================================================================
# TÓPICO 2: ARITMÉTICOS E O PODER DO MÓDULO
# ==============================================================================
def aritmeticos():
    limpar_tela()
    print("🔹 TÓPICO 2: OPERADORES ARITMÉTICOS")
    print("-" * 80)
    print("Além do básico (+ - * /), Python tem operadores especiais:")
    print("   // : Divisão Inteira (descarta a parte decimal)")
    print("   %  : Módulo (Resto da divisão) -> Muito útil para lógica!")
    print("   ** : Potência (Exponenciação)")
    print("-" * 80)
    
    # Baseado nos Exemplos 1, 2 e 9 do Glossário
    codigo = """a = 10
b = 3

print(f"Divisão Real (/):    {a / b:.2f}")  # 3.33
print(f"Divisão Inteira (//): {a // b}")    # 3 (apenas a parte inteira)
print(f"Resto da Divisão (%): {a % b}")     # 1 (sobra da divisão de 10 por 3)
print(f"Potência (**):        {a ** 2}")    # 10 ao quadrado = 100

# Uso prático do % (Módulo) para verificar Par/Ímpar
num = 4
e_par = (num % 2 == 0)  # Se resto por 2 for 0, é par
print(f"O número {num} é par? {e_par}")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1); executar_linha(2)
    
    executar_linha(4)
    print("   ↳ SAÍDA: Divisão Real (/):    3.33")
    
    executar_linha(5)
    print("   ↳ SAÍDA: Divisão Inteira (//): 3")
    
    executar_linha(6)
    print("   ↳ LÓGICA: 10 dividido por 3 dá 3 e sobra 1.")
    print("   ↳ SAÍDA: Resto da Divisão (%): 1")
    
    executar_linha(7)
    print("   ↳ SAÍDA: Potência (**):        100")
    
    executar_linha(10)
    print("   ↳ MEMÓRIA: num = 4")
    
    executar_linha(11)
    print("   ↳ CÁLCULO: 4 % 2 é 0? Sim. Então e_par recebe True.")
    
    executar_linha(12)
    print("   ↳ SAÍDA: O número 4 é par? True")
    
    esperar()

# ==============================================================================
# TÓPICO 3: RELACIONAIS (COMPARAÇÃO)
# ==============================================================================
def relacionais():
    limpar_tela()
    print("🔹 TÓPICO 3: OPERADORES RELACIONAIS")
    print("-" * 80)
    print("Objetivo: Comparar valores.")
    print("Retorno: SEMPRE um Booleano (True ou False).")
    print("Cuidado: '=' é atribuição. '==' é comparação.")
    print("-" * 80)
    
    # Baseado no Exemplo 4 do Glossário
    codigo = """nota = 7.5

# Comparações diretas
print(nota > 7)      # Maior que?
print(nota == 10)    # Igual a? (Note o duplo igual ==)
print(nota != 0)     # Diferente de?

# Comparação encadeada (Recurso exclusivo do Python!)
idade = 25
# Verifica se está entre 18 e 65 numa única linha
print(18 <= idade <= 65)"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    
    executar_linha(4)
    print("   ↳ AVALIAÇÃO: 7.5 > 7? -> True")
    
    executar_linha(5)
    print("   ↳ AVALIAÇÃO: 7.5 é igual a 10? -> False")
    
    executar_linha(6)
    print("   ↳ AVALIAÇÃO: 7.5 é diferente de 0? -> True")
    
    executar_linha(9)
    print("   ↳ MEMÓRIA: idade = 25")
    
    executar_linha(11)
    print("   ↳ AVALIAÇÃO: 18 <= 25 <= 65? -> True (Está no intervalo)")
    
    print("\n⚠️  ERRO COMUM: Usar '=' em if (if nota = 10). Isso gera SyntaxError.")
    esperar()

# ==============================================================================
# TÓPICO 4: LÓGICOS (AND, OR, NOT)
# ==============================================================================
def logicos():
    limpar_tela()
    print("🔹 TÓPICO 4: OPERADORES LÓGICOS")
    print("-" * 80)
    print("Conectam múltiplas condições.")
    print("   and : TUDO deve ser verdade.")
    print("   or  : PELO MENOS UM deve ser verdade.")
    print("   not : INVERTE o valor (True vira False).")
    print("-" * 80)
    
    # Baseado no Exemplo 5 do Glossário
    codigo = """idade = 20
renda = 3000
possui_nome_limpo = True

# Cenário 1: Empréstimo (Exige Renda E Nome Limpo)
# Ambas as condições precisam ser True
aprovado = (renda >= 2000) and possui_nome_limpo
print(f"Empréstimo Aprovado? {aprovado}")

# Cenário 2: Meia Entrada (Estudante OU Idoso)
estudante = False
idoso = True
# Basta uma condição ser True
tem_desconto = estudante or idoso
print(f"Tem desconto? {tem_desconto}")

# Cenário 3: Negação
chovendo = False
# Se NÃO estiver chovendo...
if not chovendo:
    print("Pode sair sem guarda-chuva!")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1); executar_linha(2); executar_linha(3)
    
    executar_linha(7)
    print("   ↳ LÓGICA: (True) AND (True) -> Resultado: True")
    
    executar_linha(8)
    print("   ↳ SAÍDA: Empréstimo Aprovado? True")
    
    executar_linha(11); executar_linha(12)
    
    executar_linha(14)
    print("   ↳ LÓGICA: (False) OR (True) -> Resultado: True")
    
    executar_linha(15)
    print("   ↳ SAÍDA: Tem desconto? True")
    
    executar_linha(18)
    
    executar_linha(20)
    print("   ↳ LÓGICA: not False -> True. Entra no IF.")
    
    executar_linha(21)
    print("   ↳ SAÍDA: Pode sair sem guarda-chuva!")
    
    esperar()

# ==============================================================================
# TÓPICO 5: PRECEDÊNCIA E STRINGS
# ==============================================================================
def precedencia_strings():
    limpar_tela()
    print("🔹 TÓPICO 5: PRECEDÊNCIA E OPERADORES DE TEXTO")
    print("-" * 80)
    print("Regra PEMDAS: Parênteses > Expoente > Mult/Div > Soma/Sub.")
    print("Strings também usam operadores (+ para juntar, * para repetir).")
    print("-" * 80)
    
    # Baseado nos Exemplos 6 e 7 do Glossário
    codigo = """# Precedência Matemática
res1 = 2 + 3 * 4        # Multiplicação vence: 2 + 12 = 14
res2 = (2 + 3) * 4      # Parênteses vencem: 5 * 4 = 20
print(f"Sem parênteses: {res1} | Com parênteses: {res2}")

# Operadores com Texto (Strings)
nome = "Profe" + " " + "Berssa"  # Concatenação (Juntar)
linha = "-" * 30                 # Repetição (Multiplicar texto)

print(linha)
print(nome)
print(linha)

# Operador 'in' (Verificação de pertinência)
print("Python" in "Curso de Python")  # True"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(2)
    print("   ↳ CÁLCULO: 3*4=12, depois 2+12=14")
    
    executar_linha(3)
    print("   ↳ CÁLCULO: (2+3)=5, depois 5*4=20")
    
    executar_linha(4)
    print("   ↳ SAÍDA: Sem parênteses: 14 | Com parênteses: 20")
    
    executar_linha(7)
    print("   ↳ STRING: 'Profe' + ' ' + 'Berssa' -> 'Profe Berssa'")
    
    executar_linha(8)
    print("   ↳ STRING: '-' repetido 30 vezes.")
    
    executar_linha(10); executar_linha(11); executar_linha(12)
    print("   ↳ SAÍDA VISUAL: Linhas separadoras e o nome no meio.")
    
    executar_linha(15)
    print("   ↳ LÓGICA: O texto 'Python' está dentro da frase? Sim -> True")
    
    esperar()

# ==============================================================================
# TÓPICO 6: EXEMPLO INTEGRADOR (DESCONTO)
# ==============================================================================
def desafio_desconto():
    limpar_tela()
    print("🔹 DESAFIO FINAL: SIMULADOR DE DESCONTO")
    print("Integra: Aritmética, Relacional, Lógico e Condicional.")
    print("-" * 80)
    
    # Exemplo 10 do Glossário
    codigo_ref = """# Regra:
# - Se levar 10+ unidades E for VIP: 20% desconto
# - Se levar 10+ unidades OU for VIP: 10% desconto
# - Caso contrário: 0% desconto

qtd = int(input("Quantidade: "))
vip = input("É VIP? (s/n): ") == "s"  # Gera True ou False direto

if qtd >= 10 and vip:
    desc = 0.20
elif qtd >= 10 or vip:
    desc = 0.10
else:
    desc = 0.0

total = preco * qtd * (1 - desc)"""
    
    mostrar_codigo_didatico(codigo_ref)
    
    try:
        print("\n⚙️  [Executando Entradas]...")
        # Simulação de preço fixo para focar na lógica dos operadores
        preco = 50.0
        print(f"   (Preço do produto fixado em R$ {preco:.2f} para teste)")
        
        qtd = int(input("   Digite a Quantidade: "))
        vip_input = input("   Cliente é VIP? (s/n): ").lower()
        vip = (vip_input == "s") # Operador relacional gerando booleano
        
        print(f"\n   ↳ MEMÓRIA: qtd={qtd}, vip={vip}")
        
        print("\n⚙️  [Analisando Regras de Negócio]...")
        time.sleep(1)
        
        # Lógica de decisão
        if qtd >= 10 and vip:
            print("   ✅ Condição (qtd >= 10 AND vip) Verdadeira -> 20% OFF")
            desc = 0.20
        elif qtd >= 10 or vip:
            print("   ✅ Condição (qtd >= 10 OR vip) Verdadeira -> 10% OFF")
            desc = 0.10
        else:
            print("   ✅ Nenhuma condição atendida -> 0% OFF")
            desc = 0.0
            
        # Cálculo aritmético final
        subtotal = preco * qtd
        valor_desc = subtotal * desc
        total = subtotal - valor_desc
        
        print("-" * 40)
        print(f"   Subtotal:   R$ {subtotal:.2f}")
        print(f"   Desconto: - R$ {valor_desc:.2f} ({desc*100:.0f}%)")
        print(f"   TOTAL:      R$ {total:.2f}")
        print("-" * 40)
            
    except ValueError:
        print("\n❌ ERRO: Digite um número inteiro válido para a quantidade.")
        
    esperar()

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO DE OPERADORES (GLOSSÁRIO 04)".center(80))
        print("=" * 80)
        print("1. Atribuição Simples e Composta (=, +=, -=)")
        print("2. Operadores Aritméticos (+, -, /, //, %, **)")
        print("3. Operadores Relacionais (Comparação)")
        print("4. Operadores Lógicos (And, Or, Not)")
        print("5. Precedência e Operadores de Texto")
        print("6. Desafio Integrador: Simulador de Desconto")
        print("0. Sair")
        print("=" * 80)
        
        opcao = input("Escolha o tópico para revisar: ")
        
        if opcao == '1': atribuicao()
        elif opcao == '2': aritmeticos()
        elif opcao == '3': relacionais()
        elif opcao == '4': logicos()
        elif opcao == '5': precedencia_strings()
        elif opcao == '6': desafio_desconto()
        elif opcao == '0':
            print("\nEncerrando laboratório... Pratique a precedência! 👋")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()