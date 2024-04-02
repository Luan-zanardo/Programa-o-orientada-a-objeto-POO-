class Investimento:
    def __init__(self, nome, valor_investido):
        self.nome = nome
        self.valor_investido = valor_investido

    def calcular_retorno(self):
        pass

    def calcular_risco(self):
        pass

class Acao(Investimento):
    def __init__(self, nome, valor_investido, preco_atual):
        super().__init__(nome, valor_investido)
        self.preco_atual = preco_atual

    def calcular_retorno(self):
        return (self.preco_atual - self.valor_investido) / self.valor_investido

    def calcular_risco(self):
        return self.preco_atual * 0.1

class Titulo(Investimento):
    def __init__(self, nome, valor_investido, taxa_juros):
        super().__init__(nome, valor_investido)
        self.taxa_juros = taxa_juros

    def calcular_retorno(self):
        return self.valor_investido * self.taxa_juros

    def calcular_risco(self):
        return self.valor_investido * 0.05

class FundoImobiliario(Investimento):
    def __init__(self, nome, valor_investido, renda_mensal):
        super().__init__(nome, valor_investido)
        self.renda_mensal = renda_mensal

    def calcular_retorno(self):
        return self.renda_mensal * 12

    def calcular_risco(self):
        return self.renda_mensal * 0.1