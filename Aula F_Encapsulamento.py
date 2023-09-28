"""
Encapsulamento
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}  # <- não tem acesso

    @property
    def dados(self):  # Para mostrar os valores
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for k, v in self.__dados['clientes'].items():
            print(f'ID: {k} - NOME: {v}')

    def apagar(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Everton')
bd.inserir_cliente(2, 'Anna')
bd.inserir_cliente(3, 'Airton')
bd.apagar(2)
bd.listar_clientes()
print(bd.dados)
