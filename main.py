from arvoreBinaria import *
from music import Musica

if __name__ == '__main__':
  arvoreMusical = None

  m1 = Musica('Blue bird', 2002, 'Narutin', 1)
  m2 = Musica('Sassageyo', 2002, 'SNK', 2)
  m3 = Musica('Dance monkey', 2002, 'One piece', 3)

  arvoreMusical = inserir(arvoreMusical, m1)
  arvoreMusical = inserir(arvoreMusical, m2)
  arvoreMusical = inserir(arvoreMusical, m3)

  print(arvoreMusical)
