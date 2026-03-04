# -*- coding: utf-8 -*-
"""
==============================================================================
ARQUIVO: 02_TiposVariaveis.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo sobre Variáveis, Tipos de Dados e Conversão.
    Baseado integralmente no "Glossário 03 - Tipos de Dados e Variáveis".

CONTEÚDO PROGRAMÁTICO:
    1. Conceito de Variável (A Caixa Etiquetada) e Tipos Primitivos.
    2. Tipagem Dinâmica e a função type().
    3. Regras de Nomeação e Convenções (PEP 8).
    4. Conversão de Tipos (Casting) e Valores Truthy/Falsy.
    5. Operações com Strings e Constantes.
    6. Erros Comuns (TypeError, ValueError, = vs ==).
    7. Exemplo Integrador: Cadastro de Produto.

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
# TÓPICO 1: CONCEITO E TIPOS BÁSICOS
# ==============================================================================
def conceito_tipos():
    limpar_tela()
    print("🔹 TÓPICO 1: O QUE SÃO VARIÁVEIS E TIPOS?")
    print("-" * 80)
    print("Definição: Espaços na memória para guardar dados.")
    print("\n🎯 ANALOGIA DO GLOSSÁRIO (As Caixas):")
    print("   'Imagine variáveis como caixas etiquetadas em um depósito.'")
    print("   - Etiqueta = Nome da variável")
    print("   - Conteúdo = Valor")
    print("   - Tipo da caixa = Tipo de dado (int, float, etc.)")
    print("-" * 80)

    # Exemplo cobrindo os 4 tipos primitivos (Exemplos 1 e 2 do Glossário)
    codigo = """# Criando variáveis dos 4 tipos básicos (Tipagem Dinâmica):
nome = "Profe. Berssa"  # str (Texto)
idade = 25              # int (Inteiro)
altura = 1.75           # float (Decimal/Ponto Flutuante)
ativo = True            # bool (Booleano/Lógico)

print(f"{nome} tem {idade} anos.")"""

    mostrar_codigo_didatico(codigo)

    executar_linha(2)
    print("   ↳ MEMÓRIA: Criada caixa 'nome' contendo texto.")

    executar_linha(3)
    print("   ↳ MEMÓRIA: Criada caixa 'idade' contendo número inteiro.")

    executar_linha(4)
    print("   ↳ MEMÓRIA: Criada caixa 'altura' contendo número decimal.")

    executar_linha(5)
    print("   ↳ MEMÓRIA: Criada caixa 'ativo' com valor lógico Verdadeiro.")
    
    executar_linha(7)
    print("   ↳ SAÍDA: Profe. Berssa tem 25 anos.")
    
    esperar()

# ==============================================================================
# TÓPICO 2: TIPAGEM DINÂMICA E TYPE()
# ==============================================================================
def tipagem_dinamica():
    limpar_tela()
    print("🔹 TÓPICO 2: TIPAGEM DINÂMICA E REATRIBUIÇÃO")
    print("-" * 80)
    print("Python descobre o tipo sozinho. E você pode mudar o tipo da variável!")
    print("Use a função type() para investigar o tipo atual.")
    print("-" * 80)
    
    # Baseado no Exemplo 6 do Glossário
    codigo = """dado = 10               # Começa como Inteiro
print(type(dado))

dado = "Texto"          # Agora virou String (reatribuição)
print(type(dado))

