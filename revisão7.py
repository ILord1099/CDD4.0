menu = 0
while menu != 3:
    menu = int(input("Digite [1] para Calcular o triangulo ou [2] para área do Quadrado, [3] para sair : "))
    if menu == 1:
        base = float(input("Digite o Valor da base: "))
        altura = float(input("Digite o Valor da altura: "))
        res = (base * altura) / 2
        print(res)
        menu = 0
    elif menu == 2:
        lado = float(input("Digite o valor do lado do quadrado: "))
        calc = lado ** 2
        print(calc)
        menu = 0
    elif menu == 3:
        print("você saiu do Menu")
    else:
        print("Você digitou um valor errado no menu ")
