'''5. Desenvolva um script que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''





print("Dias da semana: \n 1 - Domingo \n 2 - Segunda \n 3 - Terça \n 4 - Quarta \n 5 - Quinta \n 6 - Sexta \n 7 - Sabado")

num = int(input("Digite um numero que corresponda a um dia da semana: "))

if num==1:
    print("Domingo")
    
elif num==2:
    print("Segunda")

elif num==3:
    print("Terça")

elif num==4:
    print("Quarta")

elif num==5:
    print("Quinta")

elif num==6:
    print("Sexta")

elif num==7:
    print("Sabado")

else:
    print("Numero inválido!")

