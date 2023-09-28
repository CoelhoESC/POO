"""
Herança Multipla!
"""


class A:
    def falar(self):
        print('Classe A esta falando!')


class B(A):
    def falar(self):
        print('Classe B esta falando')


class C(A):
    def falar(self):
        print('Classe C esta falando')


class D(B, C):  # herança multipla!
    pass


d = D()
# MRO
d.falar()  # interpretador o python busca o metodo na primeira class a encontrar!
