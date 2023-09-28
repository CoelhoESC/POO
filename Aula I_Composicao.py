"""
Composição - Relação mais forte entre classes!
Uma classe vai ser dona de objetos de outra classes, ou seja, se a classe principal for apagada, todos os objetos
que a class principal utilizar, serão apagados tambem!
"""


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderedo = []  # Recebe objetos de outra classe

    def inserir_endereco(self, cidade, Estado):
        self.enderedo.append(Enderecos(cidade, Estado))  # recebendo a instancias

    def listar_endereco(self):
        for ende in self.enderedo:
            print(ende.cidade, ende.Estado)

    def __del__(self):
        print(f'{self.nome} foi apagado ')


class Enderecos:
    def __init__(self, cidade, Estado):
        self.cidade = cidade
        self.Estado = Estado

    def __del__(self):
        print(f'{self.cidade}/{self.Estado} foi apagado')


cliente1 = Cliente('Everton', 22)
print(cliente1.nome)
cliente1.inserir_endereco('Araraquara', 'São Paulo')
cliente1.listar_endereco()
del cliente1  # utilizando só a class Cliente, foi apagado os objetos da class Endereco
print()

cliente2 = Cliente('Airton', 56)
print(cliente2.nome)
cliente2.inserir_endereco('Araraquara', 'SP')
cliente2.inserir_endereco('Campinas', 'SP')
cliente2.listar_endereco()
del cliente2

Cliente_3 = Cliente("Bruno", 25)
Cliente_3.inserir_endereco()
