hora1 = int(input("Digite a hora do inicio da partida: "))
hora2 = int(input("Digite a hora do fim da partida:  "))
sub = hora2 - hora1
if sub < 0:
    sub = sub * -1
print(sub)
