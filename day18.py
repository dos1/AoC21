lines=[*map(eval,open("inputday18"))]

class Node:
  def __init__(self, value, parent = None):
    self.parent = parent
    self.nest = (parent.nest + 1) if parent else 0
    if type(value) == list:
      self.pair = True
      self.left, self.right = map(lambda n:Node(n,self), value)
    elif type(value) == Node:
      self.pair = value.pair
      if self.pair: self.left, self.right = Node(value.left, self), Node(value.right, self)
      else: self.val = value.val
    else:
      self.val = value
      self.pair = False

  def __repr__(self):
    if not self.pair: return repr(self.val)
    return '[%s,%s]' % (self.left, self.right);

  def findExplode(self):
    if self.pair:
      if self.nest >= 4: return self
      return self.left.findExplode() or self.right.findExplode()
    return False

  def findSplit(self):
    if not self.pair:
      if self.val >= 10: return self
      return False
    return self.left.findSplit() or self.right.findSplit()

  def firstValL(self):
    if self.pair: return self.left.firstValL() or self.right.firstValL()
    return self

  def firstValR(self):
    if self.pair: return self.right.firstValR() or self.left.firstValR()
    return self

  @staticmethod
  def _findLeft(root, val):
    if not root: return False
    if root.left == val: return Node._findLeft(root.parent, root)
    return root.left.firstValR()

  def findLeft(self):
    return Node._findLeft(self.parent, self)

  @staticmethod
  def _findRight(root, val):
    if not root: return False
    if root.right == val: return Node._findRight(root.parent, root)
    return root.right.firstValL()

  def findRight(self):
    return Node._findRight(self.parent, self)

  def explode(self):
    expl = self.findExplode()
    if not expl: return False
    if fL := expl.findLeft(): fL.val += expl.left.val
    if fR := expl.findRight(): fR.val += expl.right.val
    expl.pair = False
    expl.val = 0
    return True
    
  def split(self):
    splt = self.findSplit()
    if not splt: return False
    splt.pair = True
    splt.left = Node(splt.val // 2, splt)
    splt.right = Node(-int((-splt.val / 2) // 1), splt)
    return True

  def reduce(self):
    action = True
    while action:
      action = self.explode()
      if not action: action = self.split()
    return self

  def magnitude(self):
    if not self.pair: return self.val
    return 3 * self.left.magnitude() + 2 * self.right.magnitude()

  def __add__(self, node2):
    return Node([self, node2]).reduce()

nodes=[*map(Node,lines)]
print(sum(nodes[1:],nodes[0]).magnitude(),max([(nodes[i]+nodes[j]).magnitude() for i in range(len(nodes)) for j in range(len(nodes)) if i!=j]))
