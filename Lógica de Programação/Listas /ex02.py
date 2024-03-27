'''Ler 10 valores aleatórios e imprimi-los em ordem crescente.
'''


valores = []
num = 0
cont = 0
while cont <10:
    num = float(input("Digite um numero: "))
    valores.append(num)
    cont+=1

valores.sort()

print(valores)