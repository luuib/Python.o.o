class Carros:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def exibir_informacoes(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Cor:", self.cor)
        print("Ano:", self.ano)

carros = []

while  True:
    marca = input("digite a marca do carro ou clickr 'sair' pra sair")

    if marca.lower() == "sair":
        print("adeus...")
        break

    modelo = input("digiteo o modelo")
    cor = input("digite a cor")
    ano = input("digite o ano")

    carro = Carros(marca, modelo, cor, ano)
    carros.append(carro)

print("\n informacoes do carro")
for i, carros in enumerate(carros, start=1):
    print(f"\n Carro{i}")
    carro.exibir_informacoes()
