from Ecossistema import Animais, Plantas, Parasitas

animal = Animais("Leão", 100)
planta = Plantas("Carvalho", 50)
parasita = Parasitas("Vírus", 10)

animal.alimentar()
planta.crescer(10)
parasita.infectar()