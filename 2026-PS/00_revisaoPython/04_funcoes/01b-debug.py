# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

def saudacao(nome, turno="manhã"):
    return f"Bom {turno}, {nome}!"

print(saudacao("Ana"))
print(saudacao("Bruno", "tarde"))

def dobrar(x):
    return x * 2


print("Dobro de 5:", dobrar(5))

total = 0
def incrementar():
    global total
    total = total + 1

incrementar()

print("Total:",total)

def contagem(n):
    print(n)
    if n > 0:
        contagem(n-1)

contagem(3)

