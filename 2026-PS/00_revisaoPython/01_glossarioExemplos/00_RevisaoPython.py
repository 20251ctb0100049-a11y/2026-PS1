"""""
==============================================================================
ARQUIVO: 00_RevisaoPython.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo para revisão dos fundamentos de Python.
    Baseado integralmente no "Glossário 01 - Linguagem Python".

==============================================================================
"""

import sys
import time
import math
import random

def limpar_tela():
    """Limpa visualmente o terminal para focar na explicação atual."""
    print("\n" * 5)
    print("=" * 80)

def esperar():
    """Pausa para leitura."""
    input("\n[Pressione ENTER para continuar...]")

def mostrar_codigo_didatico(codigo):
    """
    Exibe o código com numeração de linhas e destaca os comentários didáticos.
    """
    print("\n📄 CÓDIGO EM ANÁLISE (Leia os comentários #):")
    print("-" * 80)
    linhas = codigo.strip().split('\n')
    for i, linha in enumerate(linhas):
        # Formata: Número da linha | Conteúdo do código
        print(f"{i+1:02d} | {linha}")
    print("-" * 80)
    print("\n▶️  INICIANDO EXECUÇÃO PASSO A PASSO...\n")
    time.sleep(1.5) # Tempo para o aluno ler o código antes de executar
    return linhas

def executar_linha(numero_linha, atraso=1.0):
    """Simula o processamento linha a linha."""
    print(f"⚙️  [Lendo Linha {numero_linha:02d}]...", end="\r")
    time.sleep(atraso)
    print(f"✅ [Executado Linha {numero_linha:02d}]   ")

# ==============================================================================
# TÓPICO 1: CONCEITOS FUNDAMENTAIS
# ==============================================================================
def fundamentos_python():
    limpar_tela()
    print("🔹 TÓPICO 1: CONCEITOS FUNDAMENTAIS (História & Filosofia)")
    print("-" * 80)
    
    print("📜 RESUMO DO GLOSSÁRIO:")
    print("• Definição: Linguagem de Alto Nível (próxima da humana).")
    print("• Criação: Guido van Rossum (1991), fã de 'Monty Python'.")
    print("• Analogia: 'Como escrever uma receita de bolo em português claro'.")
    print("-" * 80)

    # Código com comentários didáticos
    codigo = """import this  # Comando especial (Easter Egg) que exibe a filosofia do Python
# O Zen of Python define regras de design como 'Simples é melhor que complexo'"""
    
    mostrar_codigo_didatico(codigo)
    
    executar_linha(1, atraso=1.5)
    print("\n>>> SAÍDA REAL DO CONSOLE (Princípios Chave):")
    print("   * Beautiful is better than ugly.")
    print("   * Explicit is better than implicit.")
    print("   * Simple is better than complex.")
    print("   * Readability counts (Legibilidade conta).")
    
    print("\n🌍 ÁREAS DE APLICAÇÃO (Glossário):")
    print("   1. Web (Django/Flask)      2. Data Science (Pandas)")
    print("   3. IA (TensorFlow)         4. Automação & Scripts")
    
    esperar()

# ==============================================================================
# TÓPICO 2: SINTAXE E VERSÕES
# ==============================================================================
def sintaxe_versoes():
    limpar_tela()
    print("🔹 TÓPICO 2: SINTAXE, VERSÕES E ERROS COMUNS")
    
    print("\n🥊 COMPARAÇÃO (Glossário):")
    print("   C: Exige main(), chaves {}, ponto-e-vírgula ; e compilação.")
    print("   Python: Direto, indentado e interpretado linha a linha.")
    
    # Código demonstrando sintaxe e erros comuns
    codigo = """print("Hello, World!")  # Função print() exibe texto na tela. Aspas definem Texto.

# --- ERROS COMUNS CITADOS NO GLOSSÁRIO ---
# Print("Erro")   # Erro! Python é 'Case Sensitive' (maiusculas importam).
# print "Erro"    # Erro! Sintaxe do Python 2 (obsoleto desde 2020)."""
    
    mostrar_codigo_didatico(codigo)
    
    # Execução Linha 1
    executar_linha(1)
    print("   ↳ SAÍDA: Hello, World!")
    
    print("\n🚫 ANÁLISE DE ERROS (Linhas 4 e 5 Comentadas):")
    print("   Linha 04: 'Print' com P maiúsculo não existe.")
    print("   Linha 05: Falta parênteses (). Sempre use Python 3!")
    
    esperar()

