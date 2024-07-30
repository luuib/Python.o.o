import math

def calcular_area_circulo(raio):
    return math.pi * raio ** 2

def calcuar_area_quadrado(lado):
    return lado ** 2

def calcular_area_triangulo(base , altura):
    return (base * altura) / 2

raio = float(input("Digite o raio o circulo: "))
lado = float(input("Digite o lado do quadrado: "))
area = float(input("Digite a area o quadrado: "))
base = float(input("Digite a base o triangulo: "))
altura = float(input("Digite a altura do triangulo: "))

area_circulo = calcular_area_circulo(raio)
area_quadrado = calcuar_area_quadrado(lado)
area_triangulo = calcular_area_triangulo(base, altura)

print(f"Area do circulo:{area_circulo:.2f}")
print(f"Area do quadrado:{area_quadrado:.2f}")
print(f"Area do triangulo:{area_triangulo:.2f}")