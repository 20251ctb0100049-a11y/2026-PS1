# -*- coding: utf-8 -*-
"""
==============================================================================
ARQUIVO: 10_ModulosBibliotecas.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo sobre Módulos e Bibliotecas.
    Baseado integralmente no "Glossário 11 - Módulos e Bibliotecas".

CONTEÚDO PROGRAMÁTICO:
    1. Conceito: "Não reinvente a roda" - Usando código pronto.
    2. Importação Completa: import math (Acesso via ponto).
    3. Importação Específica: from math import sqrt (Acesso direto).
    4. Apelidos (Alias): import datetime as dt (Código mais curto).
    5. Módulos Nativos (Standard Lib): math, random, datetime, os.
    6. Pacotes Externos: O conceito de PIP e PyPI (pandas, requests).
    7. Erros Comuns: Nomear arquivo igual ao módulo (random.py).
    8. Desafio Integrador: Calculadora de Dias de Vida (datetime).

==============================================================================
"""

import sys
import time

# Importações que serão usadas nos exemplos (mas vamos simular a execução)
import math
import random
import datetime

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
# TÓPICO 1: O BÁSICO (IMPORT MATH)
# ==============================================================================
def import_completo():
    limpar_tela()
    print("🔹 TÓPICO 1: IMPORTAÇÃO COMPLETA (IMPORT GENÉRICO)")
    print("-" * 80)
    print("O Python vem com a 'Standard Library' (Baterias Inclusas).")
    print("Para usar, precisamos avisar com o comando 'import'.")
    print("Sintaxe: import nome_modulo -> Uso: nome_modulo.funcao()")
    print("-" * 80)

    # Baseado no Exemplo 1 do Glossário
    codigo = """import math  # Carrega TODA a biblioteca de matemática

# Precisamos usar o prefixo "math."
raiz = math.sqrt(25)
pi = math.pi

print(f"Raiz de 25: {raiz}")
print(f"Valor de Pi: {pi:.4f}")"""

    mostrar_codigo_didatico(codigo)

    executar_linha(1)
    print("   ↳ SISTEMA: Biblioteca 'math' carregada na memória RAM.")

    executar_linha(4)
    print(f"   ↳ CÁLCULO: math.sqrt(25) -> 5.0")
    
    executar_linha(5)
    print(f"   ↳ MEMÓRIA: math.pi -> 3.141592...")

    executar_linha(7)
    print(f"   ↳ SAÍDA: Raiz de 25: 5.0")

    executar_linha(8)
    print(f"   ↳ SAÍDA: Valor de Pi: 3.1416")
    
    esperar()

# ==============================================================================
# TÓPICO 2: IMPORTAÇÃO ESPECÍFICA (FROM ... IMPORT)
# ==============================================================================
def import_especifico():
    limpar_tela()
    print("🔹 TÓPICO 2: IMPORTAÇÃO ESPECÍFICA (FROM ... IMPORT)")
    print("-" * 80)
    print("Se você só quer UMA ferramenta da caixa, não traga a caixa toda.")
    print("Vantagem: Não precisa digitar o prefixo (math.).")
    print("Cuidado: Pode causar conflito de nomes se tiver variáveis iguais.")
    print("-" * 80)
    
    # Baseado no Exemplo 2 do Glossário
    codigo = """from math import sqrt, factorial

# Agora usamos DIRETO (sem "math.")
num = 5
fatorial = factorial(num)  # 5*4*3*2*1
raiz = sqrt(16)

print(f"Fatorial de 5: {fatorial}")
print(f"Raiz de 16: {raiz}")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    print("   ↳ SISTEMA: Apenas 'sqrt' e 'factorial' foram trazidas.")
    
    executar_linha(4)
    
    executar_linha(5)
    print(f"   ↳ CÁLCULO: factorial(5) -> 120")
    
    executar_linha(6)
    print(f"   ↳ CÁLCULO: sqrt(16) -> 4.0")
    
    executar_linha(8)
    print(f"   ↳ SAÍDA: Fatorial de 5: 120")
    
    executar_linha(9)
    print(f"   ↳ SAÍDA: Raiz de 16: 4.0")
    
    esperar()

# ==============================================================================
# TÓPICO 3: APELIDOS (ALIAS - AS)
# ==============================================================================
def import_alias():
    limpar_tela()
    print("🔹 TÓPICO 3: APELIDOS (AS)")
    print("-" * 80)
    print("Alguns nomes são longos ou padrões da indústria.")
    print("Usamos 'as' para dar um apelido curto.")
    print("Ex: 'import datetime as dt' ou 'import pandas as pd'.")
    print("-" * 80)
    
    # Baseado no Exemplo 3 do Glossário
    codigo = """import datetime as dt  # Apelidando para 'dt'

