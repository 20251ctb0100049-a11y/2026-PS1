# ====================================================
# SISTEMA DE GESTÃO DE BIBLIOTECA
# ====================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisão: Estruturas de Dados
# Autor      : Rafael Lopes
# Data       : 05/03/2026
# Repositorio: https://github.com/20251ctb0100049-a11y/2026-PS
# ====================================================
# Descrição  : Sistema para cadastro e visualização de 
#              acervo bibliográfico utilizando Python.
# ====================================================

# --- 1. CONFIGURAÇÃO INICIAL DO CATÁLOGO ---
# Estrutura: Lista de Dicionários
catalogo = [
    {
        "titulo": "A Sociedade do Anel", 
        "autor": "J.R.R. Tolkien", 
        "ano": 1954, 
        "disponivel": True
    },
    {
        "titulo": "Cem Anos de Solidão", 
        "autor": "Gabriel García Márquez", 
        "ano": 1967, 
        "disponivel": False
    },
    {
        "titulo": "Duna", 
        "autor": "Frank Herbert", 
        "ano": 1965, 
        "disponivel": True
    }
]

# --- 2. EXIBIÇÃO DO RELATÓRIO ATUAL ---
print("="*40)
print("       RELATÓRIO ATUAL DO ACERVO")
print("="*40)

for livro in catalogo:
    # Operador ternário para formatar o status
    status = "Disponível" if livro["disponivel"] else "Emprestado"
    print(f"Livro: {livro['titulo']} | Autor: {livro['autor']}")
    print(f"Ano: {livro['ano']} | Status: {status}")
    print("-" * 30)

# --- 3. CADASTRO DE NOVO LIVRO ---
print("\n>>> CADASTRO DE NOVO EXEMPLAR")

# Coletando dados do usuário
novo_titulo = input("Digite o título do livro: ")
novo_autor  = input("Digite o nome do autor: ")
novo_ano    = int(input("Digite o ano de publicação: "))

# Criando o novo dicionário (seguindo a estrutura padrão)
novo_livro = {
    "titulo": novo_titulo,
    "autor": novo_autor,
    "ano": novo_ano,
    "disponivel": True # Por padrão, entra como disponível
}

# Adicionando à lista principal usando .append()
catalogo.append(novo_livro)

# --- 4. EXIBIÇÃO DO CATÁLOGO ATUALIZADO ---
print("\n" + "="*40)
print("    CATÁLOGO ATUALIZADO (PÓS-CADASTRO)")
print("="*40)

for livro in catalogo:
    status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
    print(f"{livro['titulo'].ljust(25)} | {status}")

print(f"\nTotal de livros no sistema: {len(catalogo)}")
print("="*40)