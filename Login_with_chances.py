print ("Pressione qualquer tecla para continuar..")
input()
username = input("Nome: ")
senha_correta = "senha123"
numero_tentativas = 0
limite_tentativas = 3

while numero_tentativas < limite_tentativas:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        break
    else:
        print("Senha incorreta. Tente novamente.")
        numero_tentativas += 1

if numero_tentativas == limite_tentativas:
    print("Número máximo de tentativas alcançado. Acesso negado.")
else:
    print("Acesso permitido. Bem-vindo," ,username)