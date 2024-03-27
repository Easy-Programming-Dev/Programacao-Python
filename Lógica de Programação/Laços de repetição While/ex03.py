'''3.  Criar um programa para calcular a média de um conjunto de 10
 valores inteiros fornecidos em uma unidade de entrada qualquer.'''






conjunto = 0
soma = 0

while conjunto < 10:
        
        num = int(input("Digite um numero: "))
        conjunto+=1
        soma+=num

media = soma/conjunto
print(f"A media do conjunto de valores é: {media}")