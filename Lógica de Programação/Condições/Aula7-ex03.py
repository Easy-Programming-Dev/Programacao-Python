'''3. Faça um script que leia as horas e os minutos e imprima a mensagem “Bom dia”, “Boa tarde” ou “Boa noite”. 
'''


horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))



#hora_texto = [str(horas),str(minutos)]


#horario = ':'.join(hora_texto)

if horas >= 6 and horas <= 11:
    print("Turno Matutino")

elif horas >=12 and horas <= 18:
    print("Turno Vespertino")

elif horas > 18 and horas < 6:
    print("Turno Noturno")


'''if horario >= '0:00' and horario <= '11:59':    
    print("Bom dia!")

elif horario >='12:00' and horario <= '18:59':
    print("Boa tarde")

elif horario >='19:00' and horario <= '23:59':
    print("Boa noite")

else:
    print("Horario inválido!")'''