dado = 3.14             # Agora virou Float
print(type(dado))"""

    mostrar_codigo_didatico(codigo)

    executar_linha(1)
    print("   ↳ MEMÓRIA: 'dado' vale 10.")
    executar_linha(2)
    print("   ↳ SAÍDA: <class 'int'>")
    
    print("\n   🔄 [MUDANÇA DE TIPO OCORRENDO...]")
    executar_linha(4)
    print("   ↳ MEMÓRIA: 'dado' agora vale 'Texto'. O tipo mudou!")
    executar_linha(5)
    print("   ↳ SAÍDA: <class 'str'>")
    
    print("\n   🔄 [MUDANÇA DE TIPO OCORRENDO...]")
    executar_linha(7)
    print("   ↳ MEMÓRIA: 'dado' agora vale 3.14.")
    executar_linha(8)
    print("   ↳ SAÍDA: <class 'float'>")
    
    print("\n⚠️  ALERTA: Mudar tipos pode confundir. Use nomes descritivos!")
    esperar()

# ==============================================================================
# TÓPICO 3: REGRAS DE NOMEAÇÃO
# ==============================================================================
def regras_nomeacao():
    limpar_tela()
    print("🔹 TÓPICO 3: REGRAS DE NOMEAÇÃO E BOAS PRÁTICAS")
    print("-" * 80)
    
    print("✅ PERMITIDO:")
    print("   - Letras, números e underline (_).")
    print("   - Começar com letra ou _.")
    print("   - Ex: nota_1, _total, nome_completo")
    
    print("\n❌ PROIBIDO (Gera SyntaxError):")
    print("   - Começar com número (1nome).")
    print("   - Espaços (nome aluno).")
    print("   - Palavras reservadas (if, for, class).")
    
    print("\n📏 CONVENÇÃO PEP 8 (Padrão Python):")
    print("   - Variáveis: snake_case (tudo_minusculo_com_underline).")
    print("   - Constantes: MAIÚSCULAS (PI, MAX_TENTATIVAS).")
    print("-" * 80)
    
    codigo = """# Exemplo de Boas Práticas:
nota_final = 8.5      # ✅ snake_case (fácil de ler)
MAX_ALUNOS = 35       # ✅ Constante (indica que não deve mudar)

# x = 10              # ⚠️ Ruim (pouco descritivo)
# 1nota = 5           # ❌ Erro de Sintaxe!"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(2)
    print("   ↳ OK: Variável criada seguindo padrão.")
    executar_linha(3)
    print("   ↳ OK: Constante definida.")
    
    print("\n💡 DICA: Código é lido mais vezes do que é escrito. Facilite a leitura!")
    esperar()

# ==============================================================================
# TÓPICO 4: CONVERSÃO (CASTING) E BOOLEANOS
# ==============================================================================
def casting_booleanos():
    limpar_tela()
    print("🔹 TÓPICO 4: CONVERSÃO DE TIPOS E VALORES LÓGICOS")
    print("-" * 80)
    
    print("Às vezes precisamos forçar a mudança de tipo (Casting).")
    print("Funções úteis: int(), float(), str(), bool()")
    print("-" * 80)
    
    # Baseado nos Exemplos 4 e 7 do Glossário
    codigo = """# input() sempre retorna TEXTO (str). Precisamos converter!
idade_txt = "25"
idade_num = int(idade_txt)   # Converte "25" para 25

# Cuidado: int() trunca decimais (corta a parte fracionária)
nota = int(9.9)              # Vira 9, não 10!

# Valores Truthy e Falsy (Tudo tem um valor lógico)
v1 = bool(0)                 # 0 é False
v2 = bool(1)                 # 1 (ou qualquer nº != 0) é True
v3 = bool("")                # Texto vazio é False"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(2); executar_linha(3)
    print("   ↳ CONVERSÃO: String '25' virou Inteiro 25.")
    
    executar_linha(6)
    print("   ↳ CUIDADO: int(9.9) resultou em 9 (perdeu o decimal).")
    
    executar_linha(9)
    print("   ↳ LÓGICA: bool(0) -> False")
    
    executar_linha(10)
    print("   ↳ LÓGICA: bool(1) -> True")
    
    executar_linha(11)
    print("   ↳ LÓGICA: bool(\"\") -> False (String vazia)")
    
    esperar()

# ==============================================================================
# TÓPICO 5: STRINGS E ERROS COMUNS
# ==============================================================================
def strings_erros():
    limpar_tela()
    print("🔹 TÓPICO 5: OPERAÇÕES COM TEXTO E ERROS COMUNS")
    print("-" * 80)
    
    # Baseado no Exemplo 5 e Seção de Erros do Glossário
    codigo = """nome = "Python"
# Operações com Strings
print(nome * 3)          # Repetição
print(nome + " 3.12")    # Concatenação (Juntar)

# --- ERROS COMUNS (Simulados) ---
# Erro 1: Somar texto com número
# total = "R$ " + 10     # TypeError! Precisa converter o 10.

