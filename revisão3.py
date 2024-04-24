resposta = "s"
while resposta == "s" or resposta == "S":
    n = float(input("Digite um numero: "))
    if n >= 1:
        print(f"Numero: {n} é positivo")
    else:
        print(f"Numero: {n} é negativo")
    resposta = input("Deseja inserir outro numero ?")

