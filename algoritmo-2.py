nota_1 = float(input("Digite a nota do Primeiro bimestre:"))
nota_2 = float(input("Digite a nota do Seguno bimestre:"))
nota_3 = float(input("Digite a nota do Terceiro bimestre:"))
nota_4 = float(input("Digite a nota do Quarto bimestre:"))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print("A media final é :",media)

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
