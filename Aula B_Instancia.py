"""
Metodo relacionado com a instancia da classe
"""


# Existe metodo relacionado com a classe
class Pessoa:
    ano_atual = 2022  # esta ligado a instancia e, é um atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return f'Seu ano de nacimento {self.ano_atual - self.idade}'

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


# Usando os metodos da instancia
Pessoa1 = Pessoa('Luiz', 33)
print(Pessoa1.get_ano_nascimento())
print(Pessoa1.idade)

# Usando o metodo da class
Pessoa2 = Pessoa.por_ano_nascimento('Everton', 1999)
print(Pessoa2.__class__)
print(Pessoa2.nome, Pessoa2.idade)

