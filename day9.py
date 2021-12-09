data = [list(map(int,line.strip())) for line in open("inputday9")]

def fieldVal(f):
  i,j = f
  return data[i][j]

def adjacent(field):
  fields = []
  i, j = field
  if i > 0:
    fields.append((i-1, j))
  if j > 0:
    fields.append((i, j-1))
  if i < len(data) - 1:
    fields.append((i+1, j))
  if j < len(data[0]) - 1:
    fields.append((i, j+1))
  return fields

def minimum(fields):
  result = (None, 10)
  for field in fields:
    val = fieldVal(field)
    if val < result[1]:
      result = (field, val)
  return result[0]

def basin(field, encountered):
  size = 1
  encountered.append(field)
  for adj in adjacent(field):
    if adj not in encountered and fieldVal(adj) < 9:
      size += basin(adj, encountered)
  return size

lowpoints = []
for i in range(len(data)):
  for j in range(len(data[i])):
    field = (i,j)
    if fieldVal(field) < fieldVal(minimum(adjacent(field))):
      lowpoints.append(field)

basins = sorted([basin(field, []) for field in lowpoints])

print(sum([1 + fieldVal(field) for field in lowpoints]),
      basins[-1] * basins[-2] * basins[-3])
