# ====================================================
# SISTEMA DE APROVAÇÃO DE ALUNOS 
# ====================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisao: Variáveis, Tipos e Controle de Fluxo
# Autor      : RAFAEL LOPES PAZ OLIVEIRA PALHANO
# Data       : 24/02/2026
# Repositório: https://github.com/20251ctb0100049-a11y/2026-PS
# ====================================================
#
# DESCRIÇÃO:
# Este programa processa as notas de uma turma e determina
# a situação de cada aluno (Aprovado, Recuperação ou Reprovado).
# Conceitos utilizados: variáveis, tipos de dados, operadores,
# estruturas de seleção e estruturas de repetição.
# ====================================================

# ---- ENTRADA DE DADOS ----

print("=== Sistemas de Aprovação de Alunos ===")
print() # linha em branco para organizar a saída

nome = input("Digite o nome do aluno: ")    #str - texto
nota1 = float(input("digite a nota 1 (0 a 10): ")) # float - decimal
nota2 = float(input("Digite a nota 2 (0 a 10): ")) # float - decimal

# ==== PROCESSAMENTO ====


media = (nota1 + nota2) / 2 # operador aritmético: soma e divisão

print()
print(f"Aluno  : {nome}")
print(f"Nota 1  : {nota1:.1f}")
print(f"Nota 2  : {nota2:.1f}")
print(f"Média  : {media:.2f}")  # :.2f = exibe com 2 casas decimais

# ==== DECISÃO ====


if media >= 6.0:                # condição principal
   situacao = "Aprovado"
elif media>= 4.0:                # condição alternativa (só verificada se a anterior for falsa)
   situacao = "Recuperação"
else:                            # caso nenhuma condição anterior seja verdadeira
   situacao = "Reprovado"

print(f"Situação: {situacao}")
print("-" * 40)  # linha separadora: repete o caractere "-" 40 vezes

# ==== DADOS DA TURMA ====
# uma lista de dicionários: cada dicionário representa um aluno


turma = [
("nome": "Ana",   "nota1": 8.0, "nota2": 7.5),
("nome": "Bruno", "nota1": 4.5,"nota2": 5.0),
("nome": "Carla", "nota1":2.0, "nota2": 3.5),
]

print("=== Resultado da Turma ===")
print()

# O 'for' percorre cada aluno da lista automaticamente
for aluno in turma:
   nome = aluno["nome"]
   nota1 = aluno["nota1"]
   nota2 = aluno["nota2"]
   media = (nota1 + nota2) / 2


   if media >= 6.0:
      situacao = "Aprovado"
   elif media >= 4.0:
      situacao = "Recuperação"
   else:
      situacao = "Reprovado"


print(f"Aluno   : {nome}")
print(f"Média   : {nome}")
print(f"Situação: {situacao}")
print(f"-" * 30)

continuar = "a"
while continuar == "s":
   print("\nDeseja processar outro aluno? (s/n): ", end="")
   continuar = input () .lower()
   if continuar == "s":
      # complete aqui: peça, notal e nota2, calcule e exiba a situação pass