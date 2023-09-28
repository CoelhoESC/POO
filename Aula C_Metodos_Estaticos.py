"""
Metodos estaticos
self -> Metodo para instancia
cls -> Metodo para classes (variaveis globais)
Para o metodo estatico, não precisa defenir os parametros
"""
from random import randint


class Pessoa:
    @staticmethod
    def gera_id():
        rand = randint(100000, 999999)
        return rand


pessoa1 = Pessoa
print(pessoa1.gera_id())
print(Pessoa.gera_id())
