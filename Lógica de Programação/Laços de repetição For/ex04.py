'''4. Faça um programa em Python que leia um valor inteiro e mostre a 
tabuada de 1 a 10 do valor lido.'''


num = int(input("digite um numero: "))

tabuada = 0


for i in range (1,10+1):

    tabuada = i * num
    print(f"{i} x {num} = {tabuada}")
