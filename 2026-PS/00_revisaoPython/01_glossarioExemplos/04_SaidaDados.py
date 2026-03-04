# -*- coding: utf-8 -*-
"""
==============================================================================
ARQUIVO: 04_SaidaDados.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo sobre Saída de Dados (print) e Formatação.
    Baseado integralmente no "Glossário 05 - Saída de Dados".

CONTEÚDO PROGRAMÁTICO:
    1. Conceito: A função print() como a "voz" do programa.
    2. Métodos de Formatação: f-strings (Recomendado) vs .format() vs Concatenação.
    3. Formatação Numérica: Casas decimais (.2f), alinhamento e porcentagem.
    4. Parâmetros Especiais: sep (separador) e end (final de linha).
    5. Caracteres de Escape: \n (nova linha), \t (tabulação).
    6. Exemplo Integrador: Gerador de Nota Fiscal.

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
# TÓPICO 1: O BÁSICO DE PRINT E CONCATENAÇÃO
# ==============================================================================
def basico_print():
    limpar_tela()
    print("🔹 TÓPICO 1: O BÁSICO DE PRINT")
    print("-" * 80)
    print("A função print() exibe informações no console.")
    print("Podemos imprimir textos, números, variáveis ou o resultado de expressões.")
    print("-" * 80)

    # Exemplo cobrindo tipos básicos e o problema da concatenação
    codigo = """nome = "Python"
versao = 3.12

# 1. Imprimindo literais e variáveis
print("Olá, mundo!")
print(nome)

# 2. Vários argumentos (A vírgula adiciona um espaço automático)
print("Linguagem:", nome, "| Versão:", versao)

# 3. Concatenação com + (CUIDADO!)
# print("Versão: " + versao)  # ERRO! Não soma texto com número.
print("Versão: " + str(versao))  # Correção: Converter número para texto"""

    mostrar_codigo_didatico(codigo)

    executar_linha(1); executar_linha(2)
    print("   ↳ MEMÓRIA: Dados armazenados.")

    executar_linha(5)
    print("   ↳ SAÍDA: Olá, mundo!")

    executar_linha(6)
    print("   ↳ SAÍDA: Python")

    executar_linha(9)
    print("   ↳ LÓGICA: A vírgula ',' insere um espaço entre os itens.")
    print("   ↳ SAÍDA: Linguagem: Python | Versão: 3.12")

    executar_linha(12)
    print("   ↳ ERRO EVITADO: Tentativa de somar string com float geraria TypeError.")
    
    executar_linha(13)
    print("   ↳ CORREÇÃO: str(versao) transforma 3.12 em '3.12' para juntar.")
    print("   ↳ SAÍDA: Versão: 3.12")
    
    esperar()

# ==============================================================================
# TÓPICO 2: F-STRINGS (A FORMA MODERNA)
# ==============================================================================
def f_strings():
    limpar_tela()
    print("🔹 TÓPICO 2: F-STRINGS (RECOMENDADO)")
    print("-" * 80)
    print("Introduzidas no Python 3.6, são a forma mais legível de formatar.")
    print("Sintaxe: f\"Texto {variavel}\"")
    print("Basta colocar um 'f' antes das aspas e usar chaves {}.")
    print("-" * 80)
    
    # Baseado no Exemplo 4 do Glossário
    codigo = """produto = "Notebook"
preco = 3500.00

# Sem f-string (Trabalhoso e confuso):
print("O " + produto + " custa R$ " + str(preco))

# Com f-string (Limpo e direto):
print(f"O {produto} custa R$ {preco}")

# É possível fazer cálculos DENTRO das chaves!
print(f"O dobro do preço é R$ {preco * 2}")
print(f"É caro? {preco > 5000}")"""

    mostrar_codigo_didatico(codigo)

    executar_linha(1); executar_linha(2)
    
    executar_linha(5)
    print("   ↳ SAÍDA: O Notebook custa R$ 3500.0")
    
    executar_linha(8)
    print("   ↳ PROCESSAMENTO: O Python substitui {produto} e {preco} pelos valores.")
    print("   ↳ SAÍDA: O Notebook custa R$ 3500.0")
    
    executar_linha(11)
    print("   ↳ CÁLCULO: 3500.0 * 2 = 7000.0 (Feito dentro do print)")
    print("   ↳ SAÍDA: O dobro do preço é R$ 7000.0")
    
    executar_linha(12)
    print("   ↳ LÓGICA: 3500 > 5000? False")
    print("   ↳ SAÍDA: É caro? False")
    
    esperar()

