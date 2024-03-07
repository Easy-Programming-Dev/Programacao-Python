'''3.   Desenvolva um programa que leia as três notas de um aluno, calcule e mostre a sua média.
'''





n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float( input("Nota 3: "))

media = (n1+n2+n3)/3

print('A média do aluno é {:.2f}'.format(media))