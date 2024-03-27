'''2.  Implementar um programa para somar valores até o usuário digitar o 
valor 0.'''






soma=0
num = None
while num != 0:
    num = float(input("Digite um numero: "))
    soma+=num

print("A soma dos numeros digitados é: ",soma)