# ==============================================================================
# TÓPICO 3: VARIÁVEIS E TIPOS
# ==============================================================================
def variaveis_tipos():
    limpar_tela()
    print("🔹 TÓPICO 3: VARIÁVEIS E TIPAGEM DINÂMICA")
    print("Conceito: Não precisamos declarar o tipo (int, float). O Python infere.")
    
    # Código com comentários explicativos sobre tipos
    codigo = """nome = "Profe. Berssa"  # Variável tipo String (str) -> Texto
idade = 25              # Variável tipo Integer (int) -> Número Inteiro
altura = 1.75           # Variável tipo Float (float) -> Número Decimal
dev = True              # Variável tipo Boolean (bool) -> Verdadeiro/Falso

# f-strings (f"...") permitem inserir variáveis diretamente no texto
print(f"{nome} tem {idade} anos.")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    print("   ↳ MEMÓRIA: Criado espaço 'nome' com valor texto.")
    
    executar_linha(2)
    print("   ↳ MEMÓRIA: Criado espaço 'idade' com valor numérico inteiro.")
    
    executar_linha(3)
    print("   ↳ MEMÓRIA: Criado espaço 'altura' com valor numérico decimal.")
    
    executar_linha(4)
    print("   ↳ MEMÓRIA: Criado espaço 'dev' com valor lógico.")
    
    executar_linha(7) # Pula as linhas vazias/comentários
    nome = "Profe. Berssa"; idade = 25
    print(f"   ↳ SAÍDA: {nome} tem {idade} anos.")
    
    esperar()

# ==============================================================================
# TÓPICO 4: MATEMÁTICA E BIBLIOTECAS
# ==============================================================================
def matematica_libs():
    limpar_tela()
    print("🔹 TÓPICO 4: MATEMÁTICA E BIBLIOTECAS (Baterias Inclusas)")
    
    # Exemplo integrando Math e Random do Glossário
    codigo = """import math    # Importa funções matemáticas avançadas
import random  # Importa gerador de números aleatórios

# input() recebe dados do teclado (sempre como texto)
# float() converte esse texto para número decimal
num = float(input("Digite um número: "))

raiz = math.sqrt(num)        # Calcula raiz quadrada usando a lib math
dado = random.randint(1, 6)  # Gera aleatório entre 1 e 6

print(f"Raiz: {raiz:.2f} | Dado: {dado}")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1); executar_linha(2)
    print("   ↳ SISTEMA: Bibliotecas 'math' e 'random' carregadas.")
    
    executar_linha(6)
    try:
        num = float(input("   ↳ AÇÃO USUÁRIO (Digite ex: 144): "))
    except ValueError:
        num = 144.0
        print("   (Valor inválido, assumindo 144.0)")
        
    executar_linha(8)
    raiz = math.sqrt(num)
    print(f"   ↳ CÁLCULO: Raiz de {num} = {raiz}")
    
    executar_linha(9)
    dado = random.randint(1, 6)
    print(f"   ↳ SORTEIO: Número gerado foi {dado}")
    
    executar_linha(11)
    print(f"   ↳ SAÍDA: Raiz: {raiz:.2f} | Dado: {dado}")
    
    esperar()

# ==============================================================================
# TÓPICO 5: CONTROLE DE FLUXO
# ==============================================================================
def controle_fluxo():
    limpar_tela()
    print("🔹 TÓPICO 5: CONDICIONAIS (Decisões)")
    print("Nota: A indentação (espaço no início) define o que está dentro do IF.")
    
    codigo = """idade = int(input("Sua idade: "))  # Converte entrada para Inteiro

if idade >= 18:           # SE idade for maior ou igual a 18:
    print("Maior de idade")   # Execute isso (está indentado)
else:                     # SENÃO (caso contrário):
    print("Menor de idade")   # Execute aquilo"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    try:
        idade = int(input("   ↳ AÇÃO USUÁRIO (Digite idade): "))
    except:
        return

    executar_linha(3)
    print(f"   ↳ TESTE LÓGICO: {idade} >= 18? -> {idade >= 18}")
    
    if idade >= 18:
        print("   ↳ CAMINHO VERDADEIRO (Entra no IF):")
        executar_linha(4)
        print("   ↳ SAÍDA: Maior de idade")
    else:
        print("   ↳ CAMINHO FALSO (Vai para o ELSE):")
        executar_linha(6)
        executar_linha(7)
        print("   ↳ SAÍDA: Menor de idade")
        
    esperar()

# ==============================================================================
# TÓPICO 6: LISTAS E FUNÇÕES
# ==============================================================================
def listas_funcoes():
    limpar_tela()
    print("🔹 TÓPICO 6: LISTAS E FUNÇÕES")
    
    codigo = """# Definição de Função: Reutiliza código
