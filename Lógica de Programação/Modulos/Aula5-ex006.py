import math

'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
 cosseno e tangente desse ângulo.'''




angulo = float(input("Digite o ângulo que deseja calcular: "))

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print(f"O ângulo de {angulo}° tem o \n SENO de {seno:.2f}\n COSSENO de {cosseno:.2f}\n TANGENTE de {tangente:.2f}")
