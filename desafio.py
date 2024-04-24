anos = int(input("Digite o ano que você nasceu: "))
meses = int(input("DIgite o mês que você nasceu: "))
dias = int(input("Digite o dia que vocÇe nasceu :  "))

anoAtual = int(input("Digite o ano atual: "))
mesAtual = int(input("Digite o mês atual: "))
diaAtual = int(input("Digite o dia atual: "))

mes2 = 12 - meses + mesAtual
dia2 = 30 - dias + diaAtual
resulMeses = (anoAtual - anos) * 12
anos_dias = (anoAtual - anos) * 365
meses_dias = meses * 30
idadeAtual = anoAtual - anos
total_dias = anos_dias + meses_dias + dias
if dia2> 30:
    dia2 = dia2 - 30
    mes2 = mes2 + 1
if mesAtual <= meses:
    idadeAtual = idadeAtual - 1
    print(f"Você tem {idadeAtual} anos, você viveu {dia2} dias, com um total de {mes2 } meses ")
else:
    print(f"Você tem {idadeAtual} anos, você viveu {dia2} dias, com um total de {mes2} meses ")

