'''11.	Escreva um programa que leia a quantidade de Quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.'''








km = float(input("Qual a quantidade de quilometros percorridos?: "))

dias = int(input("Qual a quantidade de dias que o carro esteve alugado?: "))

valor = dias*60 + km*0.15

print("O Valor total refente ao aluguel do veiculo é de R$ {:.2f}".format(valor))

print()
