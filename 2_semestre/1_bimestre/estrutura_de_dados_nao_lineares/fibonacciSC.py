

def fibonacci(repeat, contador = 0, lista_fibonacci = [1,1]):
    lista_fibonacci.append(lista_fibonacci[-1] + lista_fibonacci[-2])
    contador += 1
    if contador == repeat:
        return lista_fibonacci
    
    return fibonacci(repeat, contador, lista_fibonacci)
    
print(fibonacci(5))