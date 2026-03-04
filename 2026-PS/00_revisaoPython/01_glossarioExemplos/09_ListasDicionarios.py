# -*- coding: utf-8 -*-
"""
==============================================================================
ARQUIVO: 09_ListasDicionarios.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo sobre Estruturas de Dados (Coleções).
    Baseado integralmente no "Glossário 10 - Listas e Dicionários".

CONTEÚDO PROGRAMÁTICO:
    1. Listas: Coleções ordenadas, mutáveis e indexadas [0, 1, 2...].
    2. Fatiamento (Slicing): Acessando partes da lista [start:stop].
    3. Métodos de Lista: append, insert, remove, pop, sort vs sorted.
    4. Dicionários: Coleções Chave-Valor {key: value} (O "Banco de Dados" da memória).
    5. Métodos de Dict: keys(), values(), items() e o método get() seguro.
    6. Aninhamento: Listas de Dicionários (JSON Style).
    7. Erros Comuns: IndexError e KeyError.
    8. Desafio Integrador: Gerenciador de Tarefas (ToDo List).

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
# TÓPICO 1: LISTAS (BÁSICO E FATIAMENTO)
# ==============================================================================
def listas_basico():
    limpar_tela()
    print("🔹 TÓPICO 1: LISTAS - GAVETAS NUMERADAS")
    print("-" * 80)
    print("Listas guardam vários itens em ordem. Acessamos pelo ÍNDICE (Posição).")
    print("⚠️  Lembre-se: A contagem começa em ZERO!")
    print("   Índices Negativos (-1) pegam do final para o início.")
    print("-" * 80)

    # Baseado no Exemplo 1 e 2 do Glossário
    codigo = """# Criando uma lista (Usa colchetes [])
filmes = ["Matrix", "Avatar", "Titanic", "Shrek"]

# Acessando itens
print(f"Primeiro: {filmes[0]}")   # Índice 0 = Matrix
print(f"Último:   {filmes[-1]}")  # Índice -1 = Shrek

# Slicing (Fatiamento) -> [inicio : fim_exclusivo]
top2 = filmes[0:2]  # Pega índices 0 e 1 (O 2 fica de fora!)
print(f"Top 2: {top2}")"""

    mostrar_codigo_didatico(codigo)

    executar_linha(2)
    filmes = ["Matrix", "Avatar", "Titanic", "Shrek"]
    print(f"   ↳ MEMÓRIA: [0:Matrix, 1:Avatar, 2:Titanic, 3:Shrek]")

    executar_linha(5)
    print(f"   ↳ SAÍDA: Primeiro: {filmes[0]}")

    executar_linha(6)
    print(f"   ↳ ACESSO REVERSO: -1 é o último item.")
    print(f"   ↳ SAÍDA: Último:   {filmes[-1]}")

    executar_linha(9)
    print(f"   ↳ SLICING: Pegando do 0 até (antes do) 2 -> [0, 1]")
    top2 = filmes[0:2]
    
    executar_linha(10)
    print(f"   ↳ SAÍDA: Top 2: {top2}")
    
    esperar()

# ==============================================================================
# TÓPICO 2: MÉTODOS DE LISTA (ALTERANDO DADOS)
# ==============================================================================
def listas_metodos():
    limpar_tela()
    print("🔹 TÓPICO 2: MÉTODOS DE LISTA (CRUD)")
    print("-" * 80)
    print("Listas são MUTÁVEIS (podemos alterar, adicionar e remover).")
    print("Principais métodos: append, insert, pop, remove, sort.")
    print("-" * 80)
    
    # Baseado no Exemplo 3 do Glossário
    codigo = """nums = [10, 5, 8]

# 1. Adicionar (Create)
nums.append(20)      # Adiciona ao FINAL
nums.insert(0, 99)   # Insere na posição 0 (Empurra o resto)
print(f"Após adições: {nums}")