# Erro 2: Confundir Atribuição (=) com Comparação (==)
x = 10                   # Guarda 10 em x (Ação)
print(x == 10)           # Pergunta: x é igual a 10? (Retorna True/False)"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    
    executar_linha(3)
    print("   ↳ SAÍDA: PythonPythonPython")
    
    executar_linha(4)
    print("   ↳ SAÍDA: Python 3.12")
    
    print("\n🚫 ANÁLISE DE ERROS:")
    print("   Linha 08 (Comentada): Somar 'Texto' + 10 causa travamento (TypeError).")
    print("   Correção: 'Texto' + str(10)")
    
    executar_linha(11)
    print("   ↳ MEMÓRIA: x recebeu 10.")
    
    executar_linha(12)
    print("   ↳ COMPARAÇÃO: 10 é igual a 10? -> True")
    
    esperar()

# ==============================================================================
# TÓPICO 6: EXEMPLO INTEGRADOR (CADASTRO)
# ==============================================================================
def desafio_cadastro():
    limpar_tela()
    print("🔹 DESAFIO FINAL: CADASTRO DE PRODUTO")
    print("Este programa integra: input, tipos variados, conversão, cálculos e f-strings.")
    print("-" * 80)
    
    # Exemplo 10 do Glossário
    codigo_ref = """# 1. Entrada (Convertendo tipos imediatamente)
nome = input("Produto: ")               # str
qtd = int(input("Quantidade: "))        # int
preco = float(input("Preço: "))         # float

# 2. Processamento
total = qtd * preco

# 3. Saída Formatada
print(f"Item: {nome} | Total: R$ {total:.2f}")"""
    
    mostrar_codigo_didatico(codigo_ref)
    
    try:
        print("\n⚙️  [Executando Entradas]...")
        nome = input("   Digite o Nome do Produto: ")
        
        # Tratamento simples para evitar quebra no teste
        qtd_input = input("   Digite a Quantidade (inteiro): ")
        qtd = int(qtd_input)
        
        preco_input = input("   Digite o Preço (decimal): ")
        preco = float(preco_input)
        
        print("\n⚙️  [Calculando]...")
        time.sleep(0.5)
        total = qtd * preco
        
        print(f"⚙️  [Gerando Relatório]...")
        time.sleep(0.5)
        print("-" * 40)
        print(f"📦 PRODUTO: {nome.upper()}")
        print(f"   Qtd: {qtd} un.")
        print(f"   Preço: R$ {preco:.2f}")
        print(f"   TOTAL: R$ {total:.2f}")
        print("-" * 40)
        
        print(f"\n🔍 VERIFICAÇÃO DE TIPOS (Bastidores):")
        print(f"   'nome' é {type(nome).__name__}")
        print(f"   'qtd' é {type(qtd).__name__}")
        print(f"   'preco' é {type(preco).__name__}")
            
    except ValueError:
        print("\n❌ ERRO: Você digitou texto onde deveria ser número!")
        print("   Lembre-se: int() e float() exigem caracteres numéricos.")
        
    esperar()

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO DE VARIÁVEIS (GLOSSÁRIO 03)".center(80))
        print("=" * 80)
        print("1. Conceito, Analogia das Caixas e 4 Tipos Básicos")
        print("2. Tipagem Dinâmica e type()")
        print("3. Regras de Nomeação e Boas Práticas (PEP 8)")
        print("4. Conversão (Casting) e Booleanos (Truthy/Falsy)")
        print("5. Operações com Strings e Erros Comuns")
        print("6. Exemplo Integrador: Cadastro de Produto")
        print("0. Sair")
        print("=" * 80)
        
        opcao = input("Escolha o tópico para revisar: ")
        
        if opcao == '1': conceito_tipos()
        elif opcao == '2': tipagem_dinamica()
        elif opcao == '3': regras_nomeacao()
        elif opcao == '4': casting_booleanos()
        elif opcao == '5': strings_erros()
        elif opcao == '6': desafio_cadastro()
        elif opcao == '0':
            print("\nEncerrando laboratório... Até a próxima! 👋")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()