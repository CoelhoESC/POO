"""
Agregação -> Representa uma relação de todo_-parte entre duas classes, onde uma classe A (todo_) contem uma ou mais
instancia de outra classe B (parte), mas a classe B pode existir independentemente da classe A.
"""


class CarrinhoDeCompra: # Classe Todo_
    def __init__(self):
        self.carrinho = []

    def inserir_produto(self, produto):  # Esse metodo esta guardando os valores da outra classe!
        self.carrinho.append(produto)

    def listar_compras(self):
        if self.carrinho:
            for produto in self.carrinho:
                print(f' Nome: {produto.nome} e preço: {produto.preco}')
        else:
            print('Seu carrinho esta vazio!')

    def total(self):
        total = 0
        for produto in self.carrinho:
            total += produto.preco
        return total

    def apagar(self, ID):
        del self.carrinho[ID]


class Produto: #Classe Parte
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = CarrinhoDeCompra()

p1 = Produto('Macarrão', 10)
p2 = Produto('Celular', 1000)
p3 = Produto('Camiseta', 50)
p4 = Produto('Caderno', 25)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p4)
carrinho.apagar(0)


carrinho.listar_compras()
print(f'Total: {carrinho.total()}')
