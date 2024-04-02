from CompanhiaAerea import VooEconomico, VooExecutivo, VooPrimeiraClasse

voo_economico = VooEconomico("São Paulo", "Rio de Janeiro", 200, 100)
voo_executivo = VooExecutivo("São Paulo", "Rio de Janeiro", 200, 50)
voo_primeira_classe = VooPrimeiraClasse("São Paulo", "Rio de Janeiro", 200, 20)

print("Preço da passagem (econômico):", voo_economico.calcular_preco_passagem())
print("Preço da passagem (executivo):", voo_executivo.calcular_preco_passagem())
print("Preço da passagem (primeira classe):", voo_primeira_classe.calcular_preco_passagem())

voo_economico.fazer_reserva()
voo_economico.fazer_reserva()
voo_economico.fazer_reserva()