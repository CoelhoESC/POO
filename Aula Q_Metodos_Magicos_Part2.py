"""
Metodos magicos
https://rszalski.github.io/magicmethods/
"""


# class A:
#    def __new__(cls, *args, **kwargs):
#       print('Eu sou o NEW')  # Executa primeito
#      return object.__new__(cls) # Toda class, deriva-se de object! Aqui retornará o INIT

#    def __init__(self):
#       print('Eu sou o INIT')


class B:
    def __init__(self, altura, base):
        self._altura = altura
        self.base = base

    def __setattr__(self, key, value):  # todas vez que atribuir, um atributo novo, é chamado para setar um atributo!
        if key == 'nome':
            self.__dict__[key] = 'Voce nao pode fazer isso'
        else:
            self.__dict__[key] = value

    def area(self):
        z = self._altura * self.base
        return z

    def __ge__(self, other):
        a1 = self.area()
        a2 = other.area()
        if a1 >= a2:
            return True
        else:
            return False

    def __iadd__(self, other):
        self.base += other.base
        return self.base


a = B(altura=15, base=25)
b = B(altura=10, base=20)
c = b >= a
print(c)
d = B(altura=30, base=20)
d.nome = 'Everton Coelho'
print(d.nome)

for x in range(10):
    b.base += a.base
    print(b.base)
