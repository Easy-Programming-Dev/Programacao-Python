'''1.	Escreva um programa que converta uma temperatura digitando em graus Celsius e converta em Fahrenheit.'''







c = float(input("Informe a temperatura em graus Celsius: "))

f = c*1.8+32

print("A temperatura de {:.1f}°C corresponde a {:.1f}°F.".format(c,f))