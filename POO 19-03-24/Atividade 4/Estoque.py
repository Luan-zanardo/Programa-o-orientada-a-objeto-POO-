class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco
        
    @property
    def preco(self):
        self._preco -= self._preco * (self.desconto / 100)
        return self._preco

class Eletronico(Produto):
    def __init__(self, nome, preco, garantia_meses, desconto):
        super().__init__(nome, preco)
        self.garantia_meses = garantia_meses
        self.desconto = desconto

class Vestuario(Produto):
    def __init__(self, nome, preco, tamanho, desconto):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        self.desconto = desconto

class Alimento(Produto):
    def __init__(self, nome, preco, validade, desconto):
        super().__init__(nome, preco)
        self.validade = validade
        self.desconto = desconto

class Estoque:
    def __init__(self):
        self.produtos = []
        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        
    def remover_produto(self, produto):
        self.produtos.remove(produto)
        
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome)