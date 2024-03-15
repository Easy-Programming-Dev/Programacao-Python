'''3. Faça um script que leia as horas e os minutos e imprima a mensagem “Bom dia”, “Boa tarde” ou “Boa noite”. 
'''


horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))

if horas < 0 or horas > 24 or minutos < 0 or minutos > 59: 
    print("Horario inválido")
else:

    if horas > 0 and horas < 12:
        print("Bom dia")

    elif horas >=12 and horas < 17:
        print("Boa tarde")

    else:
        print("Boa noite")

hora_texto = [str(horas),str(minutos)]


horario = ':'.join(hora_texto)

print(horario)


