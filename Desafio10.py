# Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dolares ela pode comprar

r = float(input('Digite o valor em "R$": '))
d = r / 5.17
print('O valor de {}, convertido de reais para dolares é: {:.2f}'.format(r, d))