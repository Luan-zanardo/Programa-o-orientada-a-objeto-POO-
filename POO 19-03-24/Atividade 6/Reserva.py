class Quarto:
    def __init__(self, numero, capacidade, preco, disponibilidade):
        self.numero = numero
        self.capacidade = capacidade
        self.preco = preco
        self.disponibilidade = disponibilidade

    def verificar_disponibilidade(self):
        return self.disponibilidade
    
    def calcular_preco_estadia(self, num_noites):
        return self.preco * num_noites

class QuartoSimples(Quarto):
    def __init__(self, numero, preco, capacidade, disponibilidade):
        super().__init__(numero, preco, capacidade, disponibilidade)

class QuartoDuplo(Quarto):
    def __init__(self, numero, preco, capacidade, disponibilidade):
        super().__init__(numero, preco, capacidade, disponibilidade)

class Suite(Quarto):
    def __init__(self, numero, preco, capacidade, disponibilidade, extras):
        super().__init__(numero, preco, capacidade, disponibilidade)
        self.extras = extras

    def calcular_preco_estadia(self, num_noites):
        return super().calcular_preco_estadia(num_noites) + self.extras * num_noites