# 2. Remover (Delete)
removido = nums.pop() # Remove e retorna o ÚLTIMO
nums.remove(5)        # Remove o VALOR 5 (não o índice)
print(f"Saiu: {removido} | Lista final: {nums}")

# 3. Ordenar (Sort)
nums.sort()           # Organiza a PRÓPRIA lista (Crescente)
print(f"Ordenada: {nums}")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    nums = [10, 5, 8]
    print(f"   ↳ LISTA INICIAL: {nums}")
    
    executar_linha(4)
    nums.append(20)
    print(f"   ↳ APPEND: [10, 5, 8, 20]")
    
    executar_linha(5)
    nums.insert(0, 99)
    print(f"   ↳ INSERT(0, 99): [99, 10, 5, 8, 20]")
    
    executar_linha(6)
    print(f"   ↳ SAÍDA: Após adições: {nums}")
    
    executar_linha(9)
    removido = nums.pop()
    print(f"   ↳ POP: Removeu o 20 do final.")
    
    executar_linha(10)
    if 5 in nums:
        nums.remove(5)
        print(f"   ↳ REMOVE(5): Procurou o valor 5 e deletou.")
    
    executar_linha(11)
    print(f"   ↳ SAÍDA: Saiu: {removido} | Lista final: {nums}")
    
    executar_linha(14)
    nums.sort()
    print(f"   ↳ SORT: Reorganizando itens em ordem crescente...")
    
    executar_linha(15)
    print(f"   ↳ SAÍDA: Ordenada: {nums}")
    
    esperar()

# ==============================================================================
# TÓPICO 3: DICIONÁRIOS (CHAVE-VALOR)
# ==============================================================================
def dicionarios_basico():
    limpar_tela()
    print("🔹 TÓPICO 3: DICIONÁRIOS (CHAVE: VALOR)")
    print("-" * 80)
    print("Dicionários não usam índices numéricos [0]. Usam CHAVES personalizadas.")
    print("Sintaxe: { 'chave': valor }")
    print("Ideal para representar objetos reais (Pessoa, Produto, Carro).")
    print("-" * 80)
    
    # Baseado no Exemplo 5 do Glossário
    codigo = """# Criando um dicionário (Usa chaves {})
aluno = {
    "nome": "João",
    "nota": 8.5,
    "ativo": True
}

# Acessando valores pela chave (Etiqueta)
print(f"Aluno: {aluno['nome']}")

# Modificando e Adicionando
aluno["nota"] = 9.0        # Atualiza existente
aluno["curso"] = "Python"  # Cria nova chave
print(aluno)"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(2) # Bloco de criação
    aluno = {"nome": "João", "nota": 8.5, "ativo": True}
    print("   ↳ MEMÓRIA: Estrutura criada. Chaves: 'nome', 'nota', 'ativo'.")
    
    executar_linha(8)
    print(f"   ↳ ACESSO: Buscando etiqueta 'nome' -> '{aluno['nome']}'")
    print(f"   ↳ SAÍDA: Aluno: João")
    
    executar_linha(11)
    aluno["nota"] = 9.0
    print("   ↳ UPDATE: Chave 'nota' atualizada para 9.0")
    
    executar_linha(12)
    aluno["curso"] = "Python"
    print("   ↳ CREATE: Nova chave 'curso' inserida.")
    
    executar_linha(13)
    print(f"   ↳ DADOS COMPLETOS: {aluno}")
    
    esperar()

# ==============================================================================
# TÓPICO 4: MÉTODOS DE DICIONÁRIO E GET
# ==============================================================================
def dicionarios_metodos():
    limpar_tela()
    print("🔹 TÓPICO 4: ITERAÇÃO E SEGURANÇA (GET)")
    print("-" * 80)
    print("1. Métodos: .keys() (chaves), .values() (valores), .items() (pares).")
    print("2. Segurança: Acessar uma chave que não existe com [] gera ERRO.")
    print("   Use .get() para evitar o crash!")
    print("-" * 80)
    
    # Baseado no Exemplo 6 e 7 do Glossário
    codigo = """produto = {"nome": "Notebook", "preco": 3500}

