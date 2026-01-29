# Exercício 15: calcular valor pago pelo aluguel de carros, através da quilometragem percorrida e dias de aluguel. Sabe-se que o aluguel do carro custa R$60/dia e R$0.15/km rodado.
dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Qual foi a quilometragem total percorrida pelo carro durante o aluguel? '))
aluguel_final = 60*dias + 0.15*km
print(f'O valor total a ser pago pelo aluguel do carro durante {dias} dias e após utilizá-lo para percorrer {km} km é de R${aluguel_final:.2f}.')
