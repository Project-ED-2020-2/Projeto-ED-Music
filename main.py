from music import Playlist

if __name__ == '__main__':

  arvoreMusical = Playlist('Lonely', 2004, 'Trouble', 1)
  m1 = Playlist('Batom cereja', 2021, 'Aqui e agora', 2)
  m2 = Playlist('Foi pá pum', 2020, 'Debaixo do meu telhado', 3)
  m3 = Playlist('Laços de familia', 2004, 'Alma gêmea', 4)

  arvoreMusical.inserir(m1)
  arvoreMusical.inserir(m2)
  arvoreMusical.inserir(m3)

  arvoreMusical.display()

  arvoreMusical.em_ordem(arvoreMusical)

  print()

  # def imprimeMenu():
  #   print(f'''
  #                       Music

  #       |  [1]    Cadastrar Nova Playlist     |
  #       |  [2]     Acrescentar Música         |
  #       |  [3]     Buscar Música por ID       |
  #       |  [4]   Exibir Maior e Menor Idade   |
  #       |  [5]   Ordernar Surfistas Por Nome  |
  #       |  [6]   Exibir Surfistas Cadastrados |
  #       |  [7] Mostrar Quantidade de Surfitas |
  #       |  [8]       Remover um Surfista      |
  #       |  [9]             SAIR               |\n''')

  # imprimeMenu()
  # interacao = int(input('Digite qual opção você deseja acessar: '))