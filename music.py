class Exception(Exception):
  def __init__ (self, mensagem):
    super().__init__(mensagem)

class Playlist:
  def __init__(self, nome = None, ano = None, album = None, id = None):
    self._name = str(nome)
    self._year = int(ano)
    self._album = str(album)
    self._id = int(id)
    self._right = None
    self._left = None
    self._heigt = 0
  
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
  def id (self, dado):
    self._id = dado

  @property
  def left (self):
    return self._left

  @left.setter
  def left (self, novo):
    self._left = novo

  @property
  def right (self):
    return self._right
  
  @right.setter
  def right (self, novo):
    self._right = novo
  
  def inserir(self, data):
    if (data.id < self._id):
      if (self._left is None):
        self._left = data
      else:
        self._left.inserir(data)
    elif (data.id > self._id):
      if (self._right is None):
        self._right = data
      else:
        self._right.inserir(data)
    elif (data.id == self._id):
      print(f'Esse ID já está em uso\n {self._name} - {self._id}')
  
  def balanco (self):
    profundidadeL = 0
    profundidadeR = 0

    if (self._left):
      profundidadeL = self._left.profundidade()

    if self._right:
      profundidadeR = self._right.profundidade()

    return profundidadeL - profundidadeR
  
  def em_ordem(self, arvore):
    if arvore != None:
      self.em_ordem(arvore.left)
      print(arvore, end='')
      self.em_ordem(arvore.right)
  
  def profundidade(self):
    profL = 0
    profR = 0

    if self._left:
      profL = self.left.profundidade()
    
    if self._right:
      profR = self.right.profundidade()

    return 1 + max(profL, profR)
  
  def buscarId (self, raiz, id):
    if (raiz is None):
      falha = ('Esse ID não existe na Playlist')
      return print(f'\n{falha}')
    
    elif (id == raiz.id):
      sucesso = (f'Nome da música: {raiz.nome}\nAno de lançamento: {raiz.ano}\nÁlbum: {raiz.album}\n')
      return print(f'\n{sucesso}')

    elif (id < raiz.id):
      self.buscarId(raiz.left, id)
    
    elif (id > raiz.id):
      self.buscarId(raiz.right, id)

  def display(self):
    lines, _, _, _ = self._display_aux()
    for line in lines:
      print(line)

  def _display_aux(self):
    if self._right is None and self._left is None:
      line = '%s' % self._id
      width = len(line)
      height = 1
      middle = width // 2
      return [line], width, height, middle

    if self._right is None:
      lines, n, p, x = self._left._display_aux()
      s = '%s' % self._id
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
      second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
      shifted_lines = [line + u * ' ' for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    if self._left is None:
      lines, n, p, x = self._right._display_aux()
      s = '%s' % self._id
      u = len(s)
      first_line = s + x * '_' + (n - x) * ' '
      second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
      shifted_lines = [u * ' ' + line for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    left, n, p, x = self._left._display_aux()
    right, m, q, y = self._right._display_aux()
    s = '%s' % self._id
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '

    if p < q:
      left += [n * ' '] * (q - p)
    elif q < p:
      right += [m * ' '] * (p - q)
        
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


  def __str__ (self):
    output = (f'\nID: {self._id}\nNome da música: {self._name}\nAno de lançamento: {self._year}\nÁlbum: {self._album}\n')

    return output