from .interfaces import Ihabilidade

class Pilotar(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("pilotar aviao")

    def nivel_atributo(self):
        print(f'Nível de Pilotar: {self.nivel}')