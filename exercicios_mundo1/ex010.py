# Exercício 10: criar um programa que leia quanto de dinheiro em reais (R$) uma pessoa tem na carteira e mostre quantos dólares (US$) ela pode comprar.
reais = float(input('Quantos R$ você tem?'))
dólar = 5.23
print(f'Com esse dinheiro você pode comprar US$ {reais/dólar:.2f}.')