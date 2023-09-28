from abc import ABC, abstractmethod

"""
Class ABC, são classe que não podem instanciadas, apenas herdadas. 
"""


class A(ABC):
    @abstractmethod
    def falar(self):  # todas as class que herda de A, teram o metodo falar'
        pass


# class B(A):
# pass

# a = B()  # Não consegue instanciar a class, enquanto a Class B nao tiver o metodo falar


class B(A):
    def falar(self):
        print('Falando... B...')


b = B()
b.falar()
