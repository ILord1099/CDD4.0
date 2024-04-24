soma = 0
for x in range(2):
    n = float(input("Digite sua nota: "))
    soma = soma + n
media = soma / 2
if media >= 7:
    print(f"Você foi aprovado com media {media}")
elif media >= 4:
    print(f"Você está de recuperação com media: {media}")
else:
    print(f"Você foi reprovado com media {media}")
