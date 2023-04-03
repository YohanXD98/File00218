print("Aperte a tecla enter para continuar...")
input()
username = input("Usuário: ")
senha01 = "senha 123"
senha02 = input("Senha: ")

while senha02 != senha01:
    print("Senha incorreta. Tente novamente.")
    senha02 = input("Senha: ")
print("Login Feito com sucesso !")