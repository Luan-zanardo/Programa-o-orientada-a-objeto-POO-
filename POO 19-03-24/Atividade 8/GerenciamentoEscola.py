class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Aluno(Usuario):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula

    def acessar_notas(self):
        print("Acessando notas do aluno...")

    def acessar_horarios(self):
        print("Acessando horários do aluno...")

class Professor(Usuario):
    def __init__(self, nome, email, disciplina):
        super().__init__(nome, email)
        self.disciplina = disciplina

    def acessar_notas(self):
        print("Acessando notas dos alunos...")

    def acessar_horarios(self):
        print("Acessando horários das aulas...")

class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

    def acessar_comunicados(self):
        print("Acessando comunicados da escola...")