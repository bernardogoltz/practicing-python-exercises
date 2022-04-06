# -*- coding: utf-8 -*-
"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

"""

lado = float(input("Lado (m) : "))


def area_quadrado(lado):
    return pow(lado, 2)

print("Lado (m): {} - Área do quadrado: {}m²".format(lado, area_quadrado(lado)))