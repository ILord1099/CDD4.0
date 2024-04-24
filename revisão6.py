resposta = "S"
while resposta == "S" or resposta == "s":
    numero = int(input("Digite um numero: "))
    div = numero % 2
    if div == 0:
        print("Numero Par")
    else:
        print("Numero Impar")
    resposta = input("Deseja refazer ? S ou N: ")
