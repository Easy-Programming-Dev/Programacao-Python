'''4.	Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. '''





metro = float(input("Quantos metros você quer converter?: "))

cm = metro*100
mm = metro*1000

print("{} Metros equivale a {} Centímetros, e a {} Milímetros.".format(metro,cm,mm))