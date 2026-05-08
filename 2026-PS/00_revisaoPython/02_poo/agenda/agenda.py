"""
agenda.py - Aula 23 (programação de Sistemas, 2026)
Agenda de Contatos: classe inicial.
"""


class Contato:
 """Representa um contato simples na agenda."""

def __init__(self, nome, telefone, email):
    self.nome = nome
    self.telefone = telefone
    self.email = email

def exibir(self):
    print(f" Nome : {self.nome}")
    print(f" telefone : {self.telefone}")
    print(f" email : {self.email}")

Contato
# Teste rápido da classe
if __name__ == "__main__":
 c1 = Contato("Maria Silva", "42 99999-0001", "maria@email.com")
 c1.exibir()

 def menu():
    while True:
       print("\n======= AGENDA =======")
       print("1- Cadastrar contato")
       print("2- Listar contatos")
       print("0- Sair")
       opcao = input("Opção: ")

       if opcao == "1":
          print("(em breve: cadastrar)")
       elif opcao == "2":
          print("(em breve: listar)")
       elif opcao == "0":
          print("Até logo!")
          break
       else:
          print("Opção inválida.")


          if __name__ == "__main__":
             menu()

 def cadastrar(contatos):
    print("\n--- Novo contato --")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos.append(Contato(nome, telefone, email))
    print("✓ Contato cadastrado.")

 def listar(contatos):
    if not contatos:
       print("\n(agenda vazia)")
       return
    print(f"\n--- Agenda ({len(contatos)} contatos) ---")
    for i, c in enumerate(contatos, start=1):
       print(f"\n[{i}]")
       c.exibir()

 def remover(contatos):
    listar(contatos)
    if not contatos:
       return
    indice = int(input("\nNº  do contato a remover: ")) - 1
    if 0 <= indice < len(contatos):
        removido = contatos.pop(indice)
        print(f"✓ Contato '{removido.nome}' removido.")
    else:
        print("Índice inválido.")

 def salvar_em_txt(contatos, caminho):
    with open(caminho, "w", encoding="ut-8") as arquivo:
       for c in contatos:
          linha = f"{c.nome};{c.telefone};{c.email}"
          arquivo.write(linha + "\n")
    print(f"✓ {len(contatos)} contato(s) salvo(s) em {caminho}")

 def carregar_de_txt(caminho):
    contatos = []
    try:
       with open(caminho, "r", enconding="utf-8") as arquivo:
          for linha in arquivo:
             linha = linha.strip()
             if not linha:
                continue
             partes = linha.strip(";")
             nome, telefone, email = partes[0], partes[1], partes[2]
             contatos.append(Contato(nome, telefone, email))
    except FileNotFoundError:
       print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
    return contatos
 
 import pickle


 def salvar_em_binario(contatos, caminho):
    with open(caminho, "wb") as arquivo:
       pickle.dump(contatos, arquivo)
    print(f" {len(contatos)} contato(s) salvo(s) em {caminho}")


 def carregar_de_binario(caminho):
    try:
       with open(caminho, "rb") as arquivo:
          return pickle.load(arquivo)
    except FileNotFoundError:
       print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
       return[]