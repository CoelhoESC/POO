from enum import Enum, auto
from dataclasses import dataclass


@dataclass
class Direcao(Enum):
    direita = auto()  # Name = value
    esquerda = auto()   # Auto gera automaticamente
    cima = auto()
    baixo = auto()


def mover(direcao):
    if not isinstance(direcao, Direcao):
        raise ValueError('Você não pode fazer esse movimento')

    return f'Movendo para {direcao.name}'


if __name__ == '__main__':
    print(mover(Direcao.direita))
    print(mover(Direcao.esquerda))
