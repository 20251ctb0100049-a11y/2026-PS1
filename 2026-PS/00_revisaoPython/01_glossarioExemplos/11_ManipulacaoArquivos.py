# -*- coding: utf-8 -*-
"""
==============================================================================
ARQUIVO: 11_ManipulacaoArquivos.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo sobre Manipulação de Arquivos (Leitura e Escrita).
    Baseado integralmente no "Glossário 12 - Manipulação de Arquivos".

CONTEÚDO PROGRAMÁTICO:
    1. Conceito: Persistência (RAM vs Disco) - Salvando dados permanentemente.
    2. Abertura: Função open() e modos (r, w, a, x).
    3. Boas Práticas: O bloco 'with' (Gerenciador de Contexto) que fecha sozinho.
    4. Escrita: write() e a necessidade do \\n para pular linha.
    5. Leitura: read() (tudo), readline() (linha) e readlines() (lista).
    6. Erros Comuns: FileNotFoundError e esquecer de fechar (close).
    7. Desafio Integrador: Bloco de Notas Persistente (Logger).

==============================================================================
"""

import sys
import time
import os # Necessário para verificar se arquivo existe e limpar bagunça

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
# TÓPICO 1: O JEITO ANTIGO VS JEITO NOVO (WITH)
# ==============================================================================
def open_vs_with():
    limpar_tela()
    print("🔹 TÓPICO 1: ABRINDO ARQUIVOS (OPEN VS WITH)")
    print("-" * 80)
    print("Para mexer num arquivo, precisamos ABRI-LO (open).")
    print("Modo Clássico: Exige .close() manual (Perigoso se der erro antes).")
    print("Modo Moderno (Pythonic): Bloco 'with' fecha sozinho (Seguro).")
    print("-" * 80)

    # Baseado no Glossário
    codigo = """# 1. Jeito Antigo (Não recomendado)
arquivo = open("teste_antigo.txt", "w") # 'w' = Write (Escrever)
arquivo.write("Olá, Disco!")
# Se o programa travar aqui, o arquivo fica aberto e corrompido!
arquivo.close() # Obrigatório lembrar disso

# 2. Jeito Seguro (with)
# O arquivo fecha automaticamente ao sair do bloco (mesmo com erro)
with open("teste_novo.txt", "w") as arq:
    arq.write("Olá, Pythonic World!")
    print("Escrevendo...")
# Aqui o arquivo já está fechado!"""

    mostrar_codigo_didatico(codigo)

    print("💾 [CRIANDO ARQUIVO NO DISCO]")
    executar_linha(2)
    print("   ↳ SISTEMA: Criado 'teste_antigo.txt' no modo escrita.")
    executar_linha(3)
    print("   ↳ DISCO: Gravando bytes...")
    executar_linha(5)
    print("   ↳ SISTEMA: Arquivo fechado manualmente.")

    print("\n🛡️  [USANDO WITH - CONTEXT MANAGER]")
    executar_linha(9)
    print("   ↳ SISTEMA: Bloco iniciado. Arquivo 'teste_novo.txt' aberto.")
    executar_linha(10)
    print("   ↳ DISCO: Gravando bytes...")
    executar_linha(11)
    print("   ↳ SAÍDA: Escrevendo...")
    
    print("\n   (Saindo do bloco with...)")
    print("   ✅ SISTEMA: O Python detectou o fim do bloco e fechou o arquivo sozinho.")
    
    esperar()

