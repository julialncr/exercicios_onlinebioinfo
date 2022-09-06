'''
---------------------------------------------
| Exercícios práticos - Variáveis - Strings |
| Aluna: Julia Alencar FOnseca Dias         |
---------------------------------------------
'''

# Exercício 1
# a)
seq = ('VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL')
print(len(seq))

# b)
print(seq.count ('LL'))

# c)
print(seq.find('GG'))
print(seq.find('RR'))

# d)
print(seq[:100])

# e)
seq_alanina = seq.replace('SSSR', 'AAAA')
print(seq)
print(seq_alanina)

# f)
print(seq_alanina.split('AAAA'))

# Exercício 2
# a)
texto = 'As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do nome.'
texto.upper()

# b)
texto.lower()

# c)
texto.title()

# d)
texto.swapcase()

# Exercício 3
insulin_signal = 'MALWMRLLPLLALLALWGPDPAAA'

# a)
print(len(insulin_signal))

# b)
seq_quebrada = insulin_signal.split('LLALLALWG')
print(seq_quebrada)

# c)
seq_concatenada = seq_quebrada[0] + seq_quebrada[1]
print(seq_concatenada)

# d)
seq_final = seq_concatenada.replace('DPAAA', 'LLALL')
print(seq_final)