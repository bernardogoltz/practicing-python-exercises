# -*- coding: utf-8 -*-
"""
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

"""

def checkPalindrome(word2c):   
    word = word2c.replace(" ","").upper()
    reversed_word = word[::-1]
    return word == reversed_word
    
word = str(input("Type a text and check if it's a palyndrome: "))

if checkPalindrome(word):
    print("{} is a Palyndrom".format(word))
else:
    print("{} is Not a Palyndrom".format(word))
    