# ==============================================================================
# TÓPICO 2: MODOS DE ABERTURA (W vs A)
# ==============================================================================
def modos_escrita():
    limpar_tela()
    print("🔹 TÓPICO 2: ESCREVENDO (WRITE VS APPEND)")
    print("-" * 80)
    print("CUIDADO: O modo 'w' APAGA tudo que tinha no arquivo antes!")
    print("Se quiser adicionar conteúdo, use o modo 'a' (Append).")
    print("Não esqueça do '\\n' para pular linha, senão fica tudo grudado.")
    print("-" * 80)
    
    # Baseado no Glossário
    codigo = """# Passo 1: Modo 'w' (Cria ou Sobrescreve)
with open("diario.txt", "w") as f:
    f.write("Dia 1: Aprendi Python.\\n")

# Passo 2: Modo 'w' de novo (PERIGO!)
with open("diario.txt", "w") as f:
    f.write("Dia 2: Esqueci tudo.\\n") 
    # O Dia 1 foi apagado!

# Passo 3: Modo 'a' (Append - Adicionar)
with open("diario.txt", "a") as f:
    f.write("Dia 3: Recuperei a memória!\\n")"""

    mostrar_codigo_didatico(codigo)

    print("📝 [DIA 1 - MODO W]")
    executar_linha(2)
    executar_linha(3)
    print("   ↳ CONTEÚDO DO ARQUIVO: 'Dia 1: Aprendi Python.'")
    
    print("\n⚠️  [DIA 2 - MODO W NOVAMENTE]")
    executar_linha(6)
    print("   ↳ ALERTA: O arquivo existia e foi ZERADO pelo modo 'w'.")
    executar_linha(7)
    print("   ↳ CONTEÚDO DO ARQUIVO: 'Dia 2: Esqueci tudo.' (Dia 1 sumiu!)")
    
    print("\nue [DIA 3 - MODO A]")
    executar_linha(11)
    print("   ↳ SISTEMA: Abrindo sem apagar (cursor no final).")
    executar_linha(12)
    print("   ↳ CONTEÚDO DO ARQUIVO:")
    print("     Line 1: Dia 2: Esqueci tudo.")
    print("     Line 2: Dia 3: Recuperei a memória!")
    
    esperar()

# ==============================================================================
# TÓPICO 3: LENDO ARQUIVOS (READ)
# ==============================================================================
def leitura():
    limpar_tela()
    print("🔹 TÓPICO 3: LENDO DADOS (READ, READLINE, READLINES)")
    print("-" * 80)
    print("Para ler, usamos modo 'r' (Read).")
    print("   .read()      -> Lê TUDO de uma vez (uma stringão).")
    print("   .readlines() -> Devolve uma LISTA de linhas.")
    print("-" * 80)
    
    # Criando arquivo para teste
    with open("lista_compras.txt", "w") as f:
        f.write("Arroz\nFeijão\nBatata")
    
    # Baseado no Glossário
    codigo = """# Arquivo 'lista_compras.txt' já existe com 3 itens.

print("--- Método 1: read() ---")
with open("lista_compras.txt", "r") as f:
    conteudo = f.read()  # Traz tudo para a memória
    print(conteudo)

print("\\n--- Método 2: readlines() ---")
with open("lista_compras.txt", "r") as f:
    linhas = f.readlines() # Cria uma lista
    print(linhas)"""

    mostrar_codigo_didatico(codigo)
    
    print("📖 [MÉTODO 1: LER TUDO]")
    executar_linha(4)
    executar_linha(5)
    print("   ↳ MEMÓRIA: 'Arroz\\nFeijão\\nBatata'")
    executar_linha(6)
    print("   ↳ SAÍDA:\nArroz\nFeijão\nBatata")
    
    print("\n📖 [MÉTODO 2: LER LISTA]")
    executar_linha(9)
    executar_linha(10)
    print("   ↳ MEMÓRIA: ['Arroz\\n', 'Feijão\\n', 'Batata']")
    print("   ↳ NOTA: O \\n vem junto na lista!")
    executar_linha(11)
    print("   ↳ SAÍDA: ['Arroz\\n', 'Feijão\\n', 'Batata']")
    
    esperar()

# ==============================================================================
# TÓPICO 4: ERROS COMUNS (FILENOTFOUND)
# ==============================================================================
def erros_comuns():
    limpar_tela()
    print("🔹 TÓPICO 4: ERROS COMUNS (ARQUIVO INEXISTENTE)")
    print("-" * 80)
    print("Tentar ler (modo 'r') um arquivo que não existe gera ERRO.")
    print("Sempre use try/except ou verifique com os.path.exists().")
    print("-" * 80)
    
    # Baseado no Glossário
    codigo = """nome_arquivo = "secreto.txt" # Não existe!

try:
    with open(nome_arquivo, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("❌ Erro: O arquivo não foi encontrado.")
    print("   Criando um novo para você...")
    with open(nome_arquivo, "w") as f:
        f.write("Segredo Revelado!")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    
    print("\n🔍 [TENTATIVA DE LEITURA]")
    executar_linha(3)
    executar_linha(4)
    print("   ↳ SISTEMA: Procurando 'secreto.txt' no disco...")
    time.sleep(1)
    print("   ↳ FALHA: Arquivo não existe.")
    
    executar_linha(6) # Cai no except
    print("   ↳ CAPTURA: FileNotFoundError tratado.")
    
    executar_linha(7)
    print("   ↳ SAÍDA: ❌ Erro: O arquivo não foi encontrado.")
    
    executar_linha(8)
    print("   ↳ AÇÃO: Recuperação do erro.")
    
    executar_linha(9)
    print("   ↳ SISTEMA: Criando arquivo vazio no modo 'w'.")
    executar_linha(10)
    print("   ↳ SUCESSO: Arquivo criado e salvo.")
    
    esperar()

# ==============================================================================
# TÓPICO 5: DESAFIO INTEGRADOR (LOGGER)
# ==============================================================================
def desafio_logger():
    limpar_tela()
    print("🔹 DESAFIO FINAL: BLOCO DE NOTAS PERSISTENTE")
    print("Este programa lembra o que você escreveu mesmo se fechar!")
    print("Integra: input, datetime, modo 'a' e leitura.")
    print("-" * 80)
    
    # Exemplo baseado no Glossário
    codigo_ref = """import datetime

arquivo_log = "meu_log.txt"

def adicionar_nota():
    texto = input("Nota: ")
    hora = datetime.datetime.now().strftime("%d/%m %H:%M")
    
    # Modo 'a' para não apagar o histórico
    with open(arquivo_log, "a") as f:
        f.write(f"[{hora}] {texto}\\n")
    print("✅ Salvo!")

def ler_notas():
    try:
        with open(arquivo_log, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("📭 Nenhum registro ainda.")"""
    
    mostrar_codigo_didatico(codigo_ref)
    
    arquivo_log = "meu_log_lab.txt" # Nome para este laboratório
    
    while True:
        print(f"\n--- LOGGER v1.0 ({arquivo_log}) ---")
        print("1. Escrever nova nota")
        print("2. Ler histórico")
        print("0. Sair e Apagar Testes")
        
        op = input("Opção: ")
        
        if op == "1":
            nota = input("   ✍️  Digite sua nota: ")
            data_hora = time.strftime("%d/%m %H:%M")
            
            with open(arquivo_log, "a", encoding='utf-8') as f:
                f.write(f"[{data_hora}] {nota}\n")
            
            print("   💾 Gravando no disco rígido...")
            time.sleep(0.5)
            print("   ✅ Persistido com sucesso!")
            
        elif op == "2":
            print("\n   📜 LENDO DO DISCO...")
            time.sleep(0.5)
            if os.path.exists(arquivo_log):
                with open(arquivo_log, "r", encoding='utf-8') as f:
                    print("-" * 40)
                    print(f.read().strip())
                    print("-" * 40)
            else:
                print("   📭 Arquivo ainda não existe.")
                
        elif op == "0":
            # Limpeza
            if os.path.exists(arquivo_log):
                os.remove(arquivo_log)
                print("   🧹 Arquivo de log de teste removido.")
            # Limpando outros arquivos criados no laboratório
            for arq in ["teste_antigo.txt", "teste_novo.txt", "diario.txt", "lista_compras.txt", "secreto.txt"]:
                if os.path.exists(arq): os.remove(arq)
            
            print("\nEncerrando Série de Laboratórios... Seus dados agora são eternos! 👋")
            break
            
        else:
            print("Opção inválida.")

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO DE ARQUIVOS (GLOSSÁRIO 12)".center(80))
        print("=" * 80)
        print("1. Abrindo Arquivos (O perigo do open sem close vs with)")
        print("2. Modos de Escrita (W apaga tudo vs A adiciona)")
        print("3. Leitura (read, readline, readlines)")
        print("4. Erros Comuns (FileNotFound)")
        print("5. Desafio Integrador: Bloco de Notas Persistente")
        print("0. Sair")
        print("=" * 80)
        
        opcao = input("\nEscolha o tópico para revisar: ")
        
        if opcao == '1': open_vs_with()
        elif opcao == '2': modos_escrita()
        elif opcao == '3': leitura()
        elif opcao == '4': erros_comuns()
        elif opcao == '5': desafio_logger()
        elif opcao == '0':
            # Limpeza final de segurança
            for arq in ["teste_antigo.txt", "teste_novo.txt", "diario.txt", "lista_compras.txt", "secreto.txt"]:
                if os.path.exists(arq): os.remove(arq)
            print("\nEncerrando... Até a próxima! 👋")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()