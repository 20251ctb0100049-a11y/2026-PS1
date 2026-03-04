# -*- coding: utf-8 -*-
"""
==============================================================================
ARQUIVO: 07_EstruturasRepeticao.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo sobre Estruturas de Repetição (Loops).
    Baseado integralmente no "Glossário 08 - Estruturas de Repetição".

CONTEÚDO PROGRAMÁTICO:
    1. Conceito: Repetir tarefas sem copiar código (Analogia da Playlist vs Encher Tanque).
    2. Loop FOR: Iterando sobre sequências e uso do range().
    3. Loop WHILE: Repetição baseada em condição (Cuidado com Loop Infinito).
    4. Controle de Fluxo: break (Para tudo) e continue (Pula essa).
    5. Recursos Avançados: Loop com else e List Comprehension.
    6. Erros Comuns: Modificar lista enquanto itera e Esquecer incremento.
    7. Exemplo Integrador: Gerador de Tabuada.

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

def executar_linha(numero_linha, atraso=0.5):
    """Simula o processamento da linha."""
    print(f"⚙️  [Lendo Linha {numero_linha:02d}]...", end="\r")
    time.sleep(atraso)
    print(f"✅ [Executado Linha {numero_linha:02d}]   ")

# ==============================================================================
# TÓPICO 1: LOOP FOR E RANGE
# ==============================================================================
def loop_for():
    limpar_tela()
    print("🔹 TÓPICO 1: O LOOP FOR (PARA CADA ITEM...)")
    print("-" * 80)
    print("Use quando você sabe o tamanho da sequência ou quantas vezes repetir.")
    print("Analogia: 'Para cada música na playlist, toque a música'.")
    print("Função range(inicio, fim, passo) cria sequências numéricas.")
    print("-" * 80)

    # Baseado nos Exemplos 1 e 2 do Glossário
    codigo = """frutas = ["Maçã", "Uva"]

# 1. Iterando sobre uma lista
for item in frutas:           # Para cada 'item' na lista 'frutas':
    print(f"Comendo {item}")  # Execute isso

# 2. Usando range() para contar
# range(1, 4) gera: 1, 2, 3 (O último NÃO entra!)
for i in range(1, 4):
    print(f"Contagem: {i}")"""

    mostrar_codigo_didatico(codigo)

    executar_linha(1)
    frutas = ["Maçã", "Uva"]
    
    print("\n🔄 [INÍCIO DO LOOP 1]")
    # Simulação da iteração 1
    executar_linha(4)
    item = "Maçã"
    print(f"   ↳ VARIÁVEL DE CONTROLE: item = '{item}'")
    executar_linha(5)
    print(f"   ↳ SAÍDA: Comendo {item}")
    
    # Simulação da iteração 2
    print("\n🔄 [VOLTA DO LOOP 1]")
    executar_linha(4)
    item = "Uva"
    print(f"   ↳ VARIÁVEL DE CONTROLE: item = '{item}'")
    executar_linha(5)
    print(f"   ↳ SAÍDA: Comendo {item}")
    
    print("\n🔄 [FIM DO LOOP 1] Lista acabou.")
    
    print("\n🔄 [INÍCIO DO LOOP 2 - RANGE]")
    # Loop Range
    for i in range(1, 4):
        executar_linha(9)
        print(f"   ↳ RANGE: i = {i}")
        executar_linha(10)
        print(f"   ↳ SAÍDA: Contagem: {i}")
        if i < 3: print("   (Voltando...)")
        
    print("   (Note que o 4 não foi impresso. O limite superior é exclusivo!)")
    esperar()

# ==============================================================================
# TÓPICO 2: LOOP WHILE
# ==============================================================================
def loop_while():
    limpar_tela()
    print("🔹 TÓPICO 2: O LOOP WHILE (ENQUANTO...)")
    print("-" * 80)
    print("Use quando NÃO sabe quantas vezes vai repetir (depende de algo acontecer).")
    print("Analogia: 'Enquanto o tanque não estiver cheio, continue enchendo'.")
    print("⚠️ CUIDADO: Se a condição nunca for False, cria um LOOP INFINITO!")
    print("-" * 80)
    
    # Baseado nos Exemplos 3 e 6 do Glossário
    codigo = """bateria = 30  # Começamos com 30%

