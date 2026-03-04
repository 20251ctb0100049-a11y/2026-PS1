# -*- coding: utf-8 -*-
"""
==============================================================================
ARQUIVO: 08_SubRotinas.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo sobre Sub-rotinas (Funções).
    Baseado integralmente no "Glossário 09 - Sub-rotinas".

CONTEÚDO PROGRAMÁTICO:
    1. Conceito: Blocos de código reutilizáveis (Analogia da Receita/Máquina).
    2. Sintaxe: def, parâmetros e a chamada da função.
    3. Parâmetros vs Argumentos: Quem recebe vs Quem envia.
    4. O Poder do Return: Diferença vital entre return e print.
    5. Escopo: Variáveis locais (dentro da função) vs globais.
    6. Parâmetros Opcionais: Valores padrão (default).
    7. Exemplo Integrador: Calculadora Modular.

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

def executar_linha(numero_linha, atraso=0.8):
    """Simula o processamento da linha."""
    print(f"⚙️  [Lendo Linha {numero_linha:02d}]...", end="\r")
    time.sleep(atraso)
    print(f"✅ [Executado Linha {numero_linha:02d}]   ")

# ==============================================================================
# TÓPICO 1: DEFINIÇÃO E CHAMADA
# ==============================================================================
def conceito_basico():
    limpar_tela()
    print("🔹 TÓPICO 1: O QUE SÃO FUNÇÕES?")
    print("-" * 80)
    print("Funções são blocos de código que realizam uma tarefa específica.")
    print("Elas só funcionam quando são CHAMADAS (invocadas).")
    print("Analogia: Ensinar um cachorro o comando 'Senta'.")
    print("   - def senta(): ... (Ensinar o truque)")
    print("   - senta() ... (Mandar fazer)")
    print("-" * 80)

    # Baseado no Exemplo 1 do Glossário
    codigo = """# 1. Definição (O Python aprende, mas não executa agora)
def saudacao():
    print("Olá! Bem-vindo ao sistema.")
    print("--- Fim da função ---")

# 2. Programa Principal
print("Início do programa")
saudacao()  # Chamada 1
print("Meio do programa")
saudacao()  # Chamada 2 (Reuso)"""

    mostrar_codigo_didatico(codigo)

    executar_linha(2)
    print("   ↳ MEMÓRIA: Função 'saudacao' registrada (aprendida).")
    
    executar_linha(7)
    print("   ↳ SAÍDA: Início do programa")
    
    executar_linha(8)
    print("   ↳ FLUXO: Saltando para a linha 02 (dentro da função)...")
    time.sleep(1)
    
    # Dentro da função
    executar_linha(3)
    print("   ↳ SAÍDA: Olá! Bem-vindo ao sistema.")
    executar_linha(4)
    print("   ↳ SAÍDA: --- Fim da função ---")
    print("   ↳ FLUXO: Retornando para a linha 08...")
    
    executar_linha(9)
    print("   ↳ SAÍDA: Meio do programa")
    
    executar_linha(10)
    print("   ↳ FLUXO: Saltando novamente para a linha 02...")
    time.sleep(1)
    
    # Dentro da função de novo
    executar_linha(3); executar_linha(4)
    print("   ↳ SAÍDA: (Mensagens repetidas)")
    
    esperar()

# ==============================================================================
# TÓPICO 2: PARÂMETROS E ARGUMENTOS
# ==============================================================================
def parametros_argumentos():
    limpar_tela()
    print("🔹 TÓPICO 2: PARÂMETROS (DADOS DE ENTRADA)")
    print("-" * 80)
    print("Podemos passar informações para a função trabalhar.")
    print("   - Parâmetro: Variável na definição (Ex: nome).")
    print("   - Argumento: Valor real enviado (Ex: 'Ana').")
    print("-" * 80)
    
    # Baseado no Exemplo 2 do Glossário
    codigo = """def personalizar(nome, idade):
    # 'nome' e 'idade' só existem aqui dentro!
    print(f"Ficha: {nome} tem {idade} anos.")

# Chamando com argumentos posicionais
personalizar("Ana", 25)

# Chamando com argumentos nomeados (ordem não importa)
personalizar(idade=40, nome="Carlos")"""

    mostrar_codigo_didatico(codigo)

    executar_linha(1)
    print("   ↳ MEMÓRIA: Função 'personalizar' aprendida.")
    
    print("\n🔄 [CHAMADA 1]")
    executar_linha(5)
    print("   ↳ ENVIO: 'Ana' -> nome, 25 -> idade")
    executar_linha(3)
    print("   ↳ SAÍDA: Ficha: Ana tem 25 anos.")
    
    print("\n🔄 [CHAMADA 2]")
    executar_linha(8)
    print("   ↳ ENVIO: nome='Carlos', idade=40 (Mapeamento direto)")
    executar_linha(3)
    print("   ↳ SAÍDA: Ficha: Carlos tem 40 anos.")
    
    esperar()

