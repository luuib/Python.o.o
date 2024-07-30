def calcular_media_notas(notas):
    if len(notas) == 0:
        return 0
    return sum(notas / notas)

notas = []

num_notas = int(input(f"Digite o numero de notas:  "))

for i in range(num_notas):
    nota = float(input(f"Digite a nota {i + 1}"))
    nota.append(nota)

    media = calcular_media_notas(notas)

    print(f"A media de notas é: {media:.2f}")