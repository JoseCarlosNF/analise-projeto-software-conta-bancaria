from datetime import date


class contaCriada:
    def __init__(self, data_abertura: date) -> None:
        self.data_abertura = data_abertura


class contaFechada:
    def __init__(self, data_encerramento: date) -> None:
        self.data_encerramento = data_encerramento


class contaDevedora:
    pass


class contaDisponivel:
    pass


class ContaBancaria:
    def __init__(self, numero, saldo: float, limite: float) -> None:
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def criar(self, data_abertura: date):
        self.state = contaCriada(data_abertura)

    def fechar(self, data_encerramento: date):
        if type(self.state) is not contaDevedora:
            self.state = contaFechada(data_encerramento)

    def depositar(self, valor: float):
        self.saldo += valor
        if self.saldo > 0:
            self.state = contaDisponivel()
        else:
            self.state = contaDevedora()

    def sacar(self, quantia: float):
        if self.saldo >= quantia:
            # saca apenas do saldo
            self.saldo -= quantia
            pass
        elif self.saldo + self.limite >= quantia:
            # zera saldo e completa com limite
            self.saldo -= quantia
            self.limite += self.saldo
            self.state = contaDevedora()
        else:
            print(f'Valor acima do disponível. {self.saldo + self.limite}')

    def aplicarJuros(self):
        if self.state == contaDevedora:
            # aplica juros a cada 30 dias
            pass


class Agencia:
    def __init__(self, numero, nome: str) -> None:
        self.numero = numero
        self.nome = nome


class Correntista:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf

if __name__ == '__main__':
    # Cria conta bancaria
    conta = ContaBancaria(123, 1000, 100)
    conta.criar(date(2022, 11, 9))

    # Consulta estado atual
    print(f'Estado atual: {conta.state}')

    # Consulta saldo atual
    print(f'Saldo atual: {conta.saldo}')
    print(f'Limite atual: {conta.limite}')

    # Realizar saque
    conta.sacar(1100) # saca tudo, zera limite e saldo

    # Estado após zerar saldo e limite
    print(f'Estado após consumir limite: {conta.state}')
    print(f'Saldo após consumir saldo e limite: {conta.saldo}')

    # Estado após fechar conta
    conta.fechar(date(2022, 11, 9))
    print(f'Estado após tentar fechar com estado devedor: {conta.state}')
