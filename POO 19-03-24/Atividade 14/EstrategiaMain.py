from Estrategia import Soldado, Tanque, Aviao

soldado1 = Soldado()
tanque1 = Tanque()
aviao1 = Aviao()

inimigo = Soldado()

soldado1.mover("Ponto A")
soldado1.atacar(inimigo)
tanque1.mover("Ponto B")
tanque1.atacar(inimigo)
aviao1.mover("Ponto C")
aviao1.atacar(inimigo)