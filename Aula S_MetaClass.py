"""
MetaClasse - São as 'classes' que criam classes.
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):  # Metaclasse, nome, pai(herança), metodo
        if name == 'A':  # Nao retorna nada de A
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace: # Se 'b_fala nao estiver em metodo
            print(f'Oi você precisa criar o metodo b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):  # chamando!
                print(f'b_fala precisa ser um metodo, não atributo em {name}')

        return type.__new__(mcs, name, bases, namespace)  #


class A(metaclass=Meta):
    def falar(self):
        self.b_fala()


class B(A):

    def b_fala(self):
        print('Oi, B esta falando!')
