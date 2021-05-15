class BinaryTreeException(Exception):
  def __init__ (self, mensagem):
    super().__init__(mensagem)

class ArvoreAVL:
  def __init__ (self, nome, ano, album):
    self._name = str(nome)
    self._year = int(ano)
    self._album = str(album)
    self._id = None
    self._right = None
    self._left = None

  @property
  def nome (self):
    return self._name
  
  @nome.setter
  def nome (self, nome):
    self._name = nome
  
  @property
  def ano (self):
    return self._year
  
  @ano.setter
  def ano (self, ano):
    self._year = ano
  
  @property
  def album (self):
    return self._album
  
  @album.setter
  def album (self, album):
    self._album = album
  
  @property
  def id (self):
    return self._id
  
  @id.setter
  def id (self, Id):
    self._id = id(Id)

  @property
  def left (self):
    return self._left

  @left.setter
  def left (self, dado):
    self._left = dado

  @property
  def right (self):
    return self._right
  
  @right.setter
  def right (self, dado):
    self._right = dado
  
  def profundidade (self):
    profundidade_L = 0
    profundidadeR = 0

    if self._left:
      profundidade_L = self._left.profundidade()

    if self._right:
      profundidadeR = self._right.profundidade()

    return 1 + max(profundidade_L, profundidadeR)
  
  def balanco (self):
    profundidadeL = 0
    profundidadeR = 0

    if (self._left):
      profundidadeL = self._left.profundidade()

    if self._right:
      profundidadeR = self._right.profundidade()

    return profundidadeL - profundidadeR
  
  def insere(self, data):
    pass



# def inserir (playlist, musica):
#   if (playlist is None):
#     return musica
#   elif (musica.id < playlist.id):
#     if (playlist.left is None):
#       playlist.left = musica
#     else:
#       inserir(playlist.left, musica)
#   elif (musica.id > playlist.id):
#     if (playlist.right is None):
#       playlist.right = musica
#     else:
#       inserir(playlist.right, musica)
  
#   return playlist
  
# def em_ordem(arvore):
#   if arvore != None:
#     em_ordem(arvore.left)
#     print(arvore, end='')
#     em_ordem(arvore.right)


# def display(self):
#     lines, _, _, _ = self._display_aux()
#     for line in lines:
#       print(line)

#  def _display_aux(self):

#     # No child exists.
#     if self._right is None and self._left is None:
#       line = '%s' % self._id
#       width = len(line)
#       height = 1
#       middle = width // 2
#       return [line], width, height, middle

#     # Only left child exists.
#     if self._right is None:
#       lines, n, p, x = self._left._display_aux()
#       s = '%s' % self._id
#       u = len(s)
#       first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
#       second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
#       shifted_lines = [line + u * ' ' for line in lines]
#       return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

#     # Only right child exists.
#     if self._left is None:
#       lines, n, p, x = self._right._display_aux()
#       s = '%s' % self._id
#       u = len(s)
#       first_line = s + x * '_' + (n - x) * ' '
#       second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
#       shifted_lines = [u * ' ' + line for line in lines]
#       return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

#     # Two children exist.
#     left, n, p, x = self._left._display_aux()
#     right, m, q, y = self._right._display_aux()
#     s = '%s' % self._id
#     u = len(s)
#     first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
#     second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '

#     if p < q:
#       left += [n * ' '] * (q - p)
#     elif q < p:
#       right += [m * ' '] * (p - q)
        
#     zipped_lines = zip(left, right)
#     lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
#     return lines, n + m + u, max(p, q) + 2, n + u // 2