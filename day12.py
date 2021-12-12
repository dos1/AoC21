data=[line.strip().split('-') for line in open("inputday12")]
paths = {}
for x,y in data:
  for a,b in ((x,y),(y,x)):
    paths[a] = paths[a]+[b] if paths.get(a) else [b]

def islowertaken(a):
  for i in a:
    if i != 'start' and i.islower() and a.count(i) > 1: return i
  return None

def visit(path, visited, roads, allowlowertwice):
  if path == 'end':
    roads.append([*visited, 'end'])
    return
  if path.islower() and path in visited:
    if not allowlowertwice or path == 'start' or islowertaken(visited):
      return
  visited = [*visited, path]
  for road in paths[path]:
    visit(road, visited, roads, allowlowertwice)
  return len(roads)

print(visit('start',[],[],0), visit('start',[],[],1))
