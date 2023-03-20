from .interfaces import Ihabilidade

class Dirigir(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("dirigir tanque")

    def nivel_atributo(self):
        print(f'Nível de Dirigir: {self.nivel}')