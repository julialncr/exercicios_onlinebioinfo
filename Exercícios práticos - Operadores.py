'''
---------------------------------------------
| Exercícios práticos - Operadores          |
| Aluna: Julia Alencar Fonseca Dias         |
---------------------------------------------
'''

## Exercício 1
x = 1
y = 2
print(x == y)

## Exercício 2
a = 5
b = 8
c = 7
d = 9
e = 10
media = (a + b + c + d + e)/5
print(media)

## Exercício 3
base = 3
expoente = 3
print(base*expoente)

## Exercício 4
x = 36
y = 4
print((x%y)==0)

## Exercício 5
print(x // y)

## Exercício 6
tam = 28
print(tam >= 5 and tam <= 30)

## Exercício 7
tam = 32
print(tam >= 5 and tam <= 30)

## Exercício 8
aa1 = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
letra = 'Z'
print(letra in aa1)

## Exercício 9
pos = ['H', 'K', 'R']
neg = ['D', 'E']
aa2 = 'R'
print('Esse aminoácido é carregado? R =', aa2 in pos or aa2 in neg )
print('Esse aminoácido é neutro? R =', not aa2 in pos and not aa2 in neg )
