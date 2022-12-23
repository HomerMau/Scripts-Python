#Faça um algritmo que leia duas notas de um aluno, calcule e mostre sua média

not1 = float(input('Digite a primeira nota do aluno: '))
not2 = float(input('Digite a segunda nota do aluno: '))
notm = (not1 + not2) / 2
print('O calculo da nota média do aluno foi {:.2f}'.format(notm))