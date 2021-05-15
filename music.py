class Musica:
  def __init__(self, nome, ano, album):
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

  def __str__ (self):
    output = (f'Playlist:\n')
    output += (f'\nID: {self._id}\nNome da música: {self._name}\nAno de lançamento: {self._year}\nÁlbum: {self._album}')
    return output
  