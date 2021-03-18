def validChar(char):
  if char.isalpha():
    return True
  elif char.isnumeric():
    return True
  elif char == "ε":
    return True
  elif char == "#":
    return True
  else: 
    return False

class leaf:
  def __init__(self,character,pos = None):
    if validChar(character):
      self.typeLeaf = "c"
    else:
      self.typeLeaf = "o"
    self.label = character
    if self.label == 'ε':
      self.primerapos = []
      self.ultimapos = []
      self.anulable = True
    elif validChar(self.label):
      self.pos = pos
      self.primerapos = [pos]
      self.ultimapos = [pos]
      self.anulable = False
  
  def setAnulable(self, flag):
    self.anulable = flag

  def setPrimeraPos (self, primerapos):
    self.primerapos = primerapos

  def setUltimaPos (self, ultimapos):
    self.ultimapos = ultimapos

  def getLabel(self):
    return self.label
  
  def getPos(self):
    return self.pos
  
  def getAnulable(self):
    return self.anulable
  
  def getUltimaPos(self):
    return self.ultimapos
  
  def getPrimeraPos(self):
    return self.primerapos
  
  def getType(self):
    return self.typeLeaf
  
  def toString(self):
    try:
      return "Nodo con pos ",self.pos," tiene la etiqueta ", self.label, " y anulable ",self.anulable
    except:
      return "Nodo con etiqueta ",self.label," tiene primerapos ",self.primerapos, " y tiene ultimapos ",self.ultimapos, " y anulable ",self.anulable