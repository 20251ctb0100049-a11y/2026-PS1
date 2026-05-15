import pickle
import os

# ====================================================
# CLASSE PET (Original Aula 20)
# ====================================================
class Pet:
    def __init__(self, nome, especie, raca, idade, peso, nome_dono, vacinado=False):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = int(idade)
        self.peso = float(peso)
        self.nome_dono = nome_dono
        self.vacinado = vacinado
        self.hospedado = False

    def exibir_dados(self):
        print("\n" + "="*35)
        print(f"FICHA DO PET: {self.nome.upper()}")
        print(f"Espécie: {self.especie} | Raça: {self.raca}")
        print(f"Idade: {self.idade} anos | Peso: {self.peso}kg")
        print(f"Dono(a): {self.nome_dono}")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Hospedado agora: {'Sim' if self.hospedado else 'Não'}")
        print("="*35)

    def registrar_entrada(self):
        if self.hospedado:
            print(f"Aviso: {self.nome} já está hospedado!")
        else:
            self.hospedado = True
            print(f"✓ Check-in: {self.nome} entrou no hotel.")

    def registrar_saida(self):
        if not self.hospedado:
            print(f"Erro: {self.nome} não está no hotel.")
        else:
            self.hospedado = False
            print(f"✓ Check-out: {self.nome} saiu do hotel.")

    def atualizar_peso(self, novo_peso):
        self.peso = float(novo_peso)
        print(f"✓ Peso de {self.nome} atualizado para {self.peso}kg.")

# ====================================================
# FUNÇÕES DE PERSISTÊNCIA (TXT E BINÁRIO)
# ====================================================

def salvar_dados(lista):
    """Salva em Binário (para o Python) e em TXT (para humanos)."""
    # 1. Salvar em Binário (Pickle) - Nível B
    with open("petville_dados.bin", "wb") as f_bin:
        pickle.dump(lista, f_bin)
    
    # 2. Salvar em TXT (Texto Simples) - Nível C
    with open("petville_lista.txt", "w", encoding="utf-8") as f_txt:
        f_txt.write("RELATÓRIO DE PETS - HOTEL PETVILLE\n")
        f_txt.write("="*40 + "\n")
        for p in lista:
            status = "Hospedado" if p.hospedado else "Em Casa"
            f_txt.write(f"Pet: {p.nome} | Espécie: {p.especie} | Peso: {p.peso}kg | Status: {status}\n")
    
    print("\n[SISTEMA] Dados salvos em 'petville_dados.bin' e 'petville_lista.txt'!")

def carregar_dados():
    """Tenta carregar o binário, se não existir, retorna lista vazia."""
    if os.path.exists("petville_dados.bin"):
        with open("petville_dados.bin", "rb") as f:
            return pickle.load(f)
    return []

# ====================================================
# MENU PRINCIPAL
# ====================================================

def menu():
    pets = carregar_dados()
    
    while True:
        print("\n--- 🐾 PETVILLE: MENU DE RECEPÇÃO ---")
        print("1. Cadastrar Pet")
        print("2. Listar Pets (Fichas)")
        print("3. Check-in (Entrada)")
        print("4. Check-out (Saída)")
        print("5. Atualizar Peso")
        print("0. Sair e Salvar Tudo")
        
        op = input("\nEscolha uma opção: ")

        if op == "1":
            n = input("Nome: ")
            e = input("Espécie: ")
            r = input("Raça: ")
            i = input("Idade: ")
            p = input("Peso: ")
            d = input("Dono: ")
            v = input("Vacinado? (s/n): ").lower() == 's'
            pets.append(Pet(n, e, r, i, p, d, v))
            print("✓ Cadastrado!")

        elif op == "2":
            if not pets: print("\n[Agenda vazia]")
            for p in pets: p.exibir_dados()

        elif op == "3":
            nome = input("Nome do pet para entrada: ")
            for p in pets:
                if p.nome.lower() == nome.lower(): p.registrar_entrada()

        elif op == "4":
            nome = input("Nome do pet para saída: ")
            for p in pets:
                if p.nome.lower() == nome.lower(): p.registrar_saida()

        elif op == "5":
            nome = input("Nome do pet: ")
            for p in pets:
                if p.nome.lower() == nome.lower():
                    np = input("Novo peso: ")
                    p.atualizar_peso(np)

        elif op == "0":
            salvar_dados(pets)
            print("Sistema encerrado com segurança.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()