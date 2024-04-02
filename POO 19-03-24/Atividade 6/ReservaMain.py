from Reserva import QuartoSimples, QuartoDuplo, Suite

quarto_simples = QuartoSimples(101, 50, 10, "Com reserva")
quarto_duplo = QuartoDuplo(201, 80, 10, "Com reserva")
suite = Suite(301, 150, 10, "Com reserva", 30)

print("Preço do quarto simples por 3 noites:", quarto_simples.calcular_preco_estadia(3))
print("Disponibilidade do quarto duplo:", quarto_duplo.verificar_disponibilidade())
print("Preço da suíte por 2 noites com extras:", suite.calcular_preco_estadia(2))