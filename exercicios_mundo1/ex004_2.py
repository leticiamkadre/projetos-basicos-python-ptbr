# Exercício 4.2: executar operações aritméticas básicas para dois números 
n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número:'))
s = n1 + n2
su = n1 - n2
m= n1 * n2
e = n1 ** n2
d = n1 / n2 
r = n1 % n2 
di = n1 // n2
print(f'A soma é {s}, a multiplicação é {m} e a subtração é {su}') 
print(f'Ao dividir {n1} e {n2}, temos {d:.2f}, com quociente {di} e resto igual a {r}') #esse :.2f significa a indicação de mostrar com 2 casas flutuantes
