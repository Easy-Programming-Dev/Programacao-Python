'''5.	Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.'''





preco = float(input("Digite o preço do produto: "))

novo_preco = preco-(preco*0.05)

print("Aplicando o desconto de 5%, o valor do produto será de R$ {:.2f} ".format(novo_preco))