# Esse programa é um teste

import math

def area_ret(ladoA,ladoB):

    area = ladoA * ladoB


    return area

print(area_ret(10,20))

def area_circ(diametro):

    area = math.pi * (diametro ** 2) /4



    return area

def area_triangulo(base,altura):

    area = base * altura / 2


    return area

def perim_triangulo(lado1,lado2, lado3):

    prim = lado1 + lado2 + lado3


    return perim