# Enquanto bateria for maior que 0...
while bateria > 0:
    print(f"Bateria: {bateria}% - Usando...")
    bateria -= 10  # Passo CRUCIAL: Modificar a variável de controle!
    # Se esquecer a linha acima, a bateria nunca acaba (Loop Infinito)

print("Celular desligou.")"""

    mostrar_codigo_didatico(codigo)

    executar_linha(1)
    bateria = 30
    
    # Volta 1
    print("\n🔄 [VOLTA 1]")
    executar_linha(4)
    print(f"   ↳ TESTE: {bateria} > 0? Sim.")
    executar_linha(5)
    print(f"   ↳ SAÍDA: Bateria: {bateria}% - Usando...")
    executar_linha(6)
    bateria -= 10
    print(f"   ↳ ATUALIZAÇÃO: bateria agora é {bateria}")
    
    # Volta 2
    print("\n🔄 [VOLTA 2]")
    executar_linha(4)
    print(f"   ↳ TESTE: {bateria} > 0? Sim.")
    executar_linha(5)
    print(f"   ↳ SAÍDA: Bateria: {bateria}% - Usando...")
    executar_linha(6)
    bateria -= 10
    print(f"   ↳ ATUALIZAÇÃO: bateria agora é {bateria}")

    # Volta 3
    print("\n🔄 [VOLTA 3]")
    executar_linha(4)
    print(f"   ↳ TESTE: {bateria} > 0? Sim.")
    executar_linha(5)
    print(f"   ↳ SAÍDA: Bateria: {bateria}% - Usando...")
    executar_linha(6)
    bateria -= 10
    print(f"   ↳ ATUALIZAÇÃO: bateria agora é {bateria}")

    # Fim
    print("\n🔄 [VOLTA FINAL]")
    executar_linha(4)
    print(f"   ↳ TESTE: {bateria} > 0? Não! (False)")
    print("   ↳ AÇÃO: Sai do loop.")
    executar_linha(9)
    print("   ↳ SAÍDA: Celular desligou.")
    
    esperar()

# ==============================================================================
# TÓPICO 3: BREAK E CONTINUE
# ==============================================================================
def break_continue():
    limpar_tela()
    print("🔹 TÓPICO 3: CONTROLE DE FLUXO (BREAK / CONTINUE)")
    print("-" * 80)
    print("break    -> PARA o loop imediatamente (Sai dele).")
    print("continue -> PULA para a próxima volta (Ignora o resto abaixo).")
    print("-" * 80)
    
    # Baseado nos Exemplos 4 e 5 do Glossário
    codigo = """# Exemplo 1: Busca com BREAK
print("--- Buscando 'Alface' ---")
lista = ["Arroz", "Feijão", "Alface", "Carne"]

for item in lista:
    print(f"Verificando: {item}")
    if item == "Alface":
        print("✅ Encontrado! Parando busca.")
        break  # Sai do loop AGORA (não olha 'Carne')

# Exemplo 2: Pular pares com CONTINUE
print("\\n--- Imprimindo Ímpares ---")
for i in range(1, 6):
    if i % 2 == 0:     # Se for par...
        continue       # ...pula pro próximo número (ignora o print abaixo)
    print(f"Número ímpar: {i}")"""

    mostrar_codigo_didatico(codigo)
    
    # Simulação Break
    executar_linha(2)
    executar_linha(3)
    lista = ["Arroz", "Feijão", "Alface", "Carne"]
    
    # Volta 1 e 2 rápidas
    print("\n🔄 [ITERAÇÃO 1 & 2]")
    print("   ↳ Verificando: Arroz... (Não é)")
    print("   ↳ Verificando: Feijão... (Não é)")
    
    # Volta 3
    print("\n🔄 [ITERAÇÃO 3]")
    executar_linha(5)
    print("   ↳ Verificando: Alface")
    executar_linha(7)
    print("   ↳ TESTE: É Alface? Sim!")
    executar_linha(8)
    print("   ↳ SAÍDA: ✅ Encontrado! Parando busca.")
    executar_linha(9)
    print("   ↳ AÇÃO: BREAK acionado. O loop morre aqui. 'Carne' nunca será lida.")
    
    # Simulação Continue
    print("\n" + "-"*30)
    executar_linha(12)
    print("\n🔄 [LOOP RANGE 1 a 5]")
    
    for i in range(1, 4): # Simulando até 3 para não ficar longo
        print(f"\n   [i = {i}]")
        executar_linha(14)
        if i % 2 == 0:
            print(f"   ↳ TESTE: {i} é par? Sim.")
            executar_linha(15)
            print("   ↳ AÇÃO: CONTINUE acionado. Volta para o topo (pula linha 16).")
        else:
            print(f"   ↳ TESTE: {i} é par? Não.")
            executar_linha(16)
            print(f"   ↳ SAÍDA: Número ímpar: {i}")

    print("   (... segue assim até 5)")
    esperar()

# ==============================================================================
# TÓPICO 4: VALIDAÇÃO DE DADOS (WHILE TRUE)
# ==============================================================================
def validacao_while():
    limpar_tela()
    print("🔹 TÓPICO 4: VALIDAÇÃO DE DADOS (PATTERN WHILE TRUE)")
    print("-" * 80)
    print("Muito usado para garantir que o usuário digite o que queremos.")
    print("Cria-se um loop infinito proposital que só quebra (break) se a entrada for válida.")
    print("-" * 80)
    
    # Baseado no Exemplo 6 do Glossário
    codigo = """while True:  # Loop infinito proposital
    try:
        idade = int(input("Digite sua idade (0-120): "))
        
        # Verifica validade
        if 0 <= idade <= 120:
            print("Idade registrada!")
            break  # Sai do loop se tudo estiver certo
        else:
            print("❌ Idade fora do intervalo lógico.")
            
    except ValueError:
        print("❌ Isso não é um número!")
        