# ==============================================================================
# TÓPICO 3: RETURN VS PRINT
# ==============================================================================
def return_vs_print():
    limpar_tela()
    print("🔹 TÓPICO 3: RETURN VS PRINT (CRUCIAL!)")
    print("-" * 80)
    print("PRINT apenas MOSTRA na tela (o valor se perde).")
    print("RETURN DEVOLVE o valor para quem chamou (pode ser salvo em variável).")
    print("⚠️ Se a função não tem return, ela devolve 'None' (Vazio).")
    print("-" * 80)
    
    # Baseado no Exemplo 3 e 4 do Glossário
    codigo = """# Função COM retorno (A máquina que produz algo)
def somar_util(a, b):
    resultado = a + b
    return resultado  # Devolve o valor

# Função SEM retorno (A máquina que só faz barulho)
def somar_inutil(a, b):
    print(f"Soma: {a + b}")
    # Não tem return (retorna None implicitamente)

# Teste 1: Usando o retorno
x = somar_util(10, 20)  # x recebe 30
print(f"O triplo da soma é {x * 3}")

# Teste 2: Tentando usar função sem retorno
y = somar_inutil(10, 20) # y recebe None!
# print(y * 3)  <-- ERRO! Não dá pra multiplicar 'None'"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(2); executar_linha(7)
    
    print("\n🧪 [TESTE 1 - COM RETURN]")
    executar_linha(12)
    print("   ↳ FLUXO: Entra em 'somar_util'. Calcula 10+20.")
    print("   ↳ RETURN: O valor 30 volta e é guardado em 'x'.")
    executar_linha(13)
    print("   ↳ CÁLCULO: 30 * 3 = 90")
    print("   ↳ SAÍDA: O triplo da soma é 90")
    
    print("\n🧪 [TESTE 2 - SEM RETURN]")
    executar_linha(16)
    print("   ↳ FLUXO: Entra em 'somar_inutil'.")
    print("   ↳ SAÍDA (dentro da função): Soma: 30")
    print("   ↳ RETURN: Nada foi retornado. 'y' recebe None.")
    
    executar_linha(17)
    print("   ↳ ANÁLISE: Se descomentar a linha 17, daria erro:")
    print("   ❌ TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'")
    
    esperar()

# ==============================================================================
# TÓPICO 4: ESCOPO DE VARIÁVEIS
# ==============================================================================
def escopo():
    limpar_tela()
    print("🔹 TÓPICO 4: ESCOPO (LOCAL VS GLOBAL)")
    print("-" * 80)
    print("Variáveis criadas DENTRO da função são invisíveis fora dela.")
    print("Isso evita que uma função bagunce os dados da outra.")
    print("-" * 80)
    
    # Baseado no Exemplo 5 do Glossário
    codigo = """def teste_escopo():
    segredo = 1234  # Variável LOCAL
    print(f"Dentro: {segredo}")

teste_escopo()

# Tentando acessar fora
# print(segredo)  # ERRO! 'segredo' não existe aqui."""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    
    print("\n🔄 [CHAMADA DA FUNÇÃO]")
    executar_linha(5)
    executar_linha(2)
    print("   ↳ MEMÓRIA: 'segredo' criada temporariamente.")
    executar_linha(3)
    print("   ↳ SAÍDA: Dentro: 1234")
    print("   ↳ MEMÓRIA: Função acabou. 'segredo' foi destruída.")
    
    print("\n🔄 [FORA DA FUNÇÃO]")
    executar_linha(8)
    print("   ↳ ANÁLISE: A linha 8 causaria 'NameError'.")
    print("   🛡️  Isso é segurança! O que acontece na função, fica na função.")
    
    esperar()

