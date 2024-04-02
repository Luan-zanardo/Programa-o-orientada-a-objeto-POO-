class Unidade:
    def __init__(self, nome, tipo, pontos_vida, poder_ataque, velocidade_movimento):
        self.nome = nome
        self.tipo = tipo
        self.pontos_vida = pontos_vida
        self.poder_ataque = poder_ataque
        self.velocidade_movimento = velocidade_movimento

    def atacar(self, alvo):
        print(f"{self.nome} atacando {alvo.nome} com poder de ataque {self.poder_ataque}!")
        alvo.receber_dano(self.poder_ataque)

    def receber_dano(self, dano):
        self.pontos_vida -= dano
        if self.pontos_vida <= 0:
            print(f"{self.nome} foi destruído!")
        else:
            print(f"{self.nome} sofreu {dano} pontos de dano. Pontos de vida restantes: {self.pontos_vida}")

    def mover(self, destino):
        print(f"{self.nome} movendo-se para {destino} com velocidade {self.velocidade_movimento}.")

class Soldado(Unidade):
    def __init__(self):
        super().__init__("Soldado", "Terrestre", 100, 25, 10)

class Tanque(Unidade):
    def __init__(self):
        super().__init__("Tanque", "Terrestre", 200, 50, 5)

class Aviao(Unidade):
    def __init__(self):
        super().__init__("Avião", "Aéreo", 150, 40, 20)