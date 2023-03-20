import time

class Impressora():
    def __init__(self):
        self.cartucho = 100

    def menu(self):
        menu = input('O que deseja fazer?\n\n[i]mprimir\n[v]erificar nível do cartucho\n[r]ecarregar cartucho\n[e]ncerrar\n\n')
        menu =  menu.lower()
        return menu
    
    def imprimir(self):
        if self.cartucho == 0:
            print('\nSeu cartucho está vazio, recarregue para continuar.\n')
        else:
            impressao = input('Digite o que deseja imprimir:\n\n')
            print('\nImprimindo...\n')
            time.sleep(2)
            print('Impressão: \n\n',impressao,'\n')
            print('Concluído!\n')
            self.cartucho -= 20
            if self.cartucho <= 20:
                print('\nSeu cartucho está chegando ao fim!\n')

    def nivel_cartucho(self):
        print('\nVerificando cartucho...\n')
        time.sleep(2)
        print(f'O nível do cartucho é: {self.cartucho}%\n')

    def recarregar_cartucho(self):
        if self.cartucho == 100:
            print('Seu cartucho já está cheio.\n')
        else:
            print('\nRecarregando...\n')
            time.sleep(2)
            self.cartucho = 100
            print('Recarregamento concluído!\n')


epson = Impressora()

while True:

    menu = epson.menu()

    if menu == 'i':
        epson.imprimir()
    elif menu == 'v':
        epson.nivel_cartucho()
    elif menu == 'r':
        epson.recarregar_cartucho()
    elif menu == 'e':
        print('Encerrando...\n')
        time.sleep(2)
        print('Até a próxima!')
        break
    else:
        print('\nOpção inválida!\n')
