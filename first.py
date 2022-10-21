from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg):
        print(f'B esta falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C esta falando {msg}')


b = B()
c = C()
b.fala('um assunto')
c.fala('outro assunto')