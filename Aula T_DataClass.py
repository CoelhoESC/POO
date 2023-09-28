"""
DataClasses

O que são DataClasses? O modelo Dataclasses fornece um decorador e funçoes para criar automaticamente metodos, como
__init__(), __repr__(), __eq__(), etc. Em classes definidas pelo usuario.
Basicamente, dataclasses sao syntax sugar para criar classes normais. Foi originalmente descrito na PEP 557.

frozen = se tiver em True, nao permite mexer na classe
order = Ordenar as classes

"""
from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple
"""
@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f' {self.nome} {self.sobrenome}'
"""


# Pode usar o init
@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)  # Desativando ou ativando
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)  # Desativa repr dessa variavel - retorna o nome organizado!

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'
        if not isinstance(self.nome, str):
            raise (TypeError(f' Tipo invalido {type(self.nome)} != str em {self}'))


P1 = Pessoa('Everton', 'Coelho')
P2 = Pessoa('Airton', 'Coelho')
P3 = Pessoa('Fabiana', 'Coelho')
P4 = Pessoa('Cléa', 'Coelho')
# P5 = Pessoa(12345, 'Coelho')

pessoa = [P1, P2, P3, P4]
print(sorted(pessoa))
print()
print(P1)
print(P1 == P2)
print()
print(asdict(P1))  # Convertendo
print(astuple(P2))
