lines=[*map(eval,open("inputday18"))]

class Node:
  def __init__(self, value, parent = None):
    self.parent = parent
    self.nest = (parent.nest + 1) if parent else 0
    if type(value) == list:
      self.pair = True
      self.leftChild, self.rightChild = map(lambda n:Node(n,self), value)
    elif type(value) == Node:
      self.pair = value.pair
      if self.pair: self.leftChild, self.rightChild = Node(value.leftChild, self), Node(value.rightChild, self)
      else: self.val = value.val
    else:
      self.val = value
      self.pair = False

  def __repr__(self):
    if not self.pair: return str(self.val)
    return '['+str(self.leftChild)+','+str(self.rightChild)+']'

  def findExplode(self):
    if self.pair:
      if self.nest >= 4: return self
      return self.leftChild.findExplode() or self.rightChild.findExplode()
    return False

  def findSplit(self):
    if not self.pair:
      if self.val >= 10: return self
      return False
    return self.leftChild.findSplit() or self.rightChild.findSplit()

  def firstValL(self):
    if self.pair: return self.leftChild.firstValL() or self.rightChild.firstValL()
    return self

  def firstValR(self):
    if self.pair: return self.rightChild.firstValR() or self.leftChild.firstValR()
    return self

  @staticmethod
  def _findLeft(root, val):
    if not root: return False
    if root.leftChild == val: return Node._findLeft(root.parent, root)
    return root.leftChild.firstValR()

  def findLeft(self):
    return Node._findLeft(self.parent, self)

  @staticmethod
  def _findRight(root, val):
    if not root: return False
    if root.rightChild == val: return Node._findRight(root.parent, root)
    return root.rightChild.firstValL()

  def findRight(self):
    return Node._findRight(self.parent, self)

  def explode(self):
    expl = self.findExplode()
    if not expl: return False
    fL = expl.findLeft()
    fR = expl.findRight()
    if fL: fL.val += expl.leftChild.val 
    if fR: fR.val += expl.rightChild.val
    expl.pair = False
    expl.val = 0
    return True
    
  def split(self):
    splt = self.findSplit()
    if not splt: return False
    splt.pair = True
    splt.leftChild = Node(splt.val // 2, splt)
    splt.rightChild = Node(-int((-splt.val / 2) // 1), splt)
    return True

  def reduce(self):
    action = True
    while action:
      action = self.explode()
      if not action: action = self.split()
    return self

  def magnitude(self):
    if not self.pair: return self.val
    return 3 * self.leftChild.magnitude() + 2 * self.rightChild.magnitude()

  @staticmethod
  def add(node1, node2):
    return Node([node1, node2]).reduce()

roots = [*map(Node,lines)]; result = roots[0]
for i in range(1, len(roots)): result = Node.add(result, roots[i])
print(result.magnitude(), max([Node.add(roots[i], roots[j]).magnitude() for i in range(len(roots)) for j in range(len(roots)) if i != j]))
