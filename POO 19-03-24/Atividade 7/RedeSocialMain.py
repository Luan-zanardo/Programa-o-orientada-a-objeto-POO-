from RedeSocial import Usuario, Influenciador, Empresa

usuario1 = Usuario("João", "joao@email.com")
usuario2 = Usuario("Maria", "maria@email.com")

usuario1.postar_conteudo("Olá pessoal, estou aqui!")
usuario2.interagir(usuario1, "Legal!")

influenciador1 = Influenciador("Pedro", "pedro@email.com", 1000)
influenciador1.postar_conteudo("Novo vídeo no meu canal!")
influenciador1.ganhar_seguidor()

empresa1 = Empresa("EmpresaXYZ", "contato@empresa.com", "Tecnologia")
empresa1.promover("Novo smartphone")