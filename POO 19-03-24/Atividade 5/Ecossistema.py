class Ecossistema:
    def __init__(self, nome, energia):
        self.nome = nome
        self._energia = energia

class Animais(Ecossistema):
    def __init__(self, nome, energia):
        super().__init__(nome, energia)

    def mover(self):
        print(f"{self.nome} está se movendo.")

    def alimentar(self):
        print(f"{self.nome} está se alimentando.")

    def reproduzir(self, quantidade):
        print(f"{self.nome} reproduziu {quantidade} seres.")

class Plantas(Ecossistema):
    def __init__(self, nome, energia):
        super().__init__(nome, energia)

    def crescer(self, cm):
        print(f"{self.nome} está crescendo {cm} centímetros.")

    def reproduzir(self, quantidade):
        print(f"{self.nome} reproduziu {quantidade} seres.")

class Parasitas(Ecossistema):
    def __init__(self, nome, energia):
        super().__init__(nome, energia)

    def infectar(self):
        print(f"{self.nome} está infectando outro ser vivo.")

    def reproduzir(self, quantidade):
        print(f"{self.nome} reproduziu {quantidade} seres.")
