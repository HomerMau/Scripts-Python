#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

prec = float(input('Digite o preço do produto: '))
precd = prec*0.95
print('O valor com disconto é {} R$'.format(precd))