class BinaryTreeException(Exception):
  def __init__ (self, mensagem):
    super().__init__(mensagem)

class ArvoreBinaria:
  def __init__ (self, dado):
    self._data = dado
    self._left = None
    self._right = None
  
  @property
  def date (self):
    return self._data
  
  @date.setter
  def date (self, dado):
    self._data = dado

  @property
  def left (self):
    return self._left

  @left.setter
  def left (self, dado):
    if self._left != None:
      raise BinaryTreeException('O nó esquerdo já existe')
    else:
      self._left = dado

  @property
  def right (self):
    return self._right
  
  @right.setter
  def right (self, dado):
    if self._right != None:
      raise BinaryTreeException('O nó direito já existe')
    else:
      self._right = dado


def inserir (arvore, musica):
  if (arvore is None):
    return musica
  elif (arvore.nome > musica.nome):
    arvore.left = inserir(musica.left, arvore)
  elif (arvore.nome < musica.nome):
    musica.right = inserir(musica.right, arvore)
  elif(arvore.nome == musica.nome):
    print('A música já existe!')

  return arvore