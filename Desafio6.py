#Crie um algoritmo que leia um número e mostre seu dobro triplo e raiz quadrada

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O numero que você colocou foi {}, o dobro dele é {}, o triplo é {}, e a raiz quadrada é {:.2f}'.format(n, d, t, r))