print(f"Processando idade: {idade}...")"""

    mostrar_codigo_didatico(codigo)
    
    print("🔄 [TENTATIVA 1 - ERRO DE TIPO]")
    executar_linha(1)
    executar_linha(3)
    print("   ↳ AÇÃO USUÁRIO: Digita 'abc'")
    executar_linha(12) # Cai no except
    print("   ↳ ERRO: ValueError capturado.")
    executar_linha(13)
    print("   ↳ SAÍDA: ❌ Isso não é um número!")
    print("   ↳ LOOP: Volta para o início (while True).")
    
    print("\n🔄 [TENTATIVA 2 - VALOR FORA DA FAIXA]")
    executar_linha(1)
    executar_linha(3)
    print("   ↳ AÇÃO USUÁRIO: Digita '200'")
    executar_linha(6)
    print("   ↳ TESTE: 200 está entre 0 e 120? Não.")
    executar_linha(10)
    print("   ↳ SAÍDA: ❌ Idade fora do intervalo lógico.")
    
    print("\n🔄 [TENTATIVA 3 - SUCESSO]")
    executar_linha(1)
    executar_linha(3)
    print("   ↳ AÇÃO USUÁRIO: Digita '25'")
    executar_linha(6)
    print("   ↳ TESTE: 25 está entre 0 e 120? Sim.")
    executar_linha(7)
    print("   ↳ SAÍDA: Idade registrada!")
    executar_linha(8)
    print("   ↳ AÇÃO: Break! Sai do loop.")
    
    executar_linha(15)
    print("   ↳ SAÍDA FINAL: Processando idade: 25...")
    
    esperar()

# ==============================================================================
# TÓPICO 5: ELSE NO LOOP E LIST COMPREHENSION
# ==============================================================================
def advanced_features():
    limpar_tela()
    print("🔹 TÓPICO 5: ELSE NO LOOP E LIST COMPREHENSION")
    print("-" * 80)
    print("1. ELSE no Loop: Executa SÓ se o loop terminar NORMALMENTE (sem break).")
    print("2. List Comprehension: Cria listas em uma linha (Pythonic Way).")
    print("-" * 80)
    
    # Baseado nos Exemplos 8 e 9 do Glossário
    codigo = """# 1. ELSE em Loop (Ex: Verificar primo)
num = 7
for i in range(2, num):
    if num % i == 0:
        print("Não é primo")
        break
else:
    # Só executa se o loop foi até o fim (NUNCA acionou o break)
    print(f"{num} é primo!")

# 2. List Comprehension (Substitui loop para criar listas)
# Versão longa:
# quadrados = []
# for x in range(5): quadrados.append(x**2)

