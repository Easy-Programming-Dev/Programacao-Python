'''6. Desenvolva um script que leia 2 números e pergunte ao usuário qual operação ele deseja realizar. 
O programa deve mostrar o resultado,
informando se ele é par ou ímpar e positivo ou negativo.'''


num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

print("Operações: \n 1 - Adição \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação")

operacao = int(input("Digite um numero referente à operação desejada: "))

if operacao == 1:       # ADIÇÃO
    resultado = num1+num2
    if resultado % 2 == 0 and resultado > 0:
        print(f"O resultado {resultado:.2f} é um numero par e positivo.")

    elif resultado % 2 == 0 and resultado < 0:
        print(f"O resultado {resultado:.2f} é um numero par e negativo.")
    
    elif resultado % 2 != 0 and resultado > 0:
        print(f"O resultado {resultado:.2f} é um numero ímpar e positivo")

    elif resultado % 2 != 0 and resultado < 0:
        print(f"O resultado {resultado:.2f} é um numero ímpar e negativo")

    else:
        print(f"O resultado {resultado:.2f} é um numero par e nulo")

elif operacao == 2:            #SUBTRAÇÃO
        if num1 < 0 or num2 < 0:
            resultado = num1+num2
            if resultado % 2 == 0 and resultado > 0:
                print(f"O resultado {resultado:.2f} é um numero par e positivo.")

            elif resultado % 2 == 0 and resultado < 0:
                print(f"O resultado {resultado:.2f} é um numero par e negativo.")
            
            elif resultado % 2 != 0 and resultado > 0:
                print(f"O resultado {resultado:.2f} é um numero ímpar e positivo")

            elif resultado % 2 != 0 and resultado < 0:
                print(f"O resultado {resultado:.2f} é um numero ímpar e negativo")

            else:
                print(f"O resultado {resultado:.2f} é um numero par e nulo")

        else:
            resultado = num1-num2
            if resultado % 2 == 0 and resultado > 0:
                print(f"O resultado {resultado:.2f} é um numero par e positivo.")

            elif resultado % 2 == 0 and resultado < 0:
                print(f"O resultado {resultado:.2f} é um numero par e negativo.")
            
            elif resultado % 2 != 0 and resultado > 0:
                print(f"O resultado {resultado:.2f} é um numero ímpar e positivo")

            elif resultado % 2 != 0 and resultado < 0:
                print(f"O resultado {resultado:.2f} é um numero ímpar e negativo")

            else:
                print(f"O resultado {resultado:.2f} é um numero par e nulo")

elif operacao == 3:
    resultado = num1/num2
    if resultado % 2 == 0 and resultado > 0:
        print(f"O resultado {resultado:.2f} é um numero par e positivo.")

    elif resultado % 2 == 0 and resultado < 0:
        print(f"O resultado {resultado:.2f} é um numero par e negativo.")
    
    elif resultado % 2 != 0 and resultado > 0:
        print(f"O resultado {resultado:.2f} é um numero ímpar e positivo")

    elif resultado % 2 != 0 and resultado < 0:
        print(f"O resultado {resultado:.2f} é um numero ímpar e negativo")

    else:
        print(f"O resultado {resultado:.2f} é um numero par e nulo")

elif operacao == 4:
    resultado = num1*num2
    if resultado % 2 == 0 and resultado > 0:
        print(f"O resultado {resultado:.2f} é um numero par e positivo.")

    elif resultado % 2 == 0 and resultado < 0:
        print(f"O resultado {resultado:.2f} é um numero par e negativo.")
    
    elif resultado % 2 != 0 and resultado > 0:
        print(f"O resultado {resultado:.2f} é um numero ímpar e positivo")

    elif resultado % 2 != 0 and resultado < 0:
        print(f"O resultado {resultado:.2f} é um numero ímpar e negativo")

    else:
        print(f"O resultado {resultado:.2f} é um numero par e nulo")
else:
    print("Número de operação inválido! Tente novamente.")    


