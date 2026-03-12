""""
==============================================================================
ARQUIVO: 01_Comentarios.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Laboratório interativo sobre Comentários e Documentação em Python.
    Baseado integralmente no "Glossário 02 - Comentários".

CONTEÚDO PROGRAMÁTICO:
    1. Conceito e Analogia (Anotações na margem).
    2. Sintaxe: Linha (#) vs Bloco (Aspas Triplas).
    3. Docstrings e a função help().
    4. Boas Práticas e Erros Comuns (O Que vs O Porquê).
    5. Uso Estratégico: Debugging, TODO e FIXME.
    6. Exemplo Integrador: Conversor de Temperatura.

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
# TÓPICO 1: O QUE SÃO E SINTAXE BÁSICA
# ==============================================================================
def conceito_sintaxe():
    limpar_tela()
    print("🔹 TÓPICO 1: O QUE SÃO COMENTÁRIOS?")
    print("-" * 80)
    print("Definição: Trechos de texto IGNORADOS pelo interpretador Python.")
    print("Objetivo: Servem para humanos, não para a máquina.")
    print("\n🎯 ANALOGIA DO GLOSSÁRIO:")
    print("   'São como anotações a lápis na margem de um livro. Ajudam a lembrar")
    print("    o significado, mas não mudam o conteúdo do livro.'")
    print("-" * 80)

    # Exemplo cobrindo: Comentário de Linha e Inline (Exemplos 1 e 2 do Glossário)
    codigo = """# Este é um comentário de linha inteira: O Python pula esta linha.
print("Olá, estudante!")  # Este é um comentário inline (após o código).

# Abaixo, definimos variáveis com comentários explicando o significado:
taxa = 0.05  # Taxa de juros (5%)
meses = 12   # Período em meses"""

    mostrar_codigo_didatico(codigo)

    executar_linha(1, atraso=0.5)
    print("   ↳ INTERPRETADOR: 'Linha começa com #. Ignorando...'")

    executar_linha(2)
    print("   ↳ SAÍDA: Olá, estudante!")
    print("   ↳ INTERPRETADOR: 'Ignorou o texto após o # na mesma linha.'")

    executar_linha(4, atraso=0.5) # Linha vazia/comentário

    executar_linha(5)
    print("   ↳ MEMÓRIA: Variável 'taxa' definida como 0.05.")

    executar_linha(6)
    print("   ↳ MEMÓRIA: Variável 'meses' definida como 12.")
    
    esperar()

# ==============================================================================
# TÓPICO 2: COMENTÁRIOS DE BLOCO E DOCSTRINGS
# ==============================================================================
def bloco_docstrings():
    limpar_tela()
    print("🔹 TÓPICO 2: BLOCOS E DOCSTRINGS (DOCUMENTAÇÃO)")
    print("-" * 80)
    print("Existem duas formas de comentar múltiplas linhas:")
    print("1. Blocos de # (Mais comum para explicar lógica).")
    print("2. Aspas Triplas \"\"\"...\"\"\" (Usado para DOCSTRINGS/Documentação).")
    
    # Exemplo baseado no Exemplo 5 do Glossário
    codigo = """def calcular_media(n1, n2):
    \"\"\"
    Calcula a média aritmética de dois números.
    
    Parâmetros:
        n1 (float): Primeira nota
        n2 (float): Segunda nota
    \"\"\"
    return (n1 + n2) / 2

# Acessando a documentação oficial da função:
print(calcular_media.__doc__)"""

    mostrar_codigo_didatico(codigo)

    print("ℹ️  NOTA: As linhas 02 a 07 formam a DOCSTRING da função.")
    
    executar_linha(1)
    print("   ↳ SISTEMA: Função 'calcular_media' registrada na memória.")
    
    executar_linha(11)
    print("\n>>> SAÍDA DO HELP/DOCSTRING:")
    print("-" * 40)
    print("    Calcula a média aritmética de dois números.")
    print("    ")
    print("    Parâmetros:")
    print("        n1 (float): Primeira nota")
    print("        n2 (float): Segunda nota")
    print("-" * 40)
    
    print("\n💡 DICA: Use a função help(nome_da_funcao) no terminal para ver isso!")
    esperar()

# ==============================================================================
# TÓPICO 3: BOAS PRÁTICAS E ERROS COMUNS
# ==============================================================================
def boas_praticas():
    limpar_tela()
    print("🔹 TÓPICO 3: BOAS PRÁTICAS E ERROS COMUNS")
    print("-" * 80)
    
    print("✅ REGRA DE OURO:")
    print("   'Comentários explicam o PORQUÊ (Motivo), não o O QUÊ (Óbvio).'")
    print("\n⚠️ ERROS COMUNS (Glossário):")
    print("   1. Esquecer o espaço após a cerquilha (#Texto vs # Texto).")
    print("   2. Deixar comentários desatualizados (MENTIROSOS).")
    print("-" * 80)

    codigo = """# ❌ RUIM (Explica o óbvio):
x = 10  # Atribui 10 a x

# ✅ BOM (Explica a Regra de Negócio):
x = 10  # Máximo de tentativas de login permitidas

# ⚠️ PERIGO (Comentário MENTIROSO/Desatualizado):
# Calcula a média de 2 notas (MENTIRA! O código usa 3)
media = (n1 + n2 + n3) / 3"""

    mostrar_codigo_didatico(codigo)
    
    print("ANÁLISE CRÍTICA:")
    time.sleep(1)
    print("\n1. Nas linhas 01-02: O comentário é inútil. Qualquer um sabe que x recebe 10.")
    print("2. Nas linhas 04-05: O comentário agrega valor explicando O QUE É o 10.")
    print("3. Nas linhas 08-09: O comentário diz '2 notas', mas o código divide por 3.")
    print("   --> ISSO GERA BUGS! Um comentário errado é pior que nenhum comentário.")
    
    esperar()

