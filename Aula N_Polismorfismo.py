"""
Polismorfismo
"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self, msg): pass


class B(A):
    def falar(self, msg):  # Recebe a mesma quantidade de parametros
        print(f'B esta falando {msg}')


class C(A):
    def falar(self, msg):  # Mesmo recebendo a mesma quantidada, a função do metodo é diferente!
        print(f'C esta falando {msg}')


C = C()
C.falar("Bom dia")
B = B()
B.falar("Te amo pai")
