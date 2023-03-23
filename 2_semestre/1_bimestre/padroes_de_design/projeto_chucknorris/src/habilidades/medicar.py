from .interfaces import Ihabilidade

class Medicar(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("medicar soldado")

    def nivel_atributo(self):
        print(f"Nivel de Medicar: {self.nivel}")