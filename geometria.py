import math

def area_circulo(raio):
    if raio < 0:
        raise ValueError("O raio não pode ser negativo.")
    return math.pi * raio ** 2

def area_retangulo(largura, altura):
    if largura < 0 or altura < 0:
        raise ValueError("A largura e a altura não podem ser negativas.")
    return largura * altura
