from Rpg import Guerreiro, Mago, Arqueiro  

nome = input("Digite nome: ")

while True:
    op = int(input("Classe:\n"
            "1 - Guerreiro\n"
            "2 - Mago\n"
            "3 - Arqueiro\n"))

    if(op == 1):
        forca = int(input("Digite força: "))
        defesa = int(input("Digite defesa: "))
        guerreiro = Guerreiro(nome, forca, defesa)
        print(guerreiro.__dict__)
        dano = int(input("Dano sofrido: "))
        guerreiro.atacar(guerreiro, dano)     
        break
    elif(op == 2):
        inteligencia = int(input("Digite inteligencia: "))
        magia = int(input("Digite magia: "))
        mago = Mago(nome, inteligencia, magia)
        print(mago.__dict__)
        dano = int(input("Dano sofrido: "))
        mago.atacar(mago, dano)  
        break
    elif(op == 3):
        destreza = int(input("Digite destreza: "))
        precisao = int(input("Digite precisao: "))
        arqueiro = Arqueiro(nome, destreza, precisao)
        print(arqueiro.__dict__)
        dano = int(input("Dano sofrido: "))
        arqueiro.atacar(arqueiro, dano)  
        break
    else:
        print("Digite um numero válido!")