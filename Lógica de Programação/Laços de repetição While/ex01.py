'''1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

login = input("Login: ")
senha = input("Senha: ")

while login == senha:
    print("Sua senha deve ser diferente do login: ")
    senha = input("Senha: ")

print("Cadastro aprovado")