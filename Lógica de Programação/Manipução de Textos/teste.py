############################# FATIAMENTO #############################
curso = 'logica de programação'

#print(curso[10])

#print(curso[10:17])

#print(curso[10:21:2])

#print(curso[:5])

#print(curso[7:])

#print(curso[10::3])



############################# ANALISE #############################

#print(len(curso)) #Vem de length = comprimento

#print(curso.count('o')) #Conta quantas vezes o elemento aparece dentro da string

#print(curso.count('o',10,21))

#print(curso.find('gra')) #Mostra a posição onde começa o elemento

#print('logica'in curso) #Mostra um booleano 


############################# TRANSFORMAÇÃO #############################
#print(curso.replace('logica','aula')) #Substitui o elemento indicado

#print(curso.upper())

#print(curso.lower())

#print(curso.capitalize()) # Apenas a primeira letra maiuscula

#print(curso.title())  # Todas as primeiras letras maiusculas utiliza os espaços para diferenciar as palavras

nome = '   Tereza    '

#print(nome.strip()) # Retira os espaços excedentes

curso = 'logica de programação'

#print(curso.split()) #Separa as palavras criando novas cadeias de caracteres

#print('-'.join(curso)) #Junta as cadeias e separa as palavras pelo sinal

'''texto = "Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker."
palavras = texto.split()
quantidade = len(palavras)
print(f"O texto contém {quantidade} palavras.")'''


'''media = 7

if media >= 8:
    print("Você é MAIOR de idade")

else:
    print("Você é MENOR de idade")'''


'''idade = int(input("Digite sua idade: "))

if idade < 18:
  print("Você é menor de idade.")

elif idade >= 18 and idade < 65:
  print("Você é adulto")

else:
  print("Você é idoso")'''

x = int(input("Digite um numero"))
y = int(input("Digite outro numero"))

if x > 10 and y > 10:
    print("Os numeros são maiores que 10")

elif x == 0 or y == 0:
    print("O valor de um do numeros é nulo")

elif not x > 5 or y > 5:
    print("Um dos numeros é menor que 5")

else:
    print("Os valores são iguais")



