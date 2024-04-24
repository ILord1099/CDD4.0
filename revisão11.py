totalEleitores = int(input("Digite o numero total de eleitores: "))
brancos = int(input("Digite numero de votos em branco: "))
nulos = int(input("Digite o numero de votos nulos: "))
validos = int(input("Digite o numero de votos validos: "))
votosBrancos = (brancos / totalEleitores) * 100
votosNulos = (nulos / totalEleitores) * 100
votosValidos = (validos / totalEleitores) * 100
total = (brancos + nulos + validos) - totalEleitores
while total > 0:
    print("Você digitou um numero invalido")
    totalEleitores = int(input("Digite o numero total de eleitores: "))
    brancos = int(input("Digite numero de votos em branco: "))
    nulos = int(input("Digite o numero de votos nulos: "))
    validos = int(input("Digite o numero de votos validos: "))
print(f"Quantidade de votos Validos : {votosValidos}%\n"
      f"Quantidade de votos Brancos:  {brancos}%\n"
      f"Quantidade de votos Nulos: {votosNulos}%\n")
