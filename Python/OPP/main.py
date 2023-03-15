class Conta:


    def __init__(self, titular, saldo, limite):
        self._titular = titular
        self._saldo   = saldo
        self._limite  = limite


    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))


    def deposita(self, valor):
        self._saldo += valor


    def saca(self, valor):
        self._saldo -= valor


    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


    # Getters e Setters usando @property
    @property
    def saldo(self):
        return self._saldo


    @property
    def titular(self):
        return self._titular


    @property
    def limite(self):
        return self._limite


    @limite.setter
    def limite(self, limite):
        print('setter')
        self._limite += limite



minha_conta = Conta("Vitor", 1000, 5000)


print(minha_conta.limite)

