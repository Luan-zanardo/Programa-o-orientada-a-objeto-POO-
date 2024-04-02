from Estoque import Estoque, Eletronico, Vestuario, Alimento

estoque = Estoque()

estoque.adicionar_produto(Eletronico("Smartphone", 10000, 12, 50)) #nome, preco, garantia em meses ,desconto
estoque.adicionar_produto(Vestuario("Camisa", 1000, "M", 50)) #nome, preco, tamanho ,desconto
estoque.adicionar_produto(Alimento("Maçã", 100, "10/04/2024", 50)) #nome, preco, data de validade ,desconto

print("Produtos disponíveis:")
estoque.listar_produtos()

print("Preço do Smartphone:", estoque.produtos[0].preco)
print("Preço do Smartphone:", estoque.produtos[1].preco)
print("Preço do Smartphone:", estoque.produtos[2].preco)