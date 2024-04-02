class Tarefa:
    def __init__(self, nome, tipo, responsavel, prazo):
        self.nome = nome
        self.tipo = tipo
        self.responsavel = responsavel
        self.prazo = prazo
        self.concluida = False

    def atribuir_responsavel(self, responsavel):
        self.responsavel = responsavel

    def definir_prazo(self, prazo):
        self.prazo = prazo

    def marcar_como_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"Tarefa: {self.nome} | Tipo: {self.tipo} | Responsável: {self.responsavel} | Prazo: {self.prazo} | Status: {status}"

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(tarefa)