'''9.	Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule sua área, e a quantidade de tinta necessária para pintá-la. 
Sabendo que cada litro de tinta, pinta uma área de 6m².'''







largura = float(input("Qual a largura da parede?: "))
altura = float(input("Qual a altura da parede?: "))

area = largura*altura

tinta = area/6

print("A área da parede é de {:.2f}m². Para pintar essa área será necessário {:.2f} litros de tinta".format(area,tinta))

