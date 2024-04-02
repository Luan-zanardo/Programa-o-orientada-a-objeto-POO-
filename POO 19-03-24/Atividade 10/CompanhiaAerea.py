class Voo:
    def __init__(self, origem, destino, preco_base, capacidade):
        self.origem = origem
        self.destino = destino
        self.preco_base = preco_base
        self.capacidade = capacidade
        self.reservas = 0

    def calcular_preco_passagem(self):
        return self.preco_base

    def verificar_disponibilidade(self):
        return self.capacidade - self.reservas > 0

    def fazer_reserva(self):
        if self.verificar_disponibilidade():
            self.reservas += 1
            print("Reserva efetuada com sucesso!")
        else:
            print("Não há disponibilidade para este voo.")

class VooEconomico(Voo):
    def __init__(self, origem, destino, preco_base, capacidade):
        super().__init__(origem, destino, preco_base, capacidade)

    def calcular_preco_passagem(self):
        return super().calcular_preco_passagem() * 0.8

class VooExecutivo(Voo):
    def __init__(self, origem, destino, preco_base, capacidade):
        super().__init__(origem, destino, preco_base, capacidade)

    def calcular_preco_passagem(self):
        return super().calcular_preco_passagem() * 1.5

class VooPrimeiraClasse(Voo):
    def __init__(self, origem, destino, preco_base, capacidade):
        super().__init__(origem, destino, preco_base, capacidade)

    def calcular_preco_passagem(self):
        return super().calcular_preco_passagem() * 2.0