from typing import Type
from .habilidades import Ihabilidade

class Soldado:

    def __init__(self, habilidade: type[Ihabilidade]):
        self.habilidade = habilidade
    
    def acao(self):
        self.habilidade.comportamento()

    def atributos(self):
        self.habilidade.nivel_atributo()