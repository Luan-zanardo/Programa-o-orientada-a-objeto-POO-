class Ingresso:
    def __init__(self, tipo, preco):
        self.tipo = tipo
        self.preco = preco

    def calcular_preco(self, quantidade):
        return self.preco * quantidade

class IngressoNormal(Ingresso):
    def __init__(self):
        super().__init__("Normal", 10.00)

class IngressoVIP(Ingresso):
    def __init__(self):
        super().__init__("VIP", 20.00)

class Ingresso3D(Ingresso):
    def __init__(self):
        super().__init__("3D", 15.00)

class Sala:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ocupadas = 0

    def verificar_disponibilidade(self):
        return self.capacidade - self.ocupadas

    def reservar(self, quantidade):
        if self.verificar_disponibilidade() >= quantidade:
            self.ocupadas += quantidade
            print(f"Reserva realizada para {quantidade} ingressos.")
            return True
        else:
            print("Não há ingressos disponíveis suficientes.")
            return False