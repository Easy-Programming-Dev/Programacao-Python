'''Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem 
ser somados. Escreva o valor final da soma efetuada.'''

soma= 0
for i in range(1,10):
    i+=1
    num = int(input("Digite um número: "))
    if num < 40:
        soma+=num
    else:
        pass

print(f"Soma dos Numeros inferiores a quarenta: {soma}")