# Exercício 13: faça um algoritmo que leia o salário atual de um funcionário e mostre seu novo salário com 15% de aumento.
salario_atual = float(input('Quanto você está ganhando atualmente? R$'))
aumento_pct = float(input('Qual será a taxa de aumento em %? '))
aumento = aumento_pct/100
print(f'Com o aumento de {aumento_pct}%, seu salário será de R${(salario_atual*(1+aumento)):.2f}')

#Deixei possível colocar a taxa de aumento que quiser