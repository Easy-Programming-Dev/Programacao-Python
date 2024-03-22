'''9. Ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2 valores lidos (incluindo 
os valores lidos na soma). Considere que o segundo valor lido será sempre maior que o primeiro valor 
lido. '''

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

soma = 0

for i in range(num1,num2):
    i+=1
    if i > 0:
        soma+=i
    else:
        pass
print(f"A soma dos inteiros existentes nesse intervalo é: {soma}")