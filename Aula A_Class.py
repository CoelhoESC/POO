"""
Class - molde (POO)
Tratar coisas do mundo real, como objetos dentro do seu programa
__init__ -> Consultor, funcionalidade incial (atributo)

"""


class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def esta_comendo(self, alimento):
        if self.falando:
            print(f'{self.nome}, não pode comer, pois esta conversando')
            return
        print(f'{self.nome} está comendo {alimento} agora')
        self.comendo = True

    def esta_conversando(self, assunto):
        if self.comendo:
            print(f'{self.nome}, não pode conversa, pois esta comendo!')
            return
        print(f'{self.nome} está conversando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        print(f'{self.nome} parou de conversa!')
        self.falando = False

    def parar_comer(self):
        print(f'{self.nome} parou de comer!')
        self.comendo = False


Pessoa1 = Pessoa('Everton', 22)
Pessoa2 = Pessoa('Anna', 23)
Pessoa2.esta_conversando('Faculdade')
Pessoa1.esta_comendo('Hot DOG')
Pessoa2.parar_falar()
Pessoa2.esta_comendo('Abacaxi')
Pessoa1.esta_conversando('Mulheres')
Pessoa1.parar_comer()
Pessoa1.esta_conversando('Carro')
