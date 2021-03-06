def calculaValorEmprestimo(valor):
    return (valor * 10 / 100) + valor

def printProsseguirComProcesso(nome, cpf):
    print(f'Prosseguir com o processo para o cliente {nome}, portador do cpf {cpf}.')

def processaFinanciamentoVeiculo(nome, cpf, dataNascimento, salario, cep, quantidadeAnos):
    
    possuiCnh = input("Possui CNH? \n S - sim \n N - não \n")
    
    if possuiCnh == 'S':
        possuiCnh = True
    else:
        possuiCnh == False
    
    if possuiCnh == True and salario <= 2000:
        printProsseguirComProcesso(nome, cpf)
        print("valor liberado foi R$ 40000")
        parcelas = quantidadeAnos * 12
        valorParcela = calculaValorEmprestimo(40000) / parcelas
        print(f'Parcelas: {parcelas}x R${valorParcela}')
    
    if possuiCnh == True and salario > 2000 and salario <= 5000:
        printProsseguirComProcesso(nome, cpf)
        print("valor liberado foi R$ 80000")
        parcelas = quantidadeAnos * 12
        valorParcela = calculaValorEmprestimo(80000) / parcelas
        print(f'Parcelas: {parcelas}x R${valorParcela}')
        
    if possuiCnh == True and salario > 5000 and salario <= 10000:
        printProsseguirComProcesso(nome, cpf)
        print("valor liberado foi R$ 120000")
        parcelas = quantidadeAnos * 12
        valorParcela = calculaValorEmprestimo(120000) / parcelas
        print(f'Parcelas: {parcelas}x R${valorParcela}')
        
    if possuiCnh == True and salario > 10000:
        printProsseguirComProcesso(nome, cpf)
        print("valor liberado foi R$ 150000")
        parcelas = quantidadeAnos * 12
        valorParcela = calculaValorEmprestimo(150000) / parcelas
        print(f'Parcelas: {parcelas}x R${valorParcela}')
        
    else:
        print(f'Financiamento não liberado {nome}, portador do cpf {cpf}.')