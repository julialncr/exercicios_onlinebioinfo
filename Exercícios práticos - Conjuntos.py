'''
---------------------------------------------
| Exercícios práticos - Conjuntos           |
| Aluna: Julia Alencar Fonseca Dias         |
---------------------------------------------
'''

## Exercício 1
C1 = {1.9, 1.8, 5.7, 1.6, 5.8, 1.7, 9.6, 5.9, 9.5, 6.5, 6.2, 1.1,4.4, 3.5, 2.9, 4.7, 4.6, 5.2, 5.3}
C2 = {4.7, 3.6, 6.2, 7.1, 7, 5.6, 5.7, 3.4, 3.3, 2.1, 3.8, 3.9, 5, 5.1, 1.9, 9.5,  1, 1.3,5.4}
C3 = {2.2, 3.3, 5.1, 3, 3.7, 9.1, 8.8, 8.5, 2, 4.1, 6.1, 4.9, 1.1, 0.5, 0.8, 3.2, 6.9,9.3, 9.5}

# a) Verifique as diferenças entre os conjuntos (1,2), (1,3) e (2,3)
print('A diferença entre C1 e C2 é:', C1.difference(C2))
print('A diferença entre C1 e C3 é:', C1.difference(C3))
print('A diferença entre C2 e C3 é:', C2.difference(C3))

# b) Retorne as intersecções entre (1,2), (1,3) e (2,3)
print('A interseção entre C1 e C2 é:', C1.intersection(C2))
print('A interseção entre C1 e C3 é:', C1.intersection(C3))
print('A interseção entre C2 e C3 é:', C2.intersection(C3))

# c) Insira todos os elementos do conjunto 2 e 3 no conjunto 1
C1.update(C2, C3)
print('C1 + C2 + C3 =', C1)

# d) Retorne o tamanho do conjunto formado pela tarefa (c).
print(len(C1))

## Exercício 2
A = {3,6,9,12,15,18,21,24,28,27}
B = {2,6,8,10,14,16,18,20,22,24}
C = {2,6,10,18,20}
D = {1,30,5,11,17,16,22,26}

# a) 
print(A.difference(B))
print(A.intersection(B))

# b)
print(A.isdisjoint(D))
print(B.isdisjoint(D))

# c
print(C.issubset(A))
print(C.issubset(B))

# d)
D.update([18,23,65,63])
print(D)