from ContasBancos import cartaocredito, ContaCorrente

#programa
conta_Jose = ContaCorrente('Jose', '122.555.333-44', 1234, 0o00152)
conta_Jose.ConsultarSaldo()
print(30*'_')

#depositar um dinheiro na conta do Jose
conta_Jose.depositar(30000)
conta_Jose.ConsultarSaldo()
print(30*'_')

#sacar um dinheiro da conta do jose
conta_Jose.sacar_dinheiro(10500)
conta_Jose.ConsultarSaldo()
print(30*'_')

conta_Jose.consultar_limite_chequeespecial()
print(30*'_')

conta_Jose.consultar_historico_transacoes()
print(30*'_')

#criar conta destino e fazer deposito
conta_maria = ContaCorrente('maria', '144.666.555-24', 2223, 222654)
conta_Jose.transferir(5000, conta_maria)

conta_Jose.ConsultarSaldo()
conta_maria.ConsultarSaldo()
print(30*'_')

conta_Jose.consultar_historico_transacoes()
print(30*'_')
conta_maria.consultar_historico_transacoes()

cartao_jose = cartaocredito('jose', conta_Jose)
print(cartao_jose.validade)
print(cartao_jose.numero)
print(cartao_jose.cod_seguranca)
print(30*'_')

cartao_jose.senha = '2568'
print(cartao_jose.senha)

# Método(__dict__) consultar todas as informações da conta
print(conta_Jose.__dict__)
print(cartao_jose.__dict__)
