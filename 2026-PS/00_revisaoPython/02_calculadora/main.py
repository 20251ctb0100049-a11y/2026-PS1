
sair = False

while sair == False:
    print("--- MINHA CALCULADORA ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    
    escolha = input("O que você quer fazer? ")

    if escolha == "5":
        print("Saindo do programa...")
        sair = True
    elif escolha == "1" or escolha == "2" or escolha == "3" or escolha == "4":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if escolha == "1":
            resultado = n1 + n2
            print("O resultado da soma é:", resultado)
        
        elif escolha == "2":
            resultado = n1 - n2
            print("O resultado da subtração é:", resultado)
            
        elif escolha == "3":
            resultado = n1 * n2
            print("O resultado da multiplicação é:", resultado)
            
        elif escolha == "4":
            if n2 == 0:
                print("Erro! Não dá pra dividir por zero!")
            else:
                resultado = n1 / n2
                print("O resultado da divisão é:", resultado)
    else:
        print("Opção errada! Escolha de 1 a 5.")

    print("-" * 25) 