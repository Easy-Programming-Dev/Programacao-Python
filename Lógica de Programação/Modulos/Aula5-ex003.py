import random


'''Um professor quer sortear um de seus 4 alunos para apagar o quadro. 
Faça um programa que leia o nome dos alunos, e escolha um deles aleatoriamente.'''





aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

turma = [aluno1,aluno2,aluno3,aluno4]

sorteado = random.choice(turma)

print("O aluno sorteado foi : ",sorteado)