from GestaoBiblioteca import Livro, Revista, CD

livro = Livro("Dom Quixote", "Miguel de Cervantes", 1605, "Romance")
revista = Revista("National Geographic", "National Geographic Society", 2022, "Janeiro")
cd = CD("Thriller", "Michael Jackson", 1982, "Pop")

livro.emprestar()
revista.emprestar()
cd.emprestar()

livro.devolver()
revista.devolver()
cd.devolver()