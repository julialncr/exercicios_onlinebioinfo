'''
---------------------------------------------
| Exercícios práticos - Dicionários         |
| Aluna: Julia Alencar Fonseca Dias         |
---------------------------------------------
'''

## Exercício 1


# a) Construa um dicionário onde os ids PDB sejam as chaves e o número de resíduos de aminoácidos sejam o valor.
Dicionario={'1A8M':471,'1TNR':283, '2AZ5':592, '1TNF':471, '2TNF':468, '2TUN':942, '4TSV': 150 ,'5TSW' : 900,'2E7A':471,'6RMJ':489	}
print(Dicionario)

# b) Imprima os valores contidos nos ids 2TNF e 2E7A.
print(Dicionario['2TNF'])
print(Dicionario['2E7A'])

# c) Verifique e imprima o tamanho do dicionário construído
len(Dicionario)

# d) Obtenha e imprima a lista de todas as chaves do dicionário
print(Dicionario.keys())

# e) Obtenha e imprima a lista de todos os valores do dicionário
print(Dicionario.values())

# f) Obtenha e imprima uma lista de tuplas com todos os pares chave-valor. Cada dupla será um par ordenado (chave, valor).
tuplas = Dicionario.items()
print(tuplas)

