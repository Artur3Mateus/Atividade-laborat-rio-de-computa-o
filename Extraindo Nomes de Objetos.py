def extrair_nomes(lista_objetos):
    nomes = []
    for obj in lista_objetos:
        nomes.append(obj.nome)
    return nomes
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

pessoas = [Pessoa("Artur"), Pessoa("Mateus"), Pessoa("Ana")]

print(extrair_nomes(pessoas))