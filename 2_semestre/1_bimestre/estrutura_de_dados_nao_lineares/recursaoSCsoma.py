
def recursaoSomaSC(num1, num2, soma):
    
    
    if num1 == num2:
        print(soma + num2)
    else:
        recursaoSomaSC(num1 + 1, num2, soma + num1)

recursaoSomaSC(2,5,0)
