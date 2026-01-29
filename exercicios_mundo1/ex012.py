# Exercício 12: faça um algoritmo que leia o preço atual de um produto e mostre seu novo preço com 5% de desconto.
preço_atual = float(input('Qual o preço atual do produto?'))
desconto_pct = float(input('Qual o desconto em %?'))
desconto = desconto_pct/100
print(f'O novo preço desse produto com desconto de {desconto_pct}% é R${(preço_atual*(1-desconto)):.2f}')

#Deixei possível colocar a taxa de desconto que quiser