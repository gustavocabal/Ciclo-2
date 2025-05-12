def ex1 (): 
    print("Quanto é 1 + 1?")
    print("a) 2")
    print("b) 3")
    print("c) 4")
    print("d) 5")
    while True:
        try:
            resposta = str(input("Digite a letra da resposta correta: "))
            resposta = resposta.lower()  # Transforma a resposta em minúscula para evitar erros de comparação
            if resposta in ["a", "b", "c", "d"]:
                break  # Sai do loop se a resposta for válida
            else:
                print("Resposta inválida! Por favor, digite a letra da resposta correta.")
        except ValueError:
            print("Erro: Entrada inesperada. Por favor, tente novamente.")

    if resposta == "a":
        print("Correto! 1 + 1 é igual a 2.")
    elif resposta == "b":
        print("Incorreto! 1 + 1 não é igual a 3.")
    elif resposta == "c":
        print("Incorreto! 1 + 1 não é igual a 4.")
    elif resposta == "d":
        print("Incorreto! 1 + 1 não é igual a 5.")
    else:
        print("Resposta inválida! Por favor, digite a letra da resposta correta.")

    print("Obrigado por participar do teste!")

def ex2 ():
    print("Digite os tamanhos dos lados de um triângulo:")
    lados = []
    for i in range(3):
        lado = float(input(f"Lado {i+1}: "))
        lados.append(lado)

    for(i) in range(3):
        print(lados[i])
    
    lados.sort()

    if lados[0] == lados[1] and lados[1] == lados[2]:
        print("O triângulo é equilátero.")
    elif lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
        print("O triângulo é escaleno.")
    else:
        print("O triângulo é isósceles.")

def ex3():
    while True:
        try:
            n = int(input("Digite um número natural: "))
            if n < 0:
                print("Por favor, digite um número natural (não negativo).")
                continue
            break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

    for i in range(1, n + 1):
        print(i, end=" ")

