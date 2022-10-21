from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('benjamin', 20)
cliente2 = Cliente('benjamin', 22)
cliente3 = Cliente('benjamin', 23)

conta1 = ContaPoupanca(1111, 233332, 0)
conta2 = ContaCorrente(2222, 233332, 0)
conta3 = ContaPoupanca(1113, 23333, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('cliente nao autenticado')
