# -*- coding: utf-8 -*-
"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""

notas = []

n = 2

for i in range(n):
    
    print("aluno{}".format(i+1))
    
    nota_aluno = 0
    
    for j in range(4):
        
        nota = float(input("Nota{}: ".format(j)))
        nota_aluno = nota_aluno + nota
        media_aluno = nota_aluno/4
        
    notas.append(media_aluno)
    
for i in range(len(notas)):
    print("notas do aluno {} = {}".format(i+1,notas[i]))
        
        
        