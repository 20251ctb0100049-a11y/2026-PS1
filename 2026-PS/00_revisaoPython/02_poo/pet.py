'''
====================================================
# ARQUIVO    : pet.py
# Disciplina : Programação de Sistemas
# Aula       : Aula 20 - Por que POO?
# Autor      : Rafael Lopes Paz Oliveira Palhano (Modificado)
# Conceitos  : Classe, objeto, Atributos, métodos, encapsulamento
# Atividade  : Classe Pet Completa
====================================================
'''
class Pet:
    '''
    Esta classe representa um Pet em um sistema simples de hotel para pets.
    '''
    def __init__(self, nome, especie, raca, idade, peso, nome_dono, vacinado=False):

        '''
        Método construtor atualizado com novos atributos.
        '''

        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.peso = peso
        self.nome_dono = nome_dono
        self.vacinado = vacinado
        self.hospedado = False



    def exibir_dados(self):

        '''Exibe os dados detalhados do pet.'''

        print("\n" + "="*30)
        print(f"FICHA DO PET: {self.nome.upper()}")
        print(f"Espécie: {self.especie} | Raça: {self.raca}")
        print(f"Idade: {self.idade} anos | Peso: {self.peso}kg")
        print(f"Dono(a): {self.nome_dono}")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Hospedado agora: {'Sim' if self.hospedado else 'Não'}")
        print("="*30)



    def registrar_entrada(self):

        '''Registra a entrada verificando se já não está no hotel.'''

        if self.hospedado:
            print(f"Aviso: {self.nome} já está hospedado no momento!")
        else:
            self.hospedado = True
            print(f"Check-in realizado: {self.nome} entrou no hotel.")
    def registrar_saida(self):

        '''Registra a saída verificando se o pet realmente estava lá.'''

        if not self.hospedado:
            print(f"Erro: {self.nome} não pode sair pois não está hospedado.")
        else:
            self.hospedado = False
            print(f"Check-out realizado: {self.nome} saiu do hotel. Volte sempre!")



    def calcular_diaria(self):

        '''Calcula o valor da diária com base na idade.'''

        if self.idade <= 3:
            valor = 50.00
        elif 4 <= self.idade <= 10:
            valor = 60.00
        else:
            valor = 75.00
        return valor


    def verificar_vacinacao(self):
        '''Exibe o status de vacinação.'''
        if self.vacinado:
            print(f"Status de {self.nome}: Vacinação em dia.")
        else:
            print(f"ATENÇÃO: {self.nome} está com vacinação pendente.")



    def atualizar_peso(self, novo_peso):
        '''Atualiza o peso do pet.'''
        print(f"Atualizando peso de {self.nome}: {self.peso}kg -> {novo_peso}kg")
        self.peso = novo_peso



    def emitir_resumo(self):

        '''Exibe um resumo geral consolidado.'''

        diaria = self.calcular_diaria()
        status_vacinacao = "Protegido" if self.vacinado else "Pendente"
        status_hosp = "No Hotel" if self.hospedado else "Em Casa"

        

        print(f"\n>>> RESUMO DE HOSPEDAGEM <<<")
        print(f"Pet: {self.nome} ({self.especie}) | Dono: {self.nome_dono}")
        print(f"Saúde: {status_vacinacao} | Peso: {self.peso}kg")
        print(f"Status: {status_hosp} | Valor da Diária: R$ {diaria:.2f}")
        print("-" * 25)



# ==================================

# TESTES DA CLASSE (Atividade Final)

# ===================================



# 1. Criando os objetos (Instanciação)

pet1 = Pet("Belinha", "Cachorro", "vira-lata", 5, 30.0, "Carlos", True)
pet2 = Pet("Mingau", "Gato", "Siamês", 2, 4.5, "Julia")
pet3 = Pet("Thor", "Cachorro", "Poodle", 12, 8.0, "Marcos", True)



# --- Testando Pet 1 (Rex) ---

pet1.exibir_dados()
pet1.registrar_entrada()
pet1.registrar_entrada() # Teste de aviso: já hospedado
# --- Testando Pet 2 (Mingau) ---
pet2.verificar_vacinacao()
pet2.atualizar_peso(4.8)
pet2.emitir_resumo()
# --- Testando Pet 3 (Thor) ---
pet3.registrar_entrada()
pet3.emitir_resumo() # Verificando se a diária de idoso (R$ 75) aplica corretamente
pet3.registrar_saida()
pet3.registrar_saida() # Teste de aviso: não está hospedado