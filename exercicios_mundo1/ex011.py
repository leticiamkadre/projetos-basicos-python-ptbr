# Exercício 11: faça um programa que leia a largura e altura de uma parede em metros. Calcule a área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m². Bônus: cálculo do total de dinheiro necessário, sabendo que o preço é R$4.89. 
largura = float(input('Qual a largura da parede, em metros?'))
altura = float(input('Qual a altura da parede, em metros?'))
área = largura*altura
rendimento_tinta = 2
preço_tinta = 4.89
print(f'Para pintar a área de {área} m², serão necessários {área/rendimento_tinta} L de tinta, e gastará R${(área/rendimento_tinta)*preço_tinta:.2f}.')

# Deixei a possibilidade do rendimento e do preço da tinta serem variáveis.