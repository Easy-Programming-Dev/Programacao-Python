'''1. Desenvolva um script que leia 2 números, em seguida mostre qual o menor, o maior e se há igualdade entre eles. 
'''








num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if num1>num2:
    print("O primeiro número é maior que o segundo")

elif num2>num1:
    print("O segundo número é maior que o primeiro")

else:
    print(f"Os números são iguais.")
