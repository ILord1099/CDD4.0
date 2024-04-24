idade = int(input("Digite sua idade: "))
mes = int(input("Digite o numero do mes que você nasceu: "))
ano = 2024 - idade
if mes >= 4:
    ano = ano - 1
    print(ano)
else:
    print(ano)