def saudacao(nome):
    return f"Olá {nome}"  # Retorna o texto formatado

frutas = ["Maçã", "Uva"]  # Lista: Coleção ordenada de dados
frutas.append("Banana")   # append() adiciona item ao final

# Loop FOR: Repete para cada item da lista
for f in frutas:
    print(saudacao(f))    # Chama a função para cada fruta"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(2); executar_linha(3)
    def saudacao(nome): return f"Olá {nome}"
    print("   ↳ MEMÓRIA: Função 'saudacao' aprendida pelo sistema.")
    
    executar_linha(5)
    frutas = ["Maçã", "Uva"]
    print(f"   ↳ LISTA: {frutas}")
    
    executar_linha(6)
    frutas.append("Banana")
    print(f"   ↳ LISTA (após append): {frutas}")
    
    print("\n🔄 INICIANDO LOOP FOR (Linhas 9 e 10):")
    for f in frutas:
        time.sleep(0.5)
        print(f"   ↳ ITEM ATUAL: '{f}' -> Chamando saudacao() -> SAÍDA: {saudacao(f)}")
        
    esperar()

# ==============================================================================
# TÓPICO 7: DESAFIO INTEGRADOR (IMC)
# ==============================================================================
def desafio_imc():
    limpar_tela()
    print("🔹 DESAFIO FINAL: CALCULADORA DE IMC")
    print("Integração: Variáveis, Input, Math, Lógica e Decisão.")
    print("-" * 80)
    
    # Código completo com comentários explicativos
    codigo_ref = """# 1. Entrada de Dados
peso = float(input("Peso (kg): "))     # Lê e converte para decimal
altura = float(input("Altura (m): "))  # Lê e converte para decimal

# 2. Processamento (Cálculo)
imc = peso / (altura ** 2)             # ** significa potência (ao quadrado)

# 3. Saída Formatada
print(f"IMC: {imc:.1f}")               # :.1f arredonda para 1 casa decimal

# 4. Lógica de Classificação (Decisão Encadeada)
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:                         # elif = else if (senão se)
    print("Peso normal")
else:                                  # Se nada acima for verdade
    print("Sobrepeso ou Obesidade")"""
    
    mostrar_codigo_didatico(codigo_ref)
    
    try:
        print("\n⚙️  [Executando Bloco 1: Entradas]...")
        peso = float(input("   Peso (kg): "))
        altura = float(input("   Altura (m): "))
        
        print("\n⚙️  [Executando Bloco 2: Cálculo]...")
        time.sleep(0.5)
        imc = peso / (altura ** 2)
        
        print(f"⚙️  [Executando Bloco 3: Saída] -> IMC: {imc:.1f}")
        
        print("\n⚙️  [Executando Bloco 4: Lógica de Decisão]...")
        time.sleep(0.5)
        
        if imc < 18.5:
            print("   ✅ Condição (imc < 18.5) Verdadeira -> Abaixo do peso")
        elif imc < 25:
            print("   ✅ Condição (imc < 25) Verdadeira -> Peso normal")
        else:
            print("   ✅ Caiu no ELSE -> Sobrepeso ou Obesidade")
            
    except ValueError:
        print("❌ Erro: Digite apenas números (use ponto para decimais).")
        
    esperar()

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO PYTHON (GLOSSÁRIO 01)".center(80))
        print("=" * 80)
        print("1. Fundamentos (História, Filosofia, Áreas)")
        print("2. Sintaxe, Versões e Case Sensitivity")
        print("3. Variáveis e Tipagem Dinâmica")
        print("4. Matemática e Bibliotecas")
        print("5. Controle de Fluxo (Condicionais)")
        print("6. Listas, Loops e Funções")
        print("7. DESAFIO INTEGRADOR: IMC")
        print("0. Sair")
        print("=" * 80)
        
        opcao = input("Escolha o tópico para revisar: ")
        
        if opcao == '1': fundamentos_python()
        elif opcao == '2': sintaxe_versoes()
        elif opcao == '3': variaveis_tipos()
        elif opcao == '4': matematica_libs()
        elif opcao == '5': controle_fluxo()
        elif opcao == '6': listas_funcoes()
        elif opcao == '7': desafio_imc()
        elif opcao == '0': break
        else: print("Opção inválida!"); time.sleep(1)

if __name__ == "__main__":
    menu_principal()