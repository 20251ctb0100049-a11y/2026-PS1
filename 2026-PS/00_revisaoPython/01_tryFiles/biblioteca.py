catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt",        "disponivel": True},
    {"titulo": "Código Limpo",             "autor": "Robert C. Martin",   "disponivel": False},
    {"titulo": "Padrões de Projeto",       "autor": "Erich Gamma",        "disponivel": True},
]

def listar_livros():
    """Exibe todos os livros com numeração e status."""
    print("\n" + "=" * 50)
    print("  📚CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)

    if not catalogo:
        print ("  Nenhum livro cadastrado.")
        return
    
    for i, livro in enumerate(catalogo, 1):
        status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
        print(f"  {i}. {livro['titulo']} - {livro['autor']} [{status}]")

    print("=" * 50)

    listar_livros()

def adicionar_livro():
    """Coleta dados via input e adiciona um novo livro ao catálogo."""
    print("\n--- Adicionar Novo Livro ---")

    titulo = input("Título: ").strip()
    autor = input("Autor : ").strip()

    if not titulo or not autor:
        print("⚠️  Título e autor são obrigatórios.")
        return

    catalogo.append({
        "titulo":      titulo,
        "autor":       autor,
        "disponivel":  True
    })
    print(f"✅ '{titulo}' adicionado com sucesso!")

def buscar_livro():
    print("\n--- Buscar Livro ---")
    termo = input("Digite parte do título: ").strip().lower()

    try:
        resultados = [l for l in catalogo if termo in l["titulo"].lower()]

        if not resultados:
            print(" Nenhum livro encontrado.")
            return

        print(f"\n {len(resultados)} resultado(s):")
        for livro in resultados:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f" • {livro['titulo']} - {livro['autor']} [{status}]")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

def registrar_emprestimo():
    listar_livros()
    if not catalogo:
        return
    
    print("\n--- Registrar Empréstimo ---")

    try:
        numero = int(input("Número do livro: "))  # ValueError se digitar letras

        if numero < 1 or numero > len(catalogo):
            print("⚠️  Número fora do intervalo.")
            return

        livro = catalogo[numero - 1]  # -1 porque lista começa em 0

        if not livro["disponivel"]:
            print(f"⚠️  '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False
            print(f"✅  Empréstimo de '{livro['titulo']}' registrado.")

    except ValueError:
        print("❌  Entrada inválida. Digite apenas o número.")

def devolver_livro():
    listar_livros()
    
    if not catalogo:
        return
        
    print("\n--- Registrar Devolução ---")
    
    try:
        numero = int(input("Número do livro a devolver: "))
        livro = catalogo[numero - 1] # IndexError se número for negativo ou > len
        
        if livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está disponível.")
        else:
            livro["disponivel"] = True
            print(f"✅ Devolução de '{livro['titulo']}' registrada.")
            
    except ValueError:
        print("❌ Digite apenas o número do livro.")
    except IndexError:
        print("❌ Número fora da lista. Verifique os livros cadastrados.")

def menu():
    print("\n📚 SISTEMA DE BIBLIOTECA - v1 (em memória)")

    opcoes = {
        "1": ("Listar livros",          listar_livros),
        "2": ("Adicionar livro",        adicionar_livro),
        "3": ("Buscar livro",           buscar_livro),
        "4": ("Registrar empréstimo",   registrar_emprestimo),
        "5": ("Devolver livro",        devolver_livro),
        "0": ("Sair",                   None),
    }

    while True:
        print("\n  Opções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"  [{chave}] {descricao}")

        try:
            escolha = input("\n  Sua escolha: ").strip()
            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")

        except ValueError as e:
            print(f"⚠️  {e}")
            continue      # volta ao while - não executa else/finally abaixo

        else:
            # Executado SOMENTE quando try termina sem exceção
            if escolha == "0":
                print("\n  Até logo! 📚")
                break

            _, funcao = opcoes[escolha]
            funcao()