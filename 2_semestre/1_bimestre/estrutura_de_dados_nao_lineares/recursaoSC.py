def fatrecsc (num, fat = 1):

    if num == 1 or num == 0:
        print(fat)
    else:
        fatrecsc(num - 1, fat * num)

fatrecsc(int(input('Digite um valor: ')))

