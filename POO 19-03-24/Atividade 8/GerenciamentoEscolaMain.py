from GerenciamentoEscola import Aluno, Professor, Funcionario

aluno1 = Aluno("João", "joao@email.com", "12345")
professor1 = Professor("Maria", "maria@email.com", "Matemática")
funcionario1 = Funcionario("Carlos", "carlos@email.com", "Secretário")

aluno1.acessar_notas()
professor1.acessar_notas()
funcionario1.acessar_comunicados()