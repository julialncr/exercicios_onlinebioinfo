'''
-------------------------------------
| Estruturas de repetição           |
| Aluna: Julia Alencar Fonseca Dias |
-------------------------------------
'''
## Exercício 1
#1.
for i in range(0,11): # [0,11) que é equiv. [0,10]
  print(i)

#2.
i = 0
while i <= 10:
  print(i)
  i+=1

##Exercício 2
#1.
for i in range(0,11,2): # [0,11) que é equiv. [0,10]
  print(i)

#2.
i = 0
while i <= 10:
  print(i)
  i+=2

##Exercício 3
DNA = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
n = ['A', 'C', 'G', 'T']

for i in range(0,len(DNA)):
  if not DNA[i] in n:
    print("Não é uma sequência válida de DNA: ", DNA[i])
    break

if i == len(DNA)-1:
  print("É uma sequência válida de DNA.")

##Exercício 4
for n in range(1,101): # Percorrer os 100 números
  div = []
  for d in range(1,n+1): # Percorrer os n possíveis divisores de um número
    if n%d == 0:  
      div.append(d)  
  print(n, div)

##Exercício 5
for n in range(1,1001): # 
  div = []
  for d in range(1,n+1): # Percorrer os n possíveis divisores de um número
    if n%d == 0:  
      div.append(d)  
  if len(div) == 2:
    print(n, end=" ")

##Exercício 6
seq = "VRSSSRTPSDKPVAAAAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLAAAFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKAAASPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAAAAEINRPDYLLFAESGQVYFGIIAL"
for i in range(0,len(seq)):
  if seq[i:i+3] == "AAA":
    print("AAA em", i)

##Exercício 7
bd = ['KTCENLA', 'DTFR', 'GPCFTDGSC', 'DDHCKNKEHLIK', 'GRCRDDFRC', 'WCTRNC', 'ATC']
maiorTam = 0
maiorInd = 0
for i in range(0,len(bd)):
  if len(bd[i]) > maiorTam:
    maiorTam = len(bd[i])
    maiorInd = i
print(bd[maiorInd], maiorTam)

##Exercício 8
l = [1,4,6,3,4,5,7,8,9,5,6,7,4,3,5,6,7,8]
soma = 0
for i in range(0, len(l)):
  soma += l[i]
media = soma / len(l)
print(media)