from GerenciamentoProjeto import Projeto, Tarefa

projeto1 = Projeto("Projeto de Desenvolvimento de Software")

tarefa1 = Tarefa("Implementar Login", "Desenvolvimento de Software", "João", "2024-04-10")
tarefa2 = Tarefa("Criar Campanha de Marketing", "Marketing", "Maria", "2024-04-15")
tarefa3 = Tarefa("Realizar Pesquisa de Mercado", "Pesquisa", "Carlos", "2024-04-20")

projeto1.adicionar_tarefa(tarefa1)
projeto1.adicionar_tarefa(tarefa2)
projeto1.adicionar_tarefa(tarefa3)

print("Tarefas do Projeto:")
projeto1.listar_tarefas()

# Atribuir responsável e definir prazo para uma tarefa
tarefa1.atribuir_responsavel("Ana")
tarefa1.definir_prazo("2024-04-25")

# Marcar uma tarefa como concluída
tarefa2.marcar_como_concluida()

print("\nTarefas do Projeto atualizadas:")
projeto1.listar_tarefas()