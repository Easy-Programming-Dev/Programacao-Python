'''5. Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS e quantos são POSITIVOS. Utilize listas para resolução.'''
i = 0
positivo = []
negativo = []

#for i in range(1,10+1):
while i <= 10:
    num = float(input("Digite um numero: "))
    i += 1

    if num > 0:
        positivo.append(num)

    else: 
        negativo.append(num)

print(f"Os numeros positivos são: {len(positivo)}")

print(f"Os numeros negativos são: {len(negativo)}")