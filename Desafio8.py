#Escreva um programa que leia um valor em metros e o exiba convertido em cintimetros.

med = int(input('Digite o valor em metros: '))
cm = med * 100
mm = med * 1000
print('O valor em metros é {}, o valor em centímetros é {}cm, e o valor em milímetros é {}mm'.format(med, cm, mm))