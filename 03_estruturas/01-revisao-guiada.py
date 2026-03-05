# ====================================================
# SISTEMA DE APROVAÇÃO DE ALUNOS 
# ====================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisao: Estruturas de Dados
# Autor      : RAFAEL LOPES PAZ OLIVEIRA PALHANO
# Data       : 05/03/2026
# Repositório: https://github.com/20251ctb0100049-a11y/2026-PS
# ====================================================
#
# DESCRIÇÃO:
# Catálogo de livros que demonstra o uso de listas e dicionários para armazenar, consultar e filtrar dados estruturados.
# ====================================================

# ---- LISTAS: CONCEITO BÁSICO ----

# Criando uma lista de títulos
titulos = [
  "O Programador Pragmático",
  "Código Limpo",
  "Entendendo Algoritmos",
]
# Acesso por índice (começa em 0, não em 1!)
print("Primeiro livro:", titulos[0])
print("Último livro :", titulos[-1])    # índice -1 = último elemento
print("Total de livros:", len(titulos))

# ---- MÉTODOS DE LISTA ----

print("\n--- Operações na lista ---")

# Adicionar um item ao final
titulos.append("Python Fluente")
print("Após append:", titulos)

# Verificar se um item existe
busca = "Código Limpo"
if busca in titulos:
  print(f'"{busca}" está no catálogo.')
else:
  print(f'"{busca}" não encontrado.')

# Ordenar a lista
titulos.sort()
print("Lista ordenada:", titulos)

# Remover um item
titulos.remove("Entendendo Algoritmos")
print("Após remove:", titulos)

# ---- DICIONÁRIOS: CONCEITO BÁSICO ----

# Um dicionário representa um livro com seus atributos
livro = {
"titulo":         "O Programador Pragmático",
"autor":          "Andrew Hunt",
"ano":            1999,                       # int, não string
"disponivel":     True,                      # bool

}

# Acessando valores pelas chaves
print("Título :", livro ["titulo"])
print("Autor :", livro ["autor"])
print("Ano :", livro["ano"])
print("Status :", "Disponível" if livro ["disponivel"] else "Emprestado")

# ---- MODIFICANDO E CONSULTANDO ----

# Atualizando um valor existente
livro ["disponivel"] = False # livro foi emprestado
print("\nApós empréstimo:", livro["disponivel"])

# Adicionando uma nova chave
livro ["paginas"] = 352
print("Páginas:", livro["paginas"])

#.get() acesso seguro: retorna None (ou padrão) se a chave não existir
editora = livro.get("editora", "Não informada")
print("Editora:", editora) # não lança KeyError, retorna o padrão

# ---- CATÁLOGO: LISTA DE DICIONÁRIOS ----
catalogo = [
   {"titulo": "0 Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999,
"disponivel": True},
   {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008,
"disponivel": False},
   {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2016,
"disponivel": True},
]

print("=== Catálogo da Biblioteca ===")
print()
# Percorrendo cada livro com for
for livro in catalogo:
   status = "Disponível" if livro["disponivel"] else "Emprestado"
   print(f' {livro["titulo"]} ({livro ["ano"]})')
   print(f' Autor: {livro ["autor"]} | {status}')
   print(" " + "" * 40)

# ---- CONSULTAS E FILTROS ----

print("\n=== Livros disponíveis ===")
for livro in catalogo:
    if livro["disponivel"]: # filtra apenas os disponíveis
        print(f' ✅ {livro["titulo"]}')

print("\n=== Busca por título ===")
busca = input("Digite o título (ou parte): ").lower()
encontrado = False

for livro in catalogo:
    if busca in livro["titulo"].lower(): # .lower() ignora maiúsculas/minúsculas
        print(f' Encontrado: {livro["titulo"]} - {livro["autor"]}')
        encontrado = True

if not encontrado:
    print(" Nenhum livro encontrado com esse termo.")

print("\n=== Atributos do primeiro livro ===")
for chave, valor in catalogo[0].items(): # .items() retorna pares chave:valor
    print(f" {chave}: {valor}")

catalogo = [
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel": False},
    {"titulo": "Python Fluente", "autor": "Luciano Ramalho", "disponivel": True},
]

print("Primeiro livro:", catalogo[0]["titulo"])

print("\nLivros disponíveis:")
for livro in catalogo:
    if livro["disponivel"] == True:
        print(f'- ✅ {livro["titulo"]}')

total = len(catalogo)
print(f"\nTotal de livros: {total}")

for chave, valor in catalogo[0].items():
    print(f"{chave}: {valor}")

primeiro_autor = catalogo[0]["autor"]
print("\nAutor do primeiro livro:", primeiro_autor)
