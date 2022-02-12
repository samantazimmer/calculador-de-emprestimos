def processaFinanciamentoCasa(nome,cpf,salario,quantidadeAnos):
    valorCasa = float(input('Insira o valor da casa: '))
    valorTotalPagamento = (valorCasa * 10 / 100) + valorCasa
    
    valorParcela = valorTotalPagamento / (quantidadeAnos * 12)
    trintaPorcentoSalario = salario * 30 / 100
    
    print(f'Para pagar uma casa de R$ {valorCasa} em {quantidadeAnos} anos.')
    print(f'A prestação ficara {valorParcela}.')

    if valorParcela <= trintaPorcentoSalario:
        print(f'Emprestimo concedido para {nome}, portador do cpf {cpf}.')
    else:
        print(f'Emprestimo negado para {nome}, portador do cpf {cpf}.')
