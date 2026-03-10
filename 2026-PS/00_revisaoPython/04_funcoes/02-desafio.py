# ==============================================================================
# NOME: Rafael Lopes
# DISCIPLINA: Programação de sistemas
# DATA: 10/03/2026
# ==============================================================================
# DESCRIÇÃO: Sistema modular para cálculo de médias e situações (IFPR).
# ==============================================================================

def calcular_media(n1, n2):
    """Calcula a média aritmética de 2 notas e a retorna."""
    return (n1+n2)/2

def verificar_situacao(mt):
    """Responde com a situação final do aluno de acordo com sua média."""
    if mt >= 6.0:
        return "Aprovado"
    elif 4.0 <= mt < 6.0:
        return "Recuperação"
    else:
        return "Reprovado"

nome = input("Digite o nome do aluno: ")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media_final = calcular_media(n1, n2)
result = verificar_situacao(media_final)

print("\n" + "="*30)
print(f"nome do estudante: {nome}")
print(f"media: {media_final:.1f}")
print(f"resultado: {result}")
print("="*30) 