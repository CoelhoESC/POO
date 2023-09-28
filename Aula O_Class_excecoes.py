"""
Criando exceçoes (levantando exceçoes, personalizando exceçoes)
"""


class EstaErradoERROR(Exception):
    pass


def testar():
    raise EstaErradoERROR('Está errado!')


try:
    testar()
except EstaErradoERROR as error:
    print(f'Erro: {error}')
