'''Ler 10 valores e escrever qual desses valores é o menor e qual o maior.
'''

valores = []
num = 0
cont = 0
while cont <10:
    num = float(input("Digite um numero: "))
    valores.append(num)
    cont+=1

print(f'''O MAIOR valor da lista é {max(valores)}\n
O MENOR valor da lista é {min(valores)}''')