# Usamos 'dt' em vez de 'datetime'
agora = dt.datetime.now()
ano_atual = agora.year

print(f"Data/Hora: {agora}")
print(f"Estamos em: {ano_atual}")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    print("   ↳ SISTEMA: Módulo 'datetime' carregado como 'dt'.")
    
    executar_linha(4)
    agora = datetime.datetime.now()
    print(f"   ↳ EXECUÇÃO: dt.datetime.now() -> {agora}")
    
    executar_linha(5)
    print(f"   ↳ ACESSO: agora.year -> {agora.year}")
    
    executar_linha(7)
    print(f"   ↳ SAÍDA: Data/Hora: {agora}")
    
    executar_linha(8)
    print(f"   ↳ SAÍDA: Estamos em: {agora.year}")
    
    esperar()

# ==============================================================================
# TÓPICO 4: MÓDULOS NATIVOS ÚTEIS
# ==============================================================================
def modulos_uteis():
    limpar_tela()
    print("🔹 TÓPICO 4: CAIXA DE FERRAMENTAS (RANDOM & TIME)")
    print("-" * 80)
    print("Dois módulos essenciais para jogos e simulações:")
    print("1. random: Gera números aleatórios e sorteios.")
    print("2. time: Controla o tempo (pausas e medições).")
    print("-" * 80)
    
    # Baseado no Exemplo 4 do Glossário
    codigo = """import random
import time

print("Sorteando dado em 3 segundos...")
time.sleep(3)  # Pausa o programa

dado = random.randint(1, 6)
print(f"Resultado: {dado}")

lista = ["Python", "Java", "C#"]
escolha = random.choice(lista) # Escolhe um item aleatório
print(f"Linguagem sorteada: {escolha}")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1); executar_linha(2)
    
    executar_linha(4)
    print("   ↳ SAÍDA: Sorteando dado em 3 segundos...")
    
    executar_linha(5)
    print("   ↳ SLEEP: O programa 'dorme' (Pausa real de 3s)...")
    time.sleep(3) # Pausa real para o aluno sentir
    
    executar_linha(7)
    dado = random.randint(1, 6)
    print(f"   ↳ RANDOM: Gerado {dado}")
    
    executar_linha(8)
    print(f"   ↳ SAÍDA: Resultado: {dado}")
    
    executar_linha(10)
    
    executar_linha(11)
    escolha = random.choice(["Python", "Java", "C#"])
    print(f"   ↳ CHOICE: Sorteado '{escolha}' da lista.")
    
    executar_linha(12)
    print(f"   ↳ SAÍDA: Linguagem sorteada: {escolha}")
    
    esperar()

# ==============================================================================
# TÓPICO 5: PACOTES EXTERNOS (PIP)
# ==============================================================================
def pacotes_externos():
    limpar_tela()
    print("🔹 TÓPICO 5: PACOTES EXTERNOS (PIP)")
    print("-" * 80)
    print("O Python tem um repositório com 500.000+ pacotes: PyPI.org")
    print("Para instalar coisas que não vêm com o Python, usamos o terminal.")
    print("Comando: pip install nome_do_pacote")
    print("-" * 80)
    
    # Baseado na seção de Pacotes Externos do Glossário
    codigo = """# No Terminal (CMD/Powershell), não no Python:
# > pip install pandas
# > pip install requests

# No Código Python:
import pandas as pd

dados = {"Nome": ["Ana", "Bia"], "Nota": [8, 9]}
tabela = pd.DataFrame(dados) # Cria uma tabela estilo Excel

print(tabela)"""

    mostrar_codigo_didatico(codigo)
    
    print("ℹ️  SIMULAÇÃO (Pandas não vem instalado por padrão, mas simularemos):")
    
    executar_linha(6)
    print("   ↳ SISTEMA: Carregando pandas como 'pd'...")
    
    executar_linha(8)
    print("   ↳ MEMÓRIA: Dicionário de dados criado.")
    
    executar_linha(9)
    print("   ↳ PANDAS: Convertendo dicionário em DataFrame (Tabela)...")
    
    executar_linha(11)
    print("   ↳ SAÍDA VIRTUAL:")
    print("      Nome  Nota")
    print("   0   Ana     8")
    print("   1   Bia     9")
    
    print("\n💡 DICA: Pandas é a biblioteca mais usada no mundo para Data Science!")
    esperar()

# ==============================================================================
# TÓPICO 6: ERROS COMUNS (IMPORTANTE!)
# ==============================================================================
def erros_comuns():
    limpar_tela()
    print("🔹 TÓPICO 6: ERROS COMUNS (O PERIGO DO NOME)")
    print("-" * 80)
    print("⚠️  ERRO CRÍTICO: Nomear seu arquivo igual a uma biblioteca.")
    print("Exemplo: Criar um arquivo chamado 'random.py' e tentar 'import random'.")
    print("O Python vai importar O SEU ARQUIVO em vez do oficial, quebrando tudo.")
    print("-" * 80)
    
    codigo = """# Arquivo: random.py (NOME ERRADO!)
