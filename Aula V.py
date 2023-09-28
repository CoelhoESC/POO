# Implementando um Iterador

class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    # Protocolo para fazer um iterador
    def __int__(self):
        return self  # Class é seu proprio iterador -> transmiti o iterador para outra lista/class

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration  # Para dizer que a lista acabou!

    def __getitem__(self, item):  # Fazendo a função de obter um item da lista
        return self.__items[item]

    def __setitem__(self, key, value):  # Fazendo a função de trocar valores
        if key > len(self.__items):
            self.__items.append(value)  # Adicionando valor
        self.__items[key] = value

    def __delitem__(self, key):  # Deletando item
        del self.__items[key]

    # _____ Precisa desses dois metodos _____

    def __str__(self):
        return f'{self.__class__.__name__} ({self.__items})'


if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('Airton')
    lista.add('Everton')
    print(lista[0])
    lista[0] = 'Fabiana'
    lista[1] = 'ALGO'
    print(lista)
