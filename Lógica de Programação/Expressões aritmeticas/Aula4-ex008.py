'''8.	Crie um programa que leia quantos reais uma pessoa tem na carteira e mostra quantos dólares ela pode comprar. Considere a cotação do dolar de hoje.'''





real = float(input("Quantos reais você tem na carteira?: R$ "))

dolar = real/4.94

print("Com o valor de R$ {:.2f} você pode comprar US$ {:.2f}.".format(real,dolar))


