# ====================================================
# Sistema de Biblioteca
# ====================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 10 - Atividade: Sistema de Biblioteca
# Autor      : RAFAEL LOPES PAZ OLIVEIRA PALHANO
# Data       : 24/03/2026
# Repositório: https://github.com/20251ctb0100049-a11y/2026-PS1
# ====================================================

ARQUIVO = "biblioteca.txt"
SEPARADOR = "|"

biblioteca = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt",        "disponivel": True},
    {"titulo": "Código Limpo",             "autor": "Robert C. Martin",   "disponivel": False},
    {"titulo": "Padrões de Projeto",       "autor": "Erich Gamma",        "disponivel": True},
]

def listar_livros(biblioteca):
    """Exibe todos os livros com numeração e status."""
    print("\n" + "=" * 50)
    print("  📚CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)

    if not biblioteca:
        print("  Nenhum livro cadastrado.")
        return
    
    for i, livro in enumerate(biblioteca, 1):
        status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
        print(f"  {i}. {livro['titulo']} - {livro['autor']} [{status}]")

    print("=" * 50)


def adicionar_livro(biblioteca):
    """Coleta dados via input e adiciona um novo livro ao catálogo."""
    print("\n--- Adicionar Novo Livro ---")

    titulo = input("Título: ").strip()
    autor = input("Autor : ").strip()

    if not titulo or not autor:
        print("⚠️  Título e autor são obrigatórios.")
        return

    biblioteca.append({
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    })
    salvar_biblioteca(biblioteca)
    print(f"✅ '{titulo}' adicionado com sucesso!")


def buscar_livro(biblioteca):
    print("\n--- Buscar Livro ---")
    termo = input("Digite parte do título: ").strip().lower()

    resultados = [l for l in biblioteca if termo in l["titulo"].lower()]

    if not resultados:
        print("Nenhum livro encontrado.")
        return

    print(f"\n {len(resultados)} resultado(s):")
    for livro in resultados:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f" • {livro['titulo']} - {livro['autor']} [{status}]")


def registrar_emprestimo(biblioteca):
    listar_livros(biblioteca)
    if not biblioteca:
        return
    
    print("\n--- Registrar Empréstimo ---")
    try:
        numero = int(input("Número do livro: "))
        if numero < 1 or numero > len(biblioteca):
            print("⚠️  Número fora do intervalo.")
            return

        livro = biblioteca[numero - 1]
        if not livro["disponivel"]:
            print(f"⚠️  '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False
            salvar_biblioteca(biblioteca)
            print(f"✅  Empréstimo de '{livro['titulo']}' registrado.")
    except ValueError:
        print("❌  Entrada inválida. Digite apenas o número.")


def devolver_livro(biblioteca):
    listar_livros(biblioteca)
    if not biblioteca:
        return
    
    print("\n--- Registrar Devolução ---")
    try:
        numero = int(input("Número do livro a devolver: "))
        livro = biblioteca[numero - 1]
        if livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está disponível.")
        else:
            livro["disponivel"] = True
            salvar_biblioteca(biblioteca)
            print(f"✅ Devolução de '{livro['titulo']}' registrada.")
    except ValueError:
        print("❌ Digite apenas o número do livro.")
    except IndexError:
        print("❌ Número fora da lista. Verifique os livros cadastrados.")


def carregar_biblioteca():
    """Lê o .txt e reconstrói a lista de dicionários."""
    catalogo = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(SEPARADOR)
                if len(partes) != 3:
                    continue
                titulo, autor, disponivel_str = partes
                catalogo.append({
                    "titulo": titulo,
                    "autor": autor,
                    "disponivel": disponivel_str == "True"
                })
    except FileNotFoundError:
        pass
    return biblioteca


def salvar_biblioteca(biblioteca):
    """Grava toda a lista no arquivo .txt."""
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for livro in biblioteca:
                linha = f"{livro['titulo']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponivel']}\n"
                f.write(linha)
        print(f"💾 Catálogo salvo em '{ARQUIVO}'.")
    except IOError as e:
        print(f"❌ Erro ao salvar: {e}")


def menu():
    catalogo = carregar_biblioteca()
    total = len(catalogo)
    print(f"\n📚 SISTEMA DE BIBLIOTECA – v2 (com persistência)")
    print(f"  {total} livro(s) carregado(s) de '{ARQUIVO}'.")

    opcoes = {
        "1": ("Listar livros", listar_livros),
        "2": ("Adicionar livro", adicionar_livro),
        "3": ("Buscar livro", buscar_livro),
        "4": ("Registrar empréstimo", registrar_emprestimo),
        "5": ("Devolver livro", devolver_livro),
        "0": ("Sair", None),
    }

    while True:
        print("\n  Opções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"  [{chave}] {descricao}")
        escolha = input("\n  Sua escolha: ").strip()
        if escolha not in opcoes:
            print(f"⚠️  Opção '{escolha}' inválida.")
            continue
        if escolha == "0":
            print("\n  Até logo! 🖐️")
            break
        _, funcao = opcoes[escolha]
        funcao(biblioteca)


if __name__ == "__main__":
    menu()