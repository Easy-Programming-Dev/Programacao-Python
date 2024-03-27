''' Faça um programa em Python utilizando a estrutura de repetição WHILE, 
que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido. Exemplo: “1 x 2 = 2”.'''






n = int(input("digite um numero de 1 a 10: "))
cont = 0

while cont <= 10:
    tab = n * cont
    print(n, "X", cont, "=", tab)
    cont += 1

    