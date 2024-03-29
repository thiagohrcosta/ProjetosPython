"""
Código básico para elaboração de cálculos matemáticos. Foi adicionada opção para sair do programa.
"""
while True:
    print()
    num_1 = input("Digite um número qualquer:")
    num_2 = input("Digite outro número qualquer:")

    # Confere se o número digitado pelo usuário é válido.
    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar um número válido.")
        continue

    operador = input("Digite o tipo de operador (-, +, *, / ou %):")

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '%':
        print(num_1 % num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print(num_1 / num_2)

    # Opção para sair ou não do programa.
    sair = input("Deseja sair do programa (Sim / Não) ?")
    if sair == 'Sim':
        print("Programa finalizado pelo usuário.")
        break
    else:
        continue
