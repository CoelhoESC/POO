"""
Associação -> Representa uma relação entre duas classes que pode ser bidirecional ou unidirecional. Pode ser um relacio-
namento simples entre duas classes, ""indicando que uma classe usa ou é usada por outra classe, sem nunhum tipo de depen-
dencia forte.""
"""


class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__mao = None  # Esse atributo recebe uma classe

    @property
    def nome(self):
        return self.__nome

    @property
    def mao(self):
        return self.__mao

    @mao.setter
    def mao(self, atributo):
        self.__mao = atributo


class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self, assunto):
        print(f'esta escrendo sobre {assunto}')

    def desenhando(self, desenho):
        print(f'esta desenhando um {desenho}')


print('ASSOCIANDO')
escritor = Escritor('Everton')
caneta = Caneta('Bic')
escritor.mao = caneta  # estao associada!
escritor.mao.escrever("Comunismo")
escritor.mao.desenhar('Pai')
