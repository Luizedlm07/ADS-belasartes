class Caixa:
    def __init__(self):
        self.valor_inicial = 100.00
        self.valor_atual = self.valor_inicial
        self.entradas = 0
        self.saidas = 0

    def comprar(self, valor):
        self.saidas += valor
        self.valor_atual -= valor
        print(f'\nCompra no valor de R${valor}')

    def vender(self, valor):
        self.entradas += valor
        self.valor_atual += valor
        print(f'\nVenda no valor R${valor}')

    def verificar_estado_atual(self):
        print(
            f"\nValor atual = R${self.valor_atual:.2f}\n"
            f"Entradas = R${self.entradas:.2f}\n"
            f"Saídas = R${self.saidas:.2f}"
        )

caixa1 = Caixa()
caixa1.verificar_estado_atual()
caixa1.comprar(35.50)
caixa1.vender(74.99)
caixa1.verificar_estado_atual()
