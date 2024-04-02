class Conta():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
        
    @salario.setter
    def salario(self):
        raise ValueError("Nao pode alterar o valor do salario!")
    
    def calcularSalario(self, bonus):
        self.__salario += (bonus / 100) * self.__salario

class Calcular(Conta):
    def __init__(self, nome, salario, cargo):
        super().__init__(nome, salario, cargo)

    def GanharBonus(self, porcent):
        self.calcularSalario(porcent)