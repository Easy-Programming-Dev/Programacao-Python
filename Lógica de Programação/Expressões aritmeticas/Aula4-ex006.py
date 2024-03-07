'''6.	Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.'''







salario = float(input("Digite o salário do funcionário: R$ "))

aumento = salario+(salario*0.15)

print("O salário com aumento de 15% será de R$ {:.2f}".format(aumento))