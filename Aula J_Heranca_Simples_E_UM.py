"""
Herança simples - (É um)
Basicamente existe um classe 'pai' (classe superior), e as classes 'filhos' herdam metodos da classe 'pai'
Porem as class 'filhos' podem ter seus metodos, que nao seram acessados pela class 'pai'!
"""


class Pessoa:  # class pai
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClass = self.__class__.__name__  # nome da classe

    def falar(self):
        print(f'{self.nomeClass} esta falando!')


class Cliente(Pessoa):  # class filho
    def comprar(self):
        print(f'{self.nomeClass} esta comprando!')


class Aluno(Pessoa):  # class filho
    def estudar(self):
        print(f'{self.nomeClass} está estudando!')  # mostra o nome da class!


C1 = Cliente('Everton', 22)
print(C1.nome)
C1.falar()  # acessando metodo da classe pai
C1.comprar()
print()
A1 = Aluno('Airton', 56)
print(A1.nome)
A1.estudar()
