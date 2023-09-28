"""
@property (getter) -> Obtem um valor
Setter -> Configura o valor
Usado para não precisa modificar os valores dos metodos ja criado
"""


# EX: trabalhando em uma classe para e-commerce
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual, aumentar=False):
        if aumentar:
            self.preco = self.preco + (self.preco * percentual / 100)
            return self.preco
        self.preco = self.preco - (self.preco * percentual / 100)
        return self.preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):  # Verificando se é uma str
            valor = float(valor.replace('R$', '').replace(',', '.'))
        self._preco = valor


# Getter e setter -> Uma proteção para o atributo
produto1 = Produto('Salgado', 'R$15.50')
print(produto1.preco)
print(produto1.desconto(10))
print(type(produto1.desconto(10)))
