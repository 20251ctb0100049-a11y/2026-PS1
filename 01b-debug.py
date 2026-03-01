# Arquivo: 01b-debug.py
# CORRIGIDO: Agora o código funciona perfeitamente!

nome = input("Digite o nome do aluno: ") # Erro 1 corrigido: imput -> input
nota1 = float(input("Digite a nota 1: ")) # Erro 2 corrigido: notal -> nota1
nota2 = float(input("Digite a nota 2: "))

# Erro 3 corrigido: Adicionado parênteses para garantir a precedência da soma
media = (nota1 + nota2) / 2

if media >= 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Erro 4 corrigido: pront -> print
print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")


# ==========================================================
# SISTEMA DE BIBLIOTECA
# ==========================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados
# Autor      : Rafael Lopes
# Data       : 26/02/2026
# Repositório: https://github.com/20251ctb0100049-a11y/2026-PS1
# ==========================================================
# DESCRIÇÃO:
# Catálogo de livros que demonstra o uso de listas
# e dicionários para armazenar, consultar e filtrar
# dados estruturados.
# ==========================================================

# Lista para armazenar o catálogo de livros (cada livro é um dicionário)
catalogo = []

def adicionar_livro(titulo, autor, ano):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }
    catalogo.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")

def listar_livros():
    print("\n--- Catálogo Atual ---")
    for livro in catalogo:
        print(f"Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']}")

def filtrar_por_autor(nome_autor):
    print(f"\n--- Livros de: {nome_autor} ---")
    resultados = [l for l in catalogo if l['autor'].lower() == nome_autor.lower()]
    
    if resultados:
        for r in resultados:
            print(f"- {r['titulo']} ({r['ano']})")
    else:
        print("Nenhum livro encontrado para este autor.")

# --- Exemplo de Uso ---
adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
adicionar_livro("O Hobbit", "J.R.R. Tolkien", 1937)
adicionar_livro("Memórias Póstumas", "Machado de Assis", 1881)

listar_livros()
filtrar_por_autor("Machado de Assis")

# ---- LISTAS: CONCEITO BÁSICO ----

# Criando uma lista de títulos de livros
titulos = [
    "O Programador Pragmático",
    "Código Limpo",
    "Entendendo Algoritmos",
]

# Acesso por índice (Lembre-se: em Python, a contagem começa em 0!)
print("Primeiro livro:", titulos[0])

# O índice -1 é um atalho prático para acessar o último item da lista
print("Último livro :", titulos[-1])

# A função len() retorna a quantidade total de itens na lista
print("Total de livros:", len(titulos))

# ---- MÉTODOS DE LISTA ----

print("\n--- Operações na lista ---")

# Adicionar um item ao final
titulos.append("Python Fluente")
print("Após append:", titulos)

# Verificar se um item existe
busca = "Código Limpo"
if busca in titulos:
    print(f"'{busca}' está no catálogo.")
else:
    print(f"'{busca}' não encontrado.")

# Ordenar a lista
titulos.sort()
print("Lista ordenada:", titulos)

# Remover um item
titulos.remove("Entendendo Algoritmos")
print("Após remove:", titulos)
