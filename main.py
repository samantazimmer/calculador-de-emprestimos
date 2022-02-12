from financiamentoVeiculo import processaFinanciamentoVeiculo
from financiamentoCasa import processaFinanciamentoCasa

def printLinha():
    print("=========================")


printLinha()
print("Simulação de financiamentos")
printLinha()
nome = str(input('Insira seu nome: '))
cpf = str(input('Insira seu cpf: '))
dataNascimento = str(input('Insira a data de nascimento: '))
salario = float(input('Insira seu salário: '))
cep = str(input('Insira seu cep: '))
quantidadeAnos = int(input('Insira a quantidade de anos de financiamento:'))
printLinha()

print("Opções de financiamento: ")
print("1 - Financiamento de veículo")
print("2 - Financiamento de casa")
print("3 - Financiamento de terreno")
opcao = int(input("Insira sua opção: "))

if opcao == 1:
    processaFinanciamentoVeiculo(nome, cpf, dataNascimento, salario, cep, quantidadeAnos)
    
if opcao == 2:
    processaFinanciamentoCasa(nome, cpf, salario, quantidadeAnos) 

if opcao == 3:
    print("Processando financiamento de terreno")