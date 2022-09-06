'''
---------------------------------------------
| Exercícios práticos - Tuplas              |
| Aluna: Julia Alencar Fonseca Dias         |
---------------------------------------------
'''

#Exercício 1
t = ('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')

# a) Conte e imprima o número de elementos contidos na tupla criada.
print(len(t))

# b) Verifique e imprima se o aminoácido Serina (S) pertence à tupla.
print('S' in t)

# c) Crie uma segunda tupla contendo os elementos Prolina (P), Glicina (G), Asparagina (N), Tirosina (Y), Valina (V) e Triptofano (W).
t2 = ('P', 'G', 'N', 'Y', 'V', 'W')

# d) Some as tuplas construídas e imprima o resultado.
soma = t + t2
print(soma)

# e) Conte a ocorrência dos elementos Glicina (G), Asparagina (N) e Cisteína (C).
print(soma.count('G'))
print(soma.count('N'))
print(soma.count('C'))

# f) Retorne a posição do primeiro elemento Asparagina (N).
print(soma.index('N'))

# g) Retorne os 5 últimos elementos da tupla.
print(soma[-5:])