# -*- coding: utf-8 -*-
"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)
"""

tamanho_arquivo = float(input("tamanho (MB): "))
velocidade = float(input("velocidade (MB/s): "))

def tempo(tamanho, velocidade):
    tempo_s = tamanho/velocidade
    tempo_min = (tempo_s/60)
    
    return round(tempo_min,1)

print("um arquivo de {}MB em uma internet com a velociade de download de dados de  {}MB/s leva {} minutos para baixar esse arquivo...".format(tamanho_arquivo, velocidade, tempo(tamanho_arquivo,velocidade)))