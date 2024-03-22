''' 3.  Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado. 
Por exemplo, se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10)'''

num = int(input("digite um numero: "))
soma = 0

for i in range(num):
    
    i += 1
    
    soma +=i
    sinal = " +"
    
    
    print(sinal[:i],i,end="")
    
print(" = ",soma)