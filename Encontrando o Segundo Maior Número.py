def segundomaior(numeros):
    unicos = list(set(numeros))
    unicos.sort(reverse=True)
    return unicos[1]

lista = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
print(segundomaior(lista))
