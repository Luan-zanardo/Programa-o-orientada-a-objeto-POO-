from Registro import Calcular

nome = input("Digite nome: ")
salario = float(input("Digite salário: "))

while True:
    op = int(input("Funcionario:\n"
            "1 - Gerente\n"
            "2 - Programador\n"
            "3 - Analista\n"))

    if(op == 1):
        gerente = Calcular(nome, salario, "gerente")
        bonus = int(input("Digite porcentagem: "))
        gerente.GanharBonus(bonus)
        print(gerente.__dict__)
        break
    elif(op == 2):
        programador = Calcular(nome, salario, "programador")
        bonus = int(input("Digite porcentagem: "))
        programador.GanharBonus(bonus)
        print(programador.__dict__)
        break
    elif(op == 3):
        analista = Calcular(nome, salario, "analista")
        bonus = int(input("Digite porcentagem: "))
        analista.GanharBonus(bonus)
        print(analista.__dict__)
        break
    else:
        print("Digite um numero válido!")