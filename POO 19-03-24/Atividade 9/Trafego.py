class Veiculo:
    def __init__(self, modelo, velocidade_media):
        self.modelo = modelo
        self.velocidade_media = velocidade_media

    def calcular_tempo_viagem(self, distancia):
        tempo = distancia / self.velocidade_media
        return tempo

class Carro(Veiculo):
    def __init__(self, modelo, velocidade_media, passageiros):
        super().__init__(modelo, velocidade_media)
        self.passageiros = passageiros

    def calcular_tempo_viagem(self, distancia):
        tempo = super().calcular_tempo_viagem(distancia)
        tempo += 0.1 * self.passageiros
        return tempo

class Onibus(Veiculo):
    def __init__(self, modelo, velocidade_media, passageiros):
        super().__init__(modelo, velocidade_media)
        self.passageiros = passageiros

    def calcular_tempo_viagem(self, distancia):
        tempo = super().calcular_tempo_viagem(distancia)
        tempo += 0.2 * self.passageiros
        return tempo

class Bicicleta(Veiculo):
    def __init__(self, modelo, velocidade_media):
        super().__init__(modelo, velocidade_media)