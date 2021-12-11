data = [[[int(val),0] for val in line.strip()] for line in open("inputday11")]
fields, field = [(i,j) for j in range(len(data[0])) for i in range(len(data))], lambda i,j:data[i][j]
adjacent = lambda i,j: [(a,b) for a in range(i-1, i+2) for b in range(j-1, j+2) if a >= 0 and b >= 0 and a < len(data) and b < len(data[0])]

def octopus(i, j, step):
  flashes = 0
  if field(i,j)[0] > 9 and field(i,j)[1] != step:
    flashes += 1
    field(i,j)[1] = step
    for a,b in adjacent(i,j):
      field(a,b)[0] += 1
      flashes += octopus(a, b, step)
  return flashes

sync = flashes = step = 0

while not sync or step <= 100:
  step += 1
  for i,j in fields: field(i,j)[0] += 1
  for i,j in fields: flashes += octopus(i, j, step) * (step <= 100)
  for i,j in fields: field(i,j)[0] = 0 if field(i,j)[1] == step else field(i,j)[0]
  if not sum(map(lambda x:field(*x)[0], fields)) and not sync: sync = step

print(flashes, sync)
