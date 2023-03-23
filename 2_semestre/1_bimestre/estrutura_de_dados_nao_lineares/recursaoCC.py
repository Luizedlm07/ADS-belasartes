
def factreccc(num):
    
    
    if num == 1 or num == 0:
        return 1
    else:
        return(num * factreccc(num-1))
    

print(factreccc(5))