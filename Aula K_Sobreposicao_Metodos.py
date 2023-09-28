"""
Sobreposição de membros/metodos - Reescrever outro metodo, que ja exista!
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

    def falar(self):  # Sobreescrita
        print('falar da classe Cliente')


class Aluno(Pessoa):  # class filho
    def estudar(self):
        print(f'{self.nomeClass} está estudando!')  # mostra o nome da class!


class ClienteVIP(Cliente):  # herdando de Cliente e Pessoa!
    def __init__(self, nome, idade, sobrenome):  # para nao reescrever o metodo pai!
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        super().falar()  # buscando da class superior
        Pessoa.falar(self)
        Cliente.falar(self)


C1 = ClienteVIP('Everton', 22, 'Coelho')
C2 = Cliente("Airton", 57)

# interpretador do python busca na class ClienteVIP, depois na Class Cliente, e por fim na class Pessoa
print(f"classe ClienteVIP", C1.idade)
print(f"classe ClienteVIP", C1.sobrenome)
C1.falar()  # mesmo sendo da classe ClienteVIP, o metodo é chamado da class super

print()
# MRO Ordem de chamada de metodos
C2.falar()  # Ocorre uma sobrescrita
