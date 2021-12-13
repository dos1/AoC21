x=open("inputday13").read().strip().split('\n\n')
d=[(*map(int,l.strip().split(',')),)for l in x[0].split('\n')]
folds=((a[0],int(a[1]))for a in[l.strip().split('=')for l in x[1].split('\n')])
maxX,maxY=(max([a[i]for a in d])for i in (0,1))

def fold(data, maxX, maxY, axis, value):
  folded = set()
  for i,j in data:
    if axis[-1]=='x':
      newI = 2 * value - i
      folded.add((newI,j) if i > value else (i,j))
      maxX = value - 1
    else:
      newJ = 2 * value - j
      folded.add((i,newJ) if j > value else (i,j))
      maxY = value - 1
  return (folded, maxX, maxY)

for i,f in enumerate(folds):
  d, maxX, maxY = fold(d, maxX, maxY, *f)
  if i==0:
    print(len(d))

for j in range(maxY+1):
  for i in range(maxX+1):
    print("#" if (i,j) in d else '.', end='')
  print()
