#Façaum programa que leia a largura e a altura de uma paredeem metros, calcule a sua area e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

lar = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
are = lar * alt
tin = are / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lar, alt, are))
print('Para pintar essa parede você precisará de {}l de tinta.'.format(tin))