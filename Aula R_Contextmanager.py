"""
Gerenciador de contextos
"""

"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando o arquivo')
        self.arquivo.close()
        # Levanta exeçóes
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True # apos tratar a exceção

with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Escrevendo no arquivo!')
    arquivo.uhsauhs('algo')  # error
"""
from contextlib import contextmanager


@contextmanager
def Abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with Abrir('abc.txt', 'a+') as arquivo:
    arquivo.write('Linha 1')
    arquivo.write('Linha 2')
    arquivo.write('Linha 3')