# ==============================================================================
# TÓPICO 5: PARÂMETROS OPCIONAIS
# ==============================================================================
def parametros_opcionais():
    limpar_tela()
    print("🔹 TÓPICO 5: PARÂMETROS OPCIONAIS (DEFAULT)")
    print("-" * 80)
    print("Você pode definir valores padrão. Se o usuário não passar, usa o padrão.")
    print("-" * 80)
    
    # Baseado no Exemplo 6 do Glossário
    codigo = """def potencia(base, expoente=2):
    return base ** expoente

# 1. Passando só a base (Usa expoente padrão = 2)
res1 = potencia(5)
print(f"5 ao quadrado: {res1}")

# 2. Passando tudo (Ignora o padrão)
res2 = potencia(5, 3)
print(f"5 ao cubo: {res2}")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    
    print("\n🔄 [CASO 1: SEM SEGUNDO ARGUMENTO]")
    executar_linha(5)
    print("   ↳ CHAMADA: potencia(5). 'expoente' assume valor 2.")
    print("   ↳ CÁLCULO: 5 ** 2 = 25.")
    executar_linha(6)
    print("   ↳ SAÍDA: 5 ao quadrado: 25")
    
    print("\n🔄 [CASO 2: COM TODOS ARGUMENTOS]")
    executar_linha(9)
    print("   ↳ CHAMADA: potencia(5, 3). 'expoente' assume valor 3.")
    print("   ↳ CÁLCULO: 5 ** 3 = 125.")
    executar_linha(10)
    print("   ↳ SAÍDA: 5 ao cubo: 125")
    
    esperar()

# ==============================================================================
# TÓPICO 6: DESAFIO INTEGRADOR (CALCULADORA)
# ==============================================================================
def desafio_calculadora():
    limpar_tela()
    print("🔹 DESAFIO FINAL: CALCULADORA MODULAR")
    print("Integra: Definição, Parâmetros, Return e Menu.")
    print("-" * 80)
    
    # Exemplo 10 do Glossário (adaptado para estrutura modular)
    codigo_ref = """# Definindo as operações (Máquinas)
def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0: return "Erro (Div Zero)"
    return a / b

# Programa Principal (Interface)
print("--- Calc Funções ---")
n1 = float(input("Num 1: "))
n2 = float(input("Num 2: "))
op = input("Operação (+, -, *, /): ")

if op == "+": res = somar(n1, n2)
elif op == "-": res = subtrair(n1, n2)
elif op == "*": res = multiplicar(n1, n2)
elif op == "/": res = dividir(n1, n2)
else: res = "Opção inválida"

print(f"Resultado: {res}")"""
    
    mostrar_codigo_didatico(codigo_ref)
    
    # Execução simulada real
    try:
        # Definições reais
        def somar(a, b): return a + b
        def subtrair(a, b): return a - b
        def multiplicar(a, b): return a * b
        def dividir(a, b): return "Erro (Div Zero)" if b == 0 else a / b
        
        executar_linha(2); executar_linha(3)
        executar_linha(4); executar_linha(5)
        print("   ↳ SISTEMA: 4 funções carregadas na memória.")
        
        print("\n⚙️  [Entrada de Dados]...")
        n1 = float(input("   Num 1: "))
        n2 = float(input("   Num 2: "))
        op = input("   Operação (+, -, *, /): ")
        
        print(f"\n⚙️  [Chamando a função especialista para '{op}']...")
        time.sleep(1)
        
        res = 0
        if op == "+": 
            print("   ↳ CHAMADA: somar(n1, n2)")
            res = somar(n1, n2)
        elif op == "-": 
            print("   ↳ CHAMADA: subtrair(n1, n2)")
            res = subtrair(n1, n2)
        elif op == "*": 
            print("   ↳ CHAMADA: multiplicar(n1, n2)")
            res = multiplicar(n1, n2)
        elif op == "/": 
            print("   ↳ CHAMADA: dividir(n1, n2)")
            res = dividir(n1, n2)
        else:
            res = "Opção inválida"
            
        print("-" * 30)
        print(f"Resultado Final: {res}")
        print("-" * 30)
            
    except ValueError:
        print("\n❌ ERRO: Digite números válidos.")
        
    esperar()

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO DE FUNÇÕES (GLOSSÁRIO 09)".center(80))
        print("=" * 80)
        print("1. Conceito Básico (Definição e Chamada)")
        print("2. Parâmetros e Argumentos (Passando dados)")
        print("3. Return vs Print (O conceito mais importante)")
        print("4. Escopo (Local vs Global)")
        print("5. Parâmetros Opcionais (Valores padrão)")
        print("6. Desafio Integrador: Calculadora Modular")
        print("0. Sair")
        print("=" * 80)
        
        opcao = input("\nEscolha o tópico para revisar: ")
        
        if opcao == '1': conceito_basico()
        elif opcao == '2': parametros_argumentos()
        elif opcao == '3': return_vs_print()
        elif opcao == '4': escopo()
        elif opcao == '5': parametros_opcionais()
        elif opcao == '6': desafio_calculadora()
        elif opcao == '0':
            print("\nEncerrando laboratório... Dividir para conquistar! 👋")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()