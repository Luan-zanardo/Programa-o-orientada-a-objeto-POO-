from MercadoFinanceiro import Acao, Titulo, FundoImobiliario

acao = Acao("Empresa X", 1000, 1200)
titulo = Titulo("Tesouro Direto", 5000, 0.05)
fundo_imobiliario = FundoImobiliario("FII ABC", 20000, 1500)

print("Retorno da ação:", acao.calcular_retorno())
print("Risco da ação:", acao.calcular_risco())

print("Retorno do título:", titulo.calcular_retorno())
print("Risco do título:", titulo.calcular_risco())

print("Retorno do fundo imobiliário:", fundo_imobiliario.calcular_retorno())
print("Risco do fundo imobiliário:", fundo_imobiliario.calcular_risco())