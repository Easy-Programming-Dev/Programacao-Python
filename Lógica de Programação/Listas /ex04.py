'''Faça um programa que leia determinada quantidade de pessoas e receba a idade de cada uma delas. 
Separe-as em 3 grupos: menores de 25 anos são jovens, maiores de 25 são adultos, e acima dos 60 anos são idosos. Mostre quantas pessoas pertencem a cada grupo.
'''


jovens = []
adultos = []
idosos = []
i= 0
quant = int (input("Digite a quantidade de pessoas que deseja receber a idade: "))

while i < quant:
    idade = int(input("Digite uma idade: "))
    i+=1
    if idade > 0 and idade < 25:
        jovens.append(idade)
    
    elif idade >= 25 and idade < 60:
        adultos.append(idade)

    elif idade > 60:
        idosos.append(idade)
    
    else:
        print("Idade inválida!")

print(f'''No grupo de jovens há {len(jovens)} pessoas. \n
      No grupo de adultos há {len(adultos)}pessoas. \n
      No grupo dos idosos há {len(idosos)}pessoas.''')