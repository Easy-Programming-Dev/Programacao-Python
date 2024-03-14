'''3. Faça um programa que leia 4 notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado: 
"Aprovado", se a média for maior ou igual a seis; ”Reprovado", se a média for menor que quatro; 
“Recuperação”, se estiver entre quatro e seis; "Aprovado com Distinção", se a média for igual ou maior que nove. 
'''




nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1+nota2+nota3+nota4)/4

if media >= 6 and media< 9: 
    print("Aluno aprovado!")

elif media <= 4:
    print("Aluno reprovado!")

elif media > 4 and media <6: 
    print("Aluno de recuperação")

else:
    print("Aluno aprovado com distinção")