# Versão Pythonica:
quadrados = [x**2 for x in range(5)]
print(f"Quadrados: {quadrados}")"""

    mostrar_codigo_didatico(codigo)
    
    print("🔍 [ANALISANDO PRIMO 7]")
    executar_linha(3)
    print("   ↳ O loop testa divisões por 2, 3, 4, 5, 6...")
    print("   ↳ Nenhuma divisão deu exata (break nunca acionado).")
    executar_linha(6)
    print("   ↳ ELSE DO LOOP: Como não houve break, entra aqui.")
    executar_linha(8)
    print("   ↳ SAÍDA: 7 é primo!")
    
    print("\n⚡ [LIST COMPREHENSION]")
    executar_linha(16)
    print("   ↳ PROCESSAMENTO: [0²=0, 1²=1, 2²=4, 3²=9, 4²=16]")
    executar_linha(17)
    print("   ↳ SAÍDA: Quadrados: [0, 1, 4, 9, 16]")
    
    esperar()

# ==============================================================================
# TÓPICO 6: ERROS COMUNS
# ==============================================================================
def erros_comuns():
    limpar_tela()
    print("🔹 TÓPICO 6: ERROS COMUNS")
    print("-" * 80)
    print("1. Loop Infinito (Esquecer de incrementar).")
    print("2. Modificar a lista enquanto itera sobre ela (Causa pulos).")
    print("-" * 80)
    
    codigo = """# ERRO 1: Loop Infinito
i = 0
while i < 5:
    print(i)
    # i += 1  <-- Se esquecer isso, 'i' sempre será 0. Ctrl+C para parar!

# ERRO 2: Modificar lista iterada
nums = [1, 2, 3, 4]
for n in nums:
    if n == 2:
        nums.remove(n) # Isso bagunça os índices internos do for!
# Resultado: Pode pular o 3. Use criar nova lista em vez disso."""

    mostrar_codigo_didatico(codigo)
    print("⚠️  DICA: Se seu programa travar, pressione Ctrl+C no terminal.")
    print("⚠️  DICA: Para filtrar listas, use List Comprehension (visto antes).")
    
    esperar()

# ==============================================================================
# TÓPICO 7: DESAFIO INTEGRADOR (TABUADA)
# ==============================================================================
def desafio_tabuada():
    limpar_tela()
    print("🔹 DESAFIO FINAL: GERADOR DE TABUADA")
    print("Integra: for, range, input, f-strings e estrutura aninhada.")
    print("-" * 80)
    
    # Exemplo 10 do Glossário
    codigo_ref = """num = int(input("Tabuada do: "))
print(f"--- Tabuada do {num} ---")

for i in range(1, 11):
    res = num * i
    print(f"{num} x {i:2} = {res:3}") # :2 e :3 alinham os números

print("-" * 20)"""
    
    mostrar_codigo_didatico(codigo_ref)
    
    try:
        print("\n⚙️  [Entrada de Dados]...")
        num = int(input("   Digite um número (ex: 7): "))
        
        print(f"\n⚙️  [Gerando Tabuada do {num}]...\n")
        time.sleep(0.5)
        
        print(f"--- Tabuada do {num} ---")
        
        # Loop real para mostrar o efeito
        for i in range(1, 11):
            time.sleep(0.2) # Efeito visual de "processamento"
            res = num * i
            # Explicação do alinhamento:
            # {i:2} reserva 2 espaços (para o 10 alinhar com o 9)
            # {res:3} reserva 3 espaços (para resultados de 3 dígitos)
            print(f"{num} x {i:2} = {res:3}")
            
        print("-" * 20)
            
    except ValueError:
        print("\n❌ ERRO: Digite um número inteiro.")
        
    esperar()

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO DE LOOPS (GLOSSÁRIO 08)".center(80))
        print("=" * 80)
        print("1. Loop For e Range (Para sequências)")
        print("2. Loop While (Para condições)")
        print("3. Break e Continue (Controle de Fluxo)")
        print("4. Validação de Dados (While True)")
        print("5. Avançado: Else no Loop e List Comprehension")
        print("6. Erros Comuns (Infinito e Modificação)")
        print("7. Desafio Integrador: Gerador de Tabuada")
        print("0. Sair")
        print("=" * 80)
        
        opcao = input("\nEscolha o tópico para revisar: ")
        
        if opcao == '1': loop_for()
        elif opcao == '2': loop_while()
        elif opcao == '3': break_continue()
        elif opcao == '4': validacao_while()
        elif opcao == '5': advanced_features()
        elif opcao == '6': erros_comuns()
        elif opcao == '7': desafio_tabuada()
        elif opcao == '0':
            print("\nEncerrando laboratório... Cuidado com os loops infinitos! 👋")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()