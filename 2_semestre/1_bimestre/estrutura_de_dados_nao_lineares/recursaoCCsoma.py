'''
O usuario deve digitar dois numeros
por exemplo 2 e 5

o algoritmo deve somar 2 + 3 + 4 + 5
'''

def recursaoSomaCC(num1, num2):
    print(num1,num2)
    if num1 == num2:
        return (num1)
    else:
        return num1 + recursaoSomaCC(num1 + 1, num2)
    
print(recursaoSomaCC(1,5))