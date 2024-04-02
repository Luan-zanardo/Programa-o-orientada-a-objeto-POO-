class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.saude = 100
        self.nivel = 1
        
    def receber_dano(self, dano):
        self.saude -= dano
        if self.saude <= 0:
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Saúde restante: {self.saude}")
            
    def __str__(self):
        return f"{self.nome}, Nível {self.nivel}, Classe: {self.classe}, Saúde: {self.saude}"

class Guerreiro(Personagem):
    def __init__(self, nome, forca, defesa):
        super().__init__(nome, "Guerreiro")
        self.forca = forca
        self.defesa = defesa
        
    def atacar(self, alvo, dano):
        alvo.receber_dano(dano)

class Mago(Personagem):
    def __init__(self, nome, inteligencia, magia):
        super().__init__(nome, "Mago")
        self.inteligencia = inteligencia
        self.magia = magia
        
    def atacar(self, alvo, dano):
        alvo.receber_dano(dano)

class Arqueiro(Personagem):
    def __init__(self, nome, destreza, precisao):
        super().__init__(nome, "Arqueiro")
        self.destreza = destreza
        self.precisao = precisao
        
    def atacar(self, alvo, dano):
        alvo.receber_dano(dano)

