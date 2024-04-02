from Trafego import Carro, Onibus, Bicicleta

carro = Carro("Fiat Uno", 60, 4)
onibus = Onibus("Mercedes-Benz", 40, 30)
bicicleta = Bicicleta("Caloi", 20)

distancia = 50

tempo_carro = carro.calcular_tempo_viagem(distancia)
tempo_onibus = onibus.calcular_tempo_viagem(distancia)
tempo_bicicleta = bicicleta.calcular_tempo_viagem(distancia)

print(f"Tempo de viagem de carro: {tempo_carro} horas")
print(f"Tempo de viagem de ônibus: {tempo_onibus} horas")
print(f"Tempo de viagem de bicicleta: {tempo_bicicleta} horas")