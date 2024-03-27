'''6. Faça um programa que receba vários números inteiros repetidamente. 
Se o número digitado não for primo, o programa deverá mostrar a mensagem "não é primo". 
Caso contrario o programa deve encerrar, 
mostrando no final do código qual o número primo digitado. 
'''




while True:
    numero = int(input("\nDigite um número: "))

    if numero % 2 == 0 and numero != 2:
        print("não primo")
    else:
        print(f"O número {numero} é primo")
        break


