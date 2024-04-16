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

carro1 = Carros("Toyota", "Corolla", "Preto", 2002)
carro2 = Carros("Honda", "Civic", "Prata", 2023)

carro1.exibir_informacoes()
carro2.exibir_informacoes()

input()