import random 

# Isso vai dar erro de "AttributeError"
# Porque o Python acha que "random" é este arquivo vazio,
# e não a biblioteca que gera números.
n = random.randint(1, 10)"""

    mostrar_codigo_didatico(codigo)
    print("🚫 ANÁLISE DO ERRO:")
    print("   1. O Python procura 'random' primeiro na pasta atual.")
    print("   2. Ele encontra 'random.py' (seu arquivo).")
    print("   3. Ele tenta achar 'randint' dentro dele e não encontra.")
    print("   4. CRASH! O programa fecha.")
    print("\n✅ SOLUÇÃO: Nunca chame seus arquivos de: math.py, random.py, time.py...")
    
    esperar()

# ==============================================================================
# TÓPICO 7: DESAFIO INTEGRADOR (DIAS DE VIDA)
# ==============================================================================
def desafio_datas():
    limpar_tela()
    print("🔹 DESAFIO FINAL: CALCULADORA DE DIAS DE VIDA")
    print("Integra: datetime (date), input, conversão e subtração de datas.")
    print("-" * 80)
    
    # Exemplo Integrador do Glossário
    codigo_ref = """import datetime as dt

def dias_de_vida():
    # 1. Entrada de dados (String)
    nasc_str = input("Data nasc (DD/MM/AAAA): ")
    
    # 2. Convertendo String para Objeto Data
    # strptime = String Parse Time (Interpretar Texto)
    nasc_data = dt.datetime.strptime(nasc_str, "%d/%m/%Y")
    
    # 3. Data de hoje
    hoje = dt.datetime.now()
    
    # 4. Cálculo (Data - Data = Timedelta/Diferença)
    diferenca = hoje - nasc_data
    
    print(f"Você viveu {diferenca.days} dias!")"""
    
    mostrar_codigo_didatico(codigo_ref)
    
    try:
        print("\n⚙️  [Executando Calculadora]...")
        nasc_str = input("   Digite sua data de nascimento (ex: 15/05/2000): ")
        
        # Simulação robusta
        try:
            # Tenta converter formato DD/MM/AAAA
            dia, mes, ano = map(int, nasc_str.split('/'))
            nasc_data = datetime.datetime(ano, mes, dia)
            hoje = datetime.datetime.now()
            
            print("\n⚙️  [Calculando Delta de Tempo]...")
            time.sleep(1)
            
            diferenca = hoje - nasc_data
            dias = diferenca.days
            
            print("-" * 30)
            print(f"📅 Data Nasc: {nasc_data.strftime('%d/%m/%Y')}")
            print(f"📅 Hoje:      {hoje.strftime('%d/%m/%Y')}")
            print(f"⏳ Resultado: Você já viveu {dias} dias!")
            
            if dias > 10000:
                print("🏆 Conquista: Clube dos 10k dias desbloqueado!")
            print("-" * 30)
            
        except:
            print("\n❌ ERRO: Formato inválido! Use DD/MM/AAAA (ex: 25/12/2000).")
            
    except ValueError:
        print("\n❌ ERRO: Dados inválidos.")
        
    esperar()

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO DE MÓDULOS (GLOSSÁRIO 11)".center(80))
        print("=" * 80)
        print("1. Importação Completa (import math)")
        print("2. Importação Específica (from ... import)")
        print("3. Apelidos/Alias (import ... as)")
        print("4. Standard Library (random, time)")
        print("5. Pacotes Externos (Conceito de PIP)")
        print("6. Erros Comuns (random.py)")
        print("7. Desafio Integrador: Dias de Vida (datetime)")
        print("0. Sair")
        print("=" * 80)
        
        opcao = input("\nEscolha o tópico para revisar: ")
        
        if opcao == '1': import_completo()
        elif opcao == '2': import_especifico()
        elif opcao == '3': import_alias()
        elif opcao == '4': modulos_uteis()
        elif opcao == '5': pacotes_externos()
        elif opcao == '6': erros_comuns()
        elif opcao == '7': desafio_datas()
        elif opcao == '0':
            print("\nEncerrando Módulo Final... Parabéns por completar a revisão! 🎓")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()