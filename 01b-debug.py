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