# ==============================================================================
# TÓPICO 4: USO ESTRATÉGICO (DEBUG, TODO, FIXME)
# ==============================================================================
def uso_estrategico():
    limpar_tela()
    print("🔹 TÓPICO 4: USO ESTRATÉGICO (Depuração e Tags)")
    print("-" * 80)
    
    # Exemplo combinando Exemplo 6 (Debug) e Exemplo 9 (TODO) do Glossário
    codigo = """# Exemplo de Debugging (Comentar para desativar):
valor = 100
# valor = 200  # Linha desativada para teste
print(f"Valor: {valor}")

# Exemplo de Tags para IDEs:
# TODO: Implementar validação se valor for negativo
# FIXME: Corrigir erro de arredondamento na linha 10"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(2)
    print("   ↳ MEMÓRIA: valor = 100")
    
    executar_linha(3)
    print("   ↳ INTERPRETADOR: Ignorou a redefinição para 200.")
    
    executar_linha(4)
    print("   ↳ SAÍDA: Valor: 100")
    
    print("\n📌 NOTA SOBRE TAGS:")
    print("   IDEs como VS Code e PyCharm destacam 'TODO' (A fazer) e")
    print("   'FIXME' (Corrigir-me) em cores diferentes para alertar o programador.")
    
    esperar()

# ==============================================================================
# TÓPICO 5: EXEMPLO INTEGRADOR (TEMPERATURA)
# ==============================================================================
def exemplo_completo():
    limpar_tela()
    print("🔹 TÓPICO 5: EXEMPLO COMPLETO (CONVERSOR DE TEMPERATURA)")
    print("Este código segue o padrão profissional do Glossário.")
    print("-" * 80)
    
    # Exemplo 10 do Glossário
    codigo = """def celsius_para_fahrenheit(c):
    \"\"\"Converte C para F usando a fórmula: F = C * 9/5 + 32\"\"\"
    return c * 9 / 5 + 32

# ---- PROGRAMA PRINCIPAL ----
# Solicita entrada (Input sempre retorna string, convertemos para float)
temp_c = float(input("Digite °C: "))

# Processamento
temp_f = celsius_para_fahrenheit(temp_c)

# Saída Formatada
print(f"Fahrenheit: {temp_f:.1f} °F")"""

    mostrar_codigo_didatico(codigo)
    
    executar_linha(1)
    print("   ↳ SISTEMA: Função de conversão definida.")
    
    executar_linha(6) # Pula comentários de seção
    try:
        temp_c = float(input("   ↳ AÇÃO USUÁRIO (Digite uma temperatura, ex: 25): "))
    except:
        temp_c = 25.0
        print("   (Valor padrão 25.0 assumido)")

    executar_linha(9)
    print("   ↳ CHAMADA DE FUNÇÃO: Executando cálculo (25 * 9/5 + 32)...")
    temp_f = temp_c * 9 / 5 + 32
    print(f"   ↳ RETORNO: {temp_f}")
    
    executar_linha(12)
    print(f"   ↳ SAÍDA: Fahrenheit: {temp_f:.1f} °F")
    
    esperar()

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================
def menu_principal():
    while True:
        limpar_tela()
        print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
        print("LABORATÓRIO DE COMENTÁRIOS (GLOSSÁRIO 02)".center(80))
        print("=" * 80)
        print("1. Conceito e Sintaxe Básica (Linha vs Inline)")
        print("2. Blocos e Docstrings (Documentação)")
        print("3. Boas Práticas e Erros Comuns")
        print("4. Uso Estratégico (Debug, TODO, FIXME)")
        print("5. Exemplo Completo (Conversor de Temperatura)")
        print("0. Sair")
        print("=" * 80)
        
        print("\n💡 DICA DO PROFE (Atalhos):")
        print("   VS Code/PyCharm: Use 'Ctrl + /' para comentar/descomentar linhas.")
        
        opcao = input("\nEscolha o tópico para revisar: ")
        
        if opcao == '1': conceito_sintaxe()
        elif opcao == '2': bloco_docstrings()
        elif opcao == '3': boas_praticas()
        elif opcao == '4': uso_estrategico()
        elif opcao == '5': exemplo_completo()
        elif opcao == '0':
            print("\nEncerrando laboratório... Lembre-se: Código bom é autoexplicativo! 👋")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()