# 1. Iterando sobre chaves e valores
for k, v in produto.items():
    print(f"{k}: {v}")

# 2. Acesso Seguro com .get()
# print(produto["estoque"])  # ERRO! KeyError (chave não existe)

qtd = produto.get("estoque", 0) # Se não existir, retorna 0
print(f"Estoque: {qtd}")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    produto = {"nome": "Notebook", "preco": 3500}
    
    print("\n🔄 [LOOP ITEMS]")
    executar_linha(4)
    print("   ↳ k='nome', v='Notebook'")
    executar_linha(5)
    print("   ↳ SAÍDA: nome: Notebook")
    
    print("   ↳ k='preco', v=3500")
    print("   ↳ SAÍDA: preco: 3500")
    
    print("\n🛡️  [ACESSO SEGURO]")
    executar_linha(8)
    print("   ↳ ANÁLISE: A linha 8 comentada causaria KeyError (Crash).")
    
    executar_linha(10)
    qtd = produto.get("estoque", 0)
    print("   ↳ GET: Chave 'estoque' não encontrada. Retornando valor padrão 0.")
    
    executar_linha(11)
    print(f"   ↳ SAÍDA: Estoque: 0")
    
    esperar()

# ==============================================================================
# TÓPICO 5: ANINHAMENTO (JSON STYLE)
# ==============================================================================
def aninhamento():
    limpar_tela()
    print("🔹 TÓPICO 5: ANINHAMENTO (ESTRUTURAS COMPLEXAS)")
    print("-" * 80)
    print("Podemos ter Listas dentro de Dicionários e vice-versa.")
    print("É assim que APIs e Bancos de Dados (JSON) trafegam dados.")
    print("-" * 80)
    
    # Baseado no Exemplo 8 do Glossário
    codigo = """# Lista de Dicionários (Tabela de Dados)
turma = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Bia"}
]

# Acessando "Bia":
# 1. Pegar o item 1 da lista (Dict da Bia)
# 2. Pegar a chave "nome" desse Dict
print(turma[1]["nome"])

# Iterando (Muito comum em sistemas!)
print("--- Chamada ---")
for aluno in turma:
    print(f"- {aluno['nome']}")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(2) # Criação
    turma = [{"id": 1, "nome": "Ana"}, {"id": 2, "nome": "Bia"}]
    print("   ↳ ESTRUTURA: Lista com 2 dicionários dentro.")
    
    executar_linha(9)
    print("   ↳ PASSO 1: turma[1] -> {'id': 2, 'nome': 'Bia'}")
    print("   ↳ PASSO 2: ...['nome'] -> 'Bia'")
    print("   ↳ SAÍDA: Bia")
    
    executar_linha(12)
    
    print("\n🔄 [LOOP NA LISTA]")
    for aluno in turma:
        time.sleep(0.5)
        print(f"   ↳ Processando aluno: {aluno}")
        print(f"   ↳ SAÍDA: - {aluno['nome']}")
        
    esperar()

# ==============================================================================
# TÓPICO 6: ERROS COMUNS
# ==============================================================================
def erros_comuns():
    limpar_tela()
    print("🔹 TÓPICO 6: ERROS COMUNS")
    print("-" * 80)
    print("1. IndexError: Tentar acessar posição que não existe na Lista.")
    print("2. KeyError: Tentar acessar chave que não existe no Dict.")
    print("3. Sort vs Sorted: Um altera o original, o outro cria cópia.")
    print("-" * 80)
    
    codigo = """lista = ["A", "B"]
# print(lista[5])      # IndexError! (Só vai até 1)

dic = {"nome": "Ana"}
# print(dic["idade"])  # KeyError! (Use .get)

