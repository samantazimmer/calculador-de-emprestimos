def processaFinanciamentoTerreno(nome,cpf,salario,quantidadeAnos):
    valorTerreno = float(input('Insira o valor do terreno: '))
    valorTotalPagamento = (valorTerreno * 10 / 100) + valorTerreno
    
    valorParcela = valorTotalPagamento / (quantidadeAnos * 12)
    trintaPorcentoSalario = salario * 30 / 100
    
    print(f'Para pagar um terrno de R$ {valorTerreno} em {quantidadeAnos} anos.')
    print(f'A prestação ficará {valorParcela}.')
    
    if valorParcela <= trintaPorcentoSalario:
        print(f'Emprestimo concedido para {nome}, portador do cpf {cpf}.')
    else:
        print(f'Emprestimo negado para {nome}, portador do cpf {cpf}.')