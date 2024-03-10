import random

'''O mesmo Professor quer sortear a ordem de apresentação dos trabalhos dos alunos. 
Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.'''






aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

turma = [aluno1,aluno2,aluno3,aluno4]

random.shuffle(turma)

print("A ordem de apresentação será: ",turma)