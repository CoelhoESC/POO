"""
Atributos de classes
As variaveis da classe são globais, e fica disposto para todas as instancias
"""


class A:
    voce = 123


a1 = A()  # <- instancia
a2 = A()
print(a1.voce)
print(A.voce)
print(a2.voce)

print()
A.voce = 321  # <- A variavel vai mudar
print(a1.voce)
print(A.voce)

print()
a1.voce = 345  # Não altera o valor da variavel da classe
print(a1.__dict__)  # Retonar um dicionario com todos os conteudo das classes
print(A.__dict__)
print(a2.__dict__)