numeros = [3, 1, 2]
novo = sorted(numeros) # Cria nova lista ordenada (numeros fica igual)
numeros.sort()         # Altera a lista 'numeros' para sempre!"""

    mostrar_codigo_didatico(codigo)
    print("⚠️  DICA: Sempre verifique o tamanho da lista (len) antes de acessar índices fixos.")
    print("⚠️  DICA: Use .get() para dicionários quando não tiver certeza se a chave existe.")
    
    esperar()

# ==============================================================================
# TÓPICO 7: DESAFIO INTEGRADOR (TODO LIST)
# ==============================================================================
def desafio_todo():
    limpar_tela()
    print("🔹 DESAFIO FINAL: GERENCIADOR DE TAREFAS (TODO LIST)")
    print("Integra: Listas, Dicionários, Input, Append e Loop.")
    print("-" * 80)
    
    # Exemplo 10 do Glossário
    codigo_ref = """tarefas = []  # Lista vazia para começar

while True:
    print("\\n1. Adicionar | 2. Listar | 0. Sair")
    opcao = input("Opção: ")
    
    if opcao == "1":
        desc = input("Tarefa: ")
        # Adiciona um Dicionário na Lista
        tarefas.append({"desc": desc, "feita": False})
        print("Adicionado!")
        
    elif opcao == "2":
        print("--- Minhas Tarefas ---")
        for i, t in enumerate(tarefas):
            status = "✅" if t["feita"] else "❌"
            print(f"{i}. [{status}] {t['desc']}")
            
    elif opcao == "0": break"""
    
    mostrar_codigo_didatico(codigo_ref)
    
    # Simulação Interativa Limitada
    tarefas = []
    print("\n--- MODO INTERATIVO (Simulação de 2 ações) ---")
    
    # Ação 1: Adicionar
    print("\n⚙️  [Simulando Opção 1: Adicionar]")
    desc = input("   Digite uma tarefa (ex: Estudar Python): ")
    tarefas.append({"desc": desc, "feita": False})
    print(f"   ↳ MEMÓRIA: tarefas = [{tarefas[0]}]")
    
    # Ação 2: Adicionar outra
    print("\n⚙️  [Simulando Opção 1: Adicionar outra]")
    tarefas.append({"desc": "Dormir cedo", "feita": True}) # Simulando uma feita
    print(f"   ↳ MEMÓRIA: 2 itens na lista.")
    
    # Ação 3: Listar
    print("\n⚙️  [Simulando Opção 2: Listar]")
    print("   --- Minhas Tarefas ---")
    for i, t in enumerate(tarefas):
        status = "✅" if t["feita"] else "❌"
        time.sleep(0.5)
        print(f"   {i}. [{status}] {t['desc']}")
        
    print("\n   (O enumerate gera o índice 'i' automaticamente!)")
    esperar()

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO DE ESTRUTURAS DE DADOS (GLOSSÁRIO 10)".center(80))
        print("=" * 80)
        print("1. Listas: Básico e Fatiamento (Slicing)")
        print("2. Métodos de Lista (Append, Pop, Sort)")
        print("3. Dicionários: Conceito Chave-Valor")
        print("4. Métodos de Dict e Segurança (.get)")
        print("5. Aninhamento (Lista de Dicionários)")
        print("6. Erros Comuns (IndexError, KeyError)")
        print("7. Desafio Integrador: ToDo List")
        print("0. Sair")
        print("=" * 80)
        
        opcao = input("\nEscolha o tópico para revisar: ")
        
        if opcao == '1': listas_basico()
        elif opcao == '2': listas_metodos()
        elif opcao == '3': dicionarios_basico()
        elif opcao == '4': dicionarios_metodos()
        elif opcao == '5': aninhamento()
        elif opcao == '6': erros_comuns()
        elif opcao == '7': desafio_todo()
        elif opcao == '0':
            print("\nEncerrando Curso de Fundamentos... Agora é praticar! 🚀")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()