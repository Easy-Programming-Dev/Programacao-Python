'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triangulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''





cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hi = (cateto_oposto**2+cateto_adjacente**2)**(1/2)



print(f"A hipotenusa do triangulo retangulo é {hi:.2f} cm")

