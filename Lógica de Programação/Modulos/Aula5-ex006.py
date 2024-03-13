from math import factorial


'''​

6. Faça um programa que leia um número qualquer e mostre o seu fatorial.
 Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''




 

n1 = int(input('Digite um numero : '))
fat = factorial(n1)

print('O fatorial de {} é {} '.format(n1,fat))