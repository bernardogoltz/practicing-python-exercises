# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:52:43 2022

Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.


@author: bernardogoltz
"""

nome = "bernardodz"
tamanho = len(nome)
n = 10

vogais = "aeiou"
nome_consoante = ""


if nome.isalpha() == True:
    
    nome = nome.lower()
    
    if tamanho == n:
        
        print(nome)
        for i in range(n):
            if nome[i] not in vogais:
                nome_consoante = nome_consoante + nome[i]                              
    else:
        print("insira um vetor com 10 caracteres")
    
else:
    print("insira um valor sem numeros")
    
print(nome_consoante)
    
# mais chatinho!



    