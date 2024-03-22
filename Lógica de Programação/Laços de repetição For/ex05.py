'''5. Escreva um algoritmo para ler 10 números e ao final da leitura 
escrever a soma total dos 10 números lidos.
'''


soma=0
for i in range(1,10+1):
    num = int(input("Digite um numero: "))

    for i in range (num):
        i+=1
        soma+=i
        

print(f"A soma dos numeros digitados é: {soma}")