# ==============================================================================
# TÓPICO 3: FORMATAÇÃO NUMÉRICA E ALINHAMENTO
# ==============================================================================
def formatacao_numerica():
    limpar_tela()
    print("🔹 TÓPICO 3: FORMATAÇÃO NUMÉRICA")
    print("-" * 80)
    print("Podemos controlar como os números aparecem usando códigos após ':'")
    print("   :.2f  -> 2 casas decimais (padrão monetário)")
    print("   :10   -> Reserva 10 espaços (Alinhamento)")
    print("   :^10  -> Centralizar")
    print("-" * 80)
    
    # Baseado no Exemplo 8 do Glossário
    codigo = """valor = 1234.56789
taxa = 0.156

# Formatação de Casas Decimais (.2f = 2 float points)
print(f"Valor normal: {valor}")
print(f"Valor fixo:   {valor:.2f}")  # Arredonda para 1234.57

# Formatação de Porcentagem (.1%)
print(f"Taxa: {taxa:.1%}")           # Multiplica por 100 e põe %

# Alinhamento e Preenchimento (Útil para tabelas)
print(f"|{valor:15}|")      # Reserva 15 espaços
print(f"|{valor:^15}|")     # Centraliza em 15 espaços"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1); executar_linha(2)
    
    executar_linha(5)
    print("   ↳ SAÍDA: Valor normal: 1234.56789")
    
    executar_linha(6)
    print("   ↳ FORMATADOR: .2f arredonda 567... para .57")
    print("   ↳ SAÍDA: Valor fixo:   1234.57")
    
    executar_linha(9)
    print("   ↳ FORMATADOR: .1% converte 0.156 para 15.6%")
    print("   ↳ SAÍDA: Taxa: 15.6%")
    
    executar_linha(12)
    print("   ↳ SAÍDA: |     1234.56789| (Alinhado à direita por padrão)")
    
    executar_linha(13)
    print("   ↳ SAÍDA: |  1234.56789   | (Centralizado)")
    
    esperar()

# ==============================================================================
# TÓPICO 4: PARÂMETROS SEP E END
# ==============================================================================
def parametros_especiais():
    limpar_tela()
    print("🔹 TÓPICO 4: PARÂMETROS SEP E END")
    print("-" * 80)
    print("O print() tem parâmetros opcionais que controlam a saída:")
    print("   sep=' ' -> O que separa os valores (Padrão: espaço)")
    print("   end='\\n' -> O que vai no final (Padrão: nova linha)")
    print("-" * 80)
    
    # Baseado no Exemplo 6 do Glossário
    codigo = """# Usando SEP (Separador)
print("Dia", "Mês", "Ano", sep="/")
print("Python", "Java", "C", sep=" -> ")

# Usando END (Final de linha)
# Por padrão, print pula linha. Podemos mudar isso.
print("Carregando", end="...")
time.sleep(1)
print("100%", end="!")
print(" Concluído.")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(2)
    print("   ↳ SAÍDA: Dia/Mês/Ano")
    
    executar_linha(3)
    print("   ↳ SAÍDA: Python -> Java -> C")
    
    print("\n   [Testando END - Observe que não pula linha]")
    executar_linha(7)
    print("   ↳ SAÍDA (parcial): Carregando...", end="") # Simula o comportamento real
    
    executar_linha(8)
    # Efeito visual
    
    executar_linha(9)
    print("100%!", end="")
    
    executar_linha(10)
    print(" Concluído.")
    
    print("\n   (Tudo acima apareceu na mesma linha visualmente)")
    esperar()

# ==============================================================================
# TÓPICO 5: CARACTERES DE ESCAPE
# ==============================================================================
def caracteres_escape():
    limpar_tela()
    print("🔹 TÓPICO 5: CARACTERES ESPECIAIS (ESCAPE)")
    print("-" * 80)
    print("A barra invertida (\\) avisa que o próximo caractere é especial.")
    print("   \\n -> New Line (Quebra de linha)")
    print("   \\t -> Tabulação (Espaçamento de tabela)")
    print("   \\\" -> Imprimir aspas dentro de aspas")
    print("-" * 80)
    
    # Baseado no Exemplo 7 do Glossário
    codigo = """print("Linha 1\\nLinha 2")
print("Nome\\tIdade\\tNota")
print("Ana\\t18\\t9.5")
print("Ela disse: \\"Estude Python!\\"")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    print("   ↳ SAÍDA:\n     Linha 1\n     Linha 2")
    
    executar_linha(2)
    print("   ↳ SAÍDA: Nome    Idade   Nota")
    
    executar_linha(3)
    print("   ↳ SAÍDA: Ana     18      9.5")
    
    executar_linha(4)
    print('   ↳ SAÍDA: Ela disse: "Estude Python!"')
    
    esperar()

# ==============================================================================
# TÓPICO 6: EXEMPLO INTEGRADOR (NOTA FISCAL)
# ==============================================================================
def desafio_nota_fiscal():
    limpar_tela()
    print("🔹 DESAFIO FINAL: GERADOR DE NOTA FISCAL")
    print("Integra: Input, Cálculos, F-Strings, Alinhamento e Decimais.")
    print("-" * 80)
    
    # Exemplo 10 do Glossário
    codigo_ref = """produto = input("Produto: ")
val = float(input("Valor: "))
qtd = int(input("Qtd: "))
total = val * qtd

print(f"{'='*30}")
print(f"{'NOTA FISCAL':^30}")
print(f"{'='*30}")
print(f"Item: {produto.upper():<20}")
print(f"Qtd:  {qtd:>20}")
print(f"Unit: R$ {val:>17.2f}")
print(f"{'-'*30}")
print(f"TOTAL:R$ {total:>17.2f}")"""
    
    mostrar_codigo_didatico(codigo_ref)
    
    try:
        print("\n⚙️  [Coletando Dados]...")
        produto = input("   Nome do Produto: ")
        val = float(input("   Valor Unitário: "))
        qtd = int(input("   Quantidade: "))
        
        # Processamento
        total = val * qtd
        
        print("\n⚙️  [Imprimindo Nota Fiscal Formatada]...\n")
        time.sleep(1)
        
        # Simulação da execução das linhas de print formatadas
        print(f"{'='*35}")
        print(f"{'NOTA FISCAL':^35}")
        print(f"{'='*35}")
        # :<20 alinha à esquerda em 20 espaços
        print(f"Item: {produto.upper():<25}") 
        # :>25 alinha à direita em 25 espaços
        print(f"Qtd:  {qtd:>25}")
        # :>22.2f alinha à direita e fixa 2 decimais
        print(f"Unit: R$ {val:>22.2f}")
        print(f"{'-'*35}")
        print(f"TOTAL:R$ {total:>22.2f}")
        print(f"{'='*35}")
            
    except ValueError:
        print("\n❌ ERRO: Valor e Quantidade devem ser números!")
        
    esperar()

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO DE SAÍDA DE DADOS (GLOSSÁRIO 05)".center(80))
        print("=" * 80)
        print("1. O Básico de print() e Erros de Concatenação")
        print("2. F-Strings (Formatação Moderna)")
        print("3. Formatação Numérica (Moeda, Porcentagem, Alinhamento)")
        print("4. Parâmetros Especiais (sep e end)")
        print("5. Caracteres de Escape (\\n, \\t)")
        print("6. Desafio Integrador: Nota Fiscal")
        print("0. Sair")
        print("=" * 80)
        
        print("\n💡 DICA: Prefira sempre f-strings (f\"...\") ao invés de usar +")
        
        opcao = input("\nEscolha o tópico para revisar: ")
        
        if opcao == '1': basico_print()
        elif opcao == '2': f_strings()
        elif opcao == '3': formatacao_numerica()
        elif opcao == '4': parametros_especiais()
        elif opcao == '5': caracteres_escape()
        elif opcao == '6': desafio_nota_fiscal()
        elif opcao == '0':
            print("\nEncerrando laboratório... Lembre-se do 'f' antes das aspas! 👋")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()