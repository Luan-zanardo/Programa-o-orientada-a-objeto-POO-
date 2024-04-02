class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def postar_conteudo(self, conteudo):
        print(f"{self.nome} postou: {conteudo}")

    def interagir(self, outro_usuario, comentario):
        print(f"{self.nome} comentou no perfil de {outro_usuario.nome}: {comentario}")

class Influenciador(Usuario):
    def __init__(self, nome, email, seguidores):
        super().__init__(nome, email)
        self.seguidores = seguidores

    def ganhar_seguidor(self):
        self.seguidores += 1
        print(f"{self.nome} ganhou um novo seguidor! Total: {self.seguidores}")

class Empresa(Usuario):
    def __init__(self, nome, email, segmento):
        super().__init__(nome, email)
        self.segmento = segmento

    def promover(self, produto):
        print(f"{self.nome} está promovendo seu produto {produto}!")