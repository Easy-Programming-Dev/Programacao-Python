import math

'''Crie um programa que leia um número real (decimal) qualquer, 
e mostre na tela a sua porção inteira.'''



num = float(input("Digite um numero: "))

print (f"O número digitado foi {num} e sua porção inteira é {math.trunc(num)}")