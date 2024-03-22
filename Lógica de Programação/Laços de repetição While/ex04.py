'''4.  Desenvolva um algoritmo que receba 1 número, o valor deverá ser lidos até que o usuário digite um número fora do intervalo de 1 a 100. 
Apresentar a mensagem “Dentro do Intervalo”, se for digitado um número fora do intervalo, o programa deverá imprimir “Fora do Intervalo” e encerrar o programa'''



while True:
    
    num = int(input("Digite um numero: "))
    if num >=1 and num <=100:
        print(f"Numero {num} Dentro do Intervalo.")
        
    else:
        break
        
print(f"Numero {num} fora do intervalo.")
    
    