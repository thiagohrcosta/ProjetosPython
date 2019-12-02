"""
Código básico para teste de login digitado pelo usuário.
"""

usuario_id_1 = "Jose"
senha_1 = "123456"

usuario_id_2 = "Maria"
senha_2 = "654321"

usuario_id = input("Digite o nome de usuário(ID):")
senha = input("Digite sua senha de usuário:")

if usuario_id == usuario_id_1 and senha == senha_1:
    print(f'Usuário(a) logado(a) no sistema. Bem vindo {usuario_id_1}')
elif usuario_id == usuario_id_2 and senha == senha_2:
    print(f'Usuário(a) logado(a) no sistema. Bem vinda {usuario_id_2}')
else:
    print("Usuário e/ou senha digitado(s) errado(s).")

    tentarNovamente = input("Gostaria de tentar novamente (Sim / Não) ?")
    if tentarNovamente == 'Não':
        print("Programa finalizado pelo usuário.")
    else:
        usuario_id2 = input("Digite o nome de usuário(ID):")
        senha2 = input("Digite sua senha de usuário:")

        if usuario_id2 == usuario_id_1 and senha2 == senha_1:
            print(f'Usuário(a) logado(a) no sistema. Bem vindo {usuario_id_1}')
        elif usuario_id2 == usuario_id_2 and senha2 == senha_2:
            print(f'Usuário(a) logado(a) no sistema. Bem vinda {usuario_id_2}')
        else:
            print("Usuário e/ou senha incorretos. Sistema bloqueado.")
