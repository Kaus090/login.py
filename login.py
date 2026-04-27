login_usuarios = {
    "admin": 1234,
    "kaua": 5984
}

tentativas = 0
limite = 3

while tentativas < limite:
    user = input("Digite o usuário: ")
    password = int(input("Digite a senha: "))

    if user in login_usuarios and password == login_usuarios[user]:
        print("Acesso liberado!")
        break
    else:
        tentativas += 1
        restantes = limite - tentativas
        if restantes > 0:
            print("Dados incorretos. Você ainda tem {restantes} tentativas.")
        else:
            print("Acesso bloqueado! Limite de tentativas excedido.")


