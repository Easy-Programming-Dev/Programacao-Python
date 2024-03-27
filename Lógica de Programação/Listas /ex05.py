'''5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor ímpar. O programa não pode aceitar o zero no vetor. Imprima os três vetores.
'''

par = []
impar = []
total = []

for i in range(10+1):
    num = int(input("Digite o numero: "))
    if num != 0:

        total.append(num)
        if num % 2 == 0: 
            par.append(num)
        else:
            impar.append(num)

    else:
        print("Digite numeros diferentes de zero!")

print(f'''Numeros pares: {par}\n
Numeros ímpares: {impar}\n
Todos os números digitados: {total}''')