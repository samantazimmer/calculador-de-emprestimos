p1 = float(input("Qual é o valor da casa? R$ "))
p2 = float(input("Qual é o salario do comprador? R$ "))
p3 = int (input("Quantos anos de financiamento? "))

calculo = p1 / (p3 * 12)
minimo = p2 * 30 / 100
print ('Para pagar uma casa de R$ {:.2f} reais, em {} anos'.format(p1,p3))
print ('A prestação ficara R$ {:.2f} reais.'.format(calculo))
if calculo <= minimo:
    print ("Emprestimo pode ser concedido!")
else:
    print ("Emprestimo negado!")