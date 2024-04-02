class Material:
    def __init__(self, titulo, autor, ano, disponibilidade=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponibilidade = disponibilidade

    def emprestar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            print(f"{self.titulo} foi emprestado com sucesso.")
        else:
            print(f"{self.titulo} não está disponível no momento.")

    def devolver(self):
        if not self.disponibilidade:
            self.disponibilidade = True
            print(f"{self.titulo} foi devolvido com sucesso.")
        else:
            print(f"{self.titulo} já está disponível.")

class Livro(Material):
    def __init__(self, titulo, autor, ano, genero, disponibilidade=True):
        super().__init__(titulo, autor, ano, disponibilidade)
        self.genero = genero

class Revista(Material):
    def __init__(self, titulo, autor, ano, edicao, disponibilidade=True):
        super().__init__(titulo, autor, ano, disponibilidade)
        self.edicao = edicao

class CD(Material):
    def __init__(self, titulo, autor, ano, genero, disponibilidade=True):
        super().__init__(titulo, autor, ano, disponibilidade)
        self.genero = genero