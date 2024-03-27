'''5. Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
números lidos. O número que encerrará a leitura será zero.'''





par = 0
impar = 0
media_par = 0
media_geral = 0
soma = 0
cont = 0
cont_par=0

while True:   
    
    num = int(input("Digite um número positivo: "))
    
    if num != 0:

        
        soma += num        

        if num % 2 != 0:
            impar+=num       
            cont+=1
        else:
            par += num
            cont_par+=1
            cont+=1
    else:
        break

media_par= par/cont_par

media_geral = soma/cont

print(f"A média dos pares é {media_par:.2f}")

print(f"A média geral é {media_geral:.2f}")