class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('Caixa está Ok. Caixa Atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Dinheiro náo disponível em caixa')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class Agenciavirtual(Agencia):
    pass

class AgenciaComum(Agencia):
    pass

class AgenciaPremium(Agencia):
    pass

# PROGRAMA
Agencia = Agencia(25648888, 22222222222, 66666444)
Agencia.caixa = 1000000
Agencia.verificar_caixa()

Agencia.emprestar_dinheiro(20000, 2564855555, 0.02)
print(Agencia.emprestimos)

Agencia.adicionar_cliente("Carlos", 10411111111, 1000000)
print(Agencia.clientes)