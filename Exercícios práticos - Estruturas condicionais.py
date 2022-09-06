'''
-------------------------------------------------
| Exercícios práticos - Estruturas condicionais |
| Aluna: Julia Alencar Fonseca Dias             |
-------------------------------------------------
'''

## Exercício 1
tam_seq = 64
if tam_seq >= 50:
	print('Sequência aceita')
else:
	print('Sequência rejeitada')

## Exercício 2
seq = 'GMWINNDQIYNSLITSHAFLMIFFMVMPFMIGGFGNFLIPLMLGSPDMAFPRMNNVSFWLLPPSLIMLLLSNFFFPKSGTGWTVYPPLSSYLFHSSPSVNLTIFSIHMTGISSILGSLNFIVTIFMMKNFSLNYDQISLFSWSLSVTVVLLIVSLPVLAGAITMLLFDRNFNTSFFDPTGGGDPILYQHLFWFFG'
if len(seq) >= 2 and len(seq) <= 50:
	print('A sequência é um peptídeo, pois seu tamanho é', len(seq))
else:
	print('A sequência não é um peptídeo, pois seu tamanho é', len(seq))

##Exercício 3
aa = 'EEERQKDKRDRFHGLMGRSNEEERQHPGSSRRD'
if len(aa) == 2:
  print("É um dipeptídeo")
elif len(aa) == 3:
  print("É um tripeptídeo")
elif len(aa) >=4 and len(aa) <= 50:
  print("É um polipeptídeo")
else:
  print("Não é um peptídeo")


## Exercício 4
hidrofobico = ['I', 'V', 'L', 'M', 'C', 'A', 'T', 'F', 'Y', 'W', 'H', 'K']
pequeno = ['P', 'A', 'G', 'C', 'S', 'T', 'D', 'N', 'V']
polar = ['C', 'S', 'T', 'N', 'D', 'Q', 'Y', 'W', 'H', 'K', 'R', 'E']
carregado = ['D', 'E', 'R', 'K', 'H']
aromatico = ['F', 'Y', 'W', 'H']
minusculo = ['A', 'C', 'G', 'S']
alifatico = ['I', 'L', 'V']
hidroxila = ['T', 'S']
acido = ['N', 'Q']
enxofre = ['C', 'M']
aa = 'S'
if aa in hidrofobico:
  print('Hidrofóbico')
if aa in pequeno:
  print('Pequeno')
if aa in polar:
  print('Polar')
if aa in carregado:
  print('Carregado')
if aa in aromatico:
  print('Aromatico')
if aa in minusculo:
  print('Minúsculo')
if aa in hidroxila:
  print('Hidroxila')
if aa in acido:
  print('Ácido')
if aa in enxofre:
  print('Enxofre')


## Exercício 5
aa = 'V'
if (not aa in polar) or (not aa in carregado):
  print('Aminoácido é apolar ou neutro.')


## Exercício 6
n = 'C'
nucleotideos = ['A', 'C', 'T', 'G']
purinas = ['A', 'G']
pirimidina = ['C', 'T']
if n in nucleotideos:
  print('É um nucleotídeo válido')
  if n in purinas:
    print('Purina')
  elif n in pirimidina:
    print('Pirimidina')   
else:
  print('É um nucleotídeo inválido')
