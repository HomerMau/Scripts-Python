#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com um aumento de 15%

sal =  float(input('Digite o salario do funcionario: '))
nsal = ((sal*0.15) + sal)
print('O novo salário será: